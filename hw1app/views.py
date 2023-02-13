from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def firsturl(request):
    return HttpResponse("Hello, im first!")


def secondurl(request):
    return HttpResponse("yes yes, im second")

def nexturl(request):
    return HttpResponse("next")

def afternexturl(request):
    return HttpResponse("one more")

def first_dynamic_url(request, article_number):
    if article_number >= 5:
        return HttpResponse("Big numbers for big boys")
    else:
        return HttpResponse("try one more time")

def second_dynamic_url(request, article_number):
    if article_number >= 5:
        return HttpResponse("Big numbers for big boys")
    else:
        return HttpResponse("try one more time")

def third_dynamic_url(request, article_number):
    return HttpResponse("Nice to meet you in Archive")

def fourth_dynamic_url(request, article_number, slug_text):
    return HttpResponse(f"Text url must be {slug_text} after {article_number}")

def fifth_dynamic_url(reqest, users_number):
    return HttpResponse(f"user number is {users_number}")

def regex(request, regular):
    return HttpResponse(f"it's regexp: {regular}")

def phone(request, reg):
    return HttpResponse(f"it's phone number: {reg}")

