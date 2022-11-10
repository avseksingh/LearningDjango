from django.shortcuts import render


# from siteclasses import Book


def index(request):
    # https://docs.djangoproject.com/en/dev/ref/contrib/admin/#reversing-admin-urls
    links = ["admin:index", "aggregates", "all", "between", "initial", "formdata"]
    return render(request, "home.html", {"links": links})


def test(request):
    return render(request, "bootstrap.html")
