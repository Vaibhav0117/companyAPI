from django.http import HttpResponse


def home_page():
    print("Home Page Returned")
    return HttpResponse('This Is Home Page')