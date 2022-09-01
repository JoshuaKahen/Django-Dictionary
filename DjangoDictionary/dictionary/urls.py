# from current folder, we are importing the two views, HomeView & SearchView
from . import views
# importing path from django's in-built urls
from django.urls import path

# defining the list for urls
urlpatterns = [
    path('', views.homeView, name='home'),
    path('search', views.searchView, name='search'),
]