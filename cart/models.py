from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie

###Collect: id, date, total, user
#store id, quant, price, movie, order
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    #auto inc id for each user
    total = models.IntegerField()
    #total amt of orders
    date = models.DateTimeField(auto_now_add=True)
    #date and time order was created
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #connects user, on_delete = if user is del, assoc orders are del
    def __str__(self):
        return str(self.id) + ' - ' + self.user.username


#str is item id and assoc movie name
#item is in order (item is the movie purchased, order is the overarching)
    #the item includes order info
class Item(models.Model):
    id = models.AutoField(primary_key = True)
    price = models.IntegerField()
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    def __str__(self): 
        return str(self.id) + ' - ' + self.movie.name
# Create your models here.

#(theory) we have order and item separated because we want to be able to change nested data
#MVT --> model-view-template