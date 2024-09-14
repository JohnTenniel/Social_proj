from django.shortcuts import render


def main(request):
    return render(request, "mainweb/main.html")

def blog(request):
    return render(request, "mainweb/blog.html")
