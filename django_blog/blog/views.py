from django.shortcuts import render

posts = [
    {
        'author': 'Andrew',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 4, 2023'
    },
    {
        'author': 'James',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 5, 2023'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


