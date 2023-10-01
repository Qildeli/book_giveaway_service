from django.urls import path
from .views import (BookListCreate, BookRetrieveUpdateDestroy, AuthorListCreate,
                    BookRequestListCreate, BookRequestRetrieveUpdateDestroy,
                    GenreListCreate, GenreRetrieveUpdateDestroy,
                    BookConditionListCreate, BookConditionRetrieveUpdateDestroy,
                    PickupLocationListCreate, PickupLocationRetrieveUpdateDestroy, AcceptBookRequest)

urlpatterns = [
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroy.as_view(), name='book-retrieve-update-destroy'),

    path('authors/', AuthorListCreate.as_view(), name='author-list-create'),
    path('genres/', GenreListCreate.as_view(), name='genre-list-create'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroy.as_view(), name='genre-retrieve-update-destroy'),

    path('conditions/', BookConditionListCreate.as_view(), name='condition-list-create'),
    path('conditions/<int:pk>/', BookConditionRetrieveUpdateDestroy.as_view(), name='condition-retrieve-update-destroy'),

    path('pickup-locations/', PickupLocationListCreate.as_view(), name='pickup-location-list-create'),
    path('pickup-locations/<int:pk>/', PickupLocationRetrieveUpdateDestroy.as_view(), name='pickup-location-retrieve-update-destroy'),

    path('book-requests/', BookRequestListCreate.as_view(), name='book-request-list-create'),
    path('book-requests/<int:pk>/', BookRequestRetrieveUpdateDestroy.as_view(),
         name='book-request-retrieve-update-destroy'),
    path('book-requests/<int:request_id>/accept/', AcceptBookRequest.as_view(), name='accept-book-request'),
]
