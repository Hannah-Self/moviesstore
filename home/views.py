from django.shortcuts import render

# Create your views here.
def index(request):
    template_data = {}
    template_data['title'] = 'Movies Store'
    #changes tab name to Movies Store
    return render(request, 'home/index.html', {
        'template_data': template_data})

#imports render, defines index, returns rendered template
#connected '' with views.index

def about(request): 
    template_data = {}
    template_data['title'] = 'About'
    return render(request, 'home/about.html',
                  {'template_data': template_data})
