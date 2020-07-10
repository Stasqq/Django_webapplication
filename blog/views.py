from django.shortcuts import render

posts = [
    {
        'author': 'Stasq',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '09.07.2020r.'
    },
{
        'author': 'Stasq',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '10.07.2020r.'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})