from django.contrib import admin
from .models import Book, Author, Genre, BookCondition, PickupLocation, BookRequest


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookCondition)
admin.site.register(PickupLocation)
admin.site.register(BookRequest)

