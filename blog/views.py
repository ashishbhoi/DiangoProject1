from django.shortcuts import render

posts = [
    {
        'author': 'CoryeMS',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'August 27, 2019'
    },
    {
        'author': 'Jyn Doe',
        'title': 'Blog Post 1',
        'content': 'Second Post Content',
        'date_posted': 'August 30, 2019'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
