from django.contrib import admin

# Register your models here.
from.models import Movie, Review, Report

#order movies by name
class MovieAdmin(admin.ModelAdmin): 
    ordering = ['name']
    #MovieAdmin class inherits admin.ModelAdmin --> allow custom
    #set ordering by name
    #regster Movie model with custom admin (below)

    search_fields = ['name']
    #allow search by name

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)
admin.site.register(Report)

