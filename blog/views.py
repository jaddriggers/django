from django.shortcuts import render

post = [
    {
        'author': 'Jad',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 30, 1977'
    },
    {
        'author': 'Keira',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'June 05, 2011'
    }
]

def home(request):
    context = {
        'posts': post
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

