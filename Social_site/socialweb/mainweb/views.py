from django.shortcuts import render


def main(request):
    return render(request, "mainweb/main.html")
