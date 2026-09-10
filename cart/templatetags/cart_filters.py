#django filters allows to modify or format data in template
#filters use pipe | char for custom presentation of data in template
#LIST movies added to cart, display quantity of movie
    #access cart session data, use movie ID as key to get QUANTITY

from django import template
register = template.Library()
    #intance of template.Library for custom tags and filters
@register.filter(name='get_quantity') 
    #register function as custom template filter
def get_cart_quantity(cart, movie_id):
    #define func to access quantity value by using dict and id as key
    return cart[str(movie_id)] 
    #convert to string to make compat with cart keys and return corr quant val

#once custom filter is defined, registered, can use in Django template like: 
    #{{ request.session.cart|get_quantity:movie.id }}