from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# each model is a class that extends django.db.models.Model
# each model attribute represents a database column
# Django provides us with a set of useful methods to CRUD (create, update, read, delete) this info from db

class Movie(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='movie_images/')
    def __str__(self): 
        return str(self.id) + ' - ' + self.name
#python class inherits models.Model
#Movie is Django model class
    #id --> autofield val, inc val for each new record added
    #primary_key=True --> this is pri key for table (unique)
    #name is charfield for movie name, price (int), description (text), image (img)
        #for image --> upload_to says where to store
    #__str__ = python what it returns is string (converts id to str for display)

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self): 
        return str(self.id) + ' - ' + self.movie.name

#import User model from Django
#define python class called Review(inherits Django model)
#id = autofield, auto inc value for each new record
#primary_key=true --> field is primary key (id)
#comment (char) --> str field of max length 255 (review)
#date --> tracks date/time
#auto_now_add=True --> ensures date/time auto set to curr
#movie --> foreign key, assoc review to movie
#on_delete --> handles delete movie of assoc review
    #=models.CASCADE --> if movie del, assoc review del too
#user --> foreign key --> review assoc w/user, same as above
#__str__ --> returns string review

class Report(models.Model):
    id = models.AutoField(primary_key=True)
    reason = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    # review = models.CharField(max_length=500)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id) + ' - ' + self.movie.name

#MODELS in Django are used when you need to manipulate the db later on
    #don't use if its just a static output