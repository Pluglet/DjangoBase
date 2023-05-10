"""
URL configuration for core project.
"""

from django.shortcuts import render


def landing(request):
    """
    Landing page view.
    :param request:
    :return:
    """
    return render(request, "landing.html")


def home(request):
    """
    Home page view.
    :param request:
    :return:
    """
    return render(request, "home.html")


def about(request):
    """
    About page view.
    :param request:
    :return:
    """
    return render(request, "about.html")


def contact(request):
    """
    Contact page view.
    :param request:
    :return:
    """
    return render(request, "contact.html")
