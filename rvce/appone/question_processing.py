
from gensim import corpora, models, similarities
from gensim.similarities import MatrixSimilarity
import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import numpy as np
from nltk import ne_chunk, pos_tag
from nltk.tree import Tree
import re
from dateutil import parser
from summa import summarizer

nltk.download("wordnet")
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
def extract_event_time(doc):
    sentences = re.findall(r'\b([A-Z][^\.!?]*[\.!?])', doc)
    event_time = None
    for sentence in sentences:
        try:
            event_time = parser.parse(sentence, fuzzy=True)
            break  # Stop iterating if a valid time is found
        except ValueError:
            pass
    return event_time

def time(query):
    
    documents=open("time_questions.txt").readlines()
    query=remove_punctuation(query)
    processed_docs=[remove_punctuation(doc.lower()).split() for doc in documents]
    dictionary = corpora.Dictionary(processed_docs)

    corpus = [dictionary.doc2bow(doc) for doc in processed_docs]
    tfidf = models.TfidfModel(corpus)

    corpus_tfidf = tfidf[corpus]
    index = MatrixSimilarity(corpus_tfidf)
    query_bow = dictionary.doc2bow(query.lower().split())
    query_tfidf = tfidf[query_bow]
    sims = index[query_tfidf]
    return max(sims)>0.6
def summarize(doc):
    return summarizer.summarize(doc,ratio=0.1)
def clean_text(query):
    query=remove_stopwords(query)
    query=remove_punctuation(query)
    query=remove_question_words(query)
    return query

def summarizable(query):

    query=remove_stopwords(query)
    documents=open("summary_questions.txt").readlines()

    processed_docs=[remove_stopwords(doc.lower()).split() for doc in documents]
    dictionary = corpora.Dictionary(processed_docs)

    corpus = [dictionary.doc2bow(doc) for doc in processed_docs]
    tfidf = models.TfidfModel(corpus)

    corpus_tfidf = tfidf[corpus]
    index = MatrixSimilarity(corpus_tfidf)
    query_bow = dictionary.doc2bow(query.lower().split())
    query_tfidf = tfidf[query_bow]
    sims = index[query_tfidf]
    return max(sims)>0.6



def remove_question_words(text):
    question_words = ['what', 'when', 'where', 'who', 'whom', 'which', 'why', 'how']
    words = word_tokenize(text.lower())  
    filtered_words = [word for word in words if word not in question_words]
    cleaned_text = ' '.join(filtered_words)

    return cleaned_text


def remove_stopwords(query):
    lemmatizer=WordNetLemmatizer()
    query=remove_punctuation(query)
    tokens=word_tokenize(query)
    stop_words=set(stopwords.words("english"))
    normalized_tokens = [token for token in tokens if token not in stop_words]
    normalized_tokens=[lemmatizer.lemmatize(token) for token in normalized_tokens]
    # Join the tokens back into a sentence
    normalized_query = ' '.join(normalized_tokens)
    return normalized_query

def remove_punctuation(text):
    text_without_punct = re.sub(r'[^\w\s]', '', text)
    return text_without_punct



# Example documents
def response(query,filename):

    documents=open(filename).read()
    docs=documents
    if(summarizable(query)):
        return summarize(documents)
        
    if(time(query)):

        return extract_event_time(docs)
        
    
    documents=documents.replace("\n"," ").split(".")
    processed_docs=[remove_stopwords(doc.lower()).split() for doc in documents]
    dictionary = corpora.Dictionary(processed_docs)


    corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

    tfidf = models.TfidfModel(corpus)


    corpus_tfidf = tfidf[corpus]


    index = MatrixSimilarity(corpus_tfidf)
    query=clean_text(query)
    query_bow = dictionary.doc2bow(query.lower().split())
    query_tfidf = tfidf[query_bow]

    sims = index[query_tfidf]
    similarity_scores = sorted(enumerate(sims), key=lambda item: -item[1])
    if len(documents[similarity_scores[0][0]].split())<10:
        del similarity_scores[0]
    if similarity_scores[0][1]==0:
        print("Sorry cannot get the information")
    else:
        scores=[i[1] for i in similarity_scores]
        std_score=np.std(scores)
        max_score=similarity_scores[0][1]
        
        answer=[]
        for i in similarity_scores:
            if abs((i[1])-(max_score))<std_score:
                answer.append(documents[i[0]])
        return "\n".join(answer)
  
    
    # most_similar_document_index = similarity_scores[0][0]
    # most_similar_document = documents[most_similar_document_index]
    # print("Most similar document:", most_similar_document)
