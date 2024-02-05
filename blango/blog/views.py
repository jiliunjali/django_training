from django.shortcuts import render
from django.views.generic import ListView, DetailView #listview help us by looking through the list, it brings the list , while detailview bring out the detail of maybe ...say a element of  the list
from .models import Post

# Create your views here.
# def home(request):
#     return render(request,'home.html',{})
class HomeView(ListView): # listview is passed as we want to list all of our blogs on that page
    model = Post #model we are going to use in this page
    template_name='home.html'
    
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'