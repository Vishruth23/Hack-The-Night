from django.db import models

class NGO(models.Model):
    username = models.CharField(max_length=150, unique=True)
    profile_pic = models.ImageField(upload_to='profilepics/ngos',blank=True)
    email = models.EmailField(unique=True,null=True,blank=True)
    password = models.CharField(max_length=128)
    bio_and_works = models.TextField()

class NGODetails(models.Model):
    username = models.ForeignKey(NGO,on_delete=models.CASCADE)
    category = models.CharField(max_length=150)
    rating = models.IntegerField()

class Volunteer(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True,null=True,blank=True)
    password = models.CharField(max_length=128)
    profile_pic = models.ImageField(upload_to='profilepics/ngos',blank=True)

    def __str__(self):
        return self.username

class Author(models.Model):
    user = models.ForeignKey(NGO, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.ForeignKey(Volunteer, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
