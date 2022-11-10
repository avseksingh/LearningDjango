from django.contrib import admin
from .models import BooksModel,Reader,TestBook
admin.site.register(BooksModel)
admin.site.register(Reader)
admin.site.register(TestBook)
# Register your models here.
