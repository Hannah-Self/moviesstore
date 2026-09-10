from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Review, Report
from django.contrib.auth.decorators import login_required
# Create your views here.

#we used to have movies here (dummy), but we now reference direct from db (admin)
#we have removed dummy data, replace with db ref
def index(request):
    #retrieve all movies if search is not sent in curr reque, or retrieve specific based on search
    search_term = request.GET.get('search')
    if search_term: 
        movies = Movie.objects.filter(name__icontains=search_term)
    else: 
        movies = Movie.objects.all()
    template_data = {}
    template_data['title'] = 'Movies'
    template_data['movies'] = movies
    return render(request, 'movies/index.html',
                {'template_data': template_data})

def show(request, id):
    movie = Movie.objects.get(id=id)
    reviews = Review.objects.filter(movie=movie)

    template_data = {}
    template_data['title'] = movie.name
    template_data['movie'] = movie
    template_data['reviews'] = reviews
    return render(request, 'movies/show.html',
                {'template_data': template_data})

#request and id in show, extract movie data, pass to movies/show.html

@login_required
def report_review(request, id, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.method == 'GET':
        template_data = {}
        template_data['title'] = 'REPORT THIS REVIEW!'
        template_data['review'] = review
        return render(request, 'movies/report_review.html', {'template_data': template_data})
    elif request.method =='POST' and request.POST['reason'] != '':
        reviewDel = Review.objects.get(id=review_id)
        movie = Movie.objects.get(id=id)
        report = Report()
        report.reason = request.POST['reason']
        report.movie = movie
        report.user = request.user
        # report.review = reviewDel.comment
        report.save()
        review.delete()
        return redirect('movies.show', id=id)
    else: 
        return redirect('movies.show', id=id)

@login_required
def create_review(request, id):
    if request.method == 'POST' and request.POST['comment'] != '':
        movie = Movie.objects.get(id=id)
        review = Review()
        review.comment = request.POST['comment']
        review.movie = movie
        review.user = request.user
        review.save()
        return redirect('movies.show', id=id)
    else:
        return redirect('movies.show', id=id)
#verify with login_requred, create_review func handles creation
#create_review takes in http req and id, check if post, then apply comment
#apply connect between comment, movie, user

@login_required
def edit_review(request, id, review_id): 
    review = get_object_or_404(Review, id=review_id)
    if request.user != review.user:
        return redirect('movies.show', id=id)
    if request.method == 'GET':
        template_data = {}
        template_data['title'] = 'Edit Review'
        template_data['review'] = review
        return render(request, 'movies/edit_review.html', {'template_data': template_data})
    elif request.method =='POST' and request.POST['comment'] != '':
        review = Review.objects.get(id=review_id)
        review.comment = request.POST['comment']
        review.save()
        return redirect('movies.show', id=id)
    else: 
        return redirect('movies.show', id=id)

@login_required
def delete_review(request, id, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    review.delete() #Django model delete()
    return redirect('movies.show', id=id)

    # if request.method == 'POST' and request.POST['report'] != '':
    #     movie = Movie.objects.get(id=id)
    #     report = Report()
    #     report.report = request.POST['report']
    #     report.movie = movie
    #     report.user = request.user
    #     report.save()
    #     review.delete()
    #     return redirect('movies.show', id=id)
    # else: 
    #     return redirect('movies.show', id=id)

    