from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='movies.index'),
    path('<int:id>/', views.show, name='movies.show'),
    path('<int:id>/review/create/', views.create_review, name='movies.create_review'),
    path('<int:id>/review/<int:review_id>/edit/', views.edit_review, name='movies.edit_review'),
    path('<int:id>/review/<int:review_id>/delete/', views.delete_review, name='movies.delete_review'),
    path('<int:id>/review/<int:review_id>/report/', views.report_review, name='movies.report_review'),
]

#<int:id> indicates that the path expects int value passed from url
#int will be assoc with a var named id, which identifies movie data to show
#What movie corresponds to the id that we want to show?