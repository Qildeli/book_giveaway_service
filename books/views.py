from rest_framework import generics, permissions, status
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book, Author, Genre, BookCondition, PickupLocation, BookRequest
from .serializers import (BookSerializer, AuthorSerializer, GenreSerializer,
                          BookConditionSerializer, PickupLocationSerializer, BookRequestSerializer)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of a book to edit it.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'genre', 'condition', 'status']

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("You must be logged in to add a book")
        serializer.save(owner=self.request.user)


class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        book = self.get_object()
        if self.request.user != book.owner:
            raise PermissionDenied("You don't have permission to modify this book")
        serializer.save()


class AuthorListCreate(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GenreListCreate(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GenreRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookConditionListCreate(generics.ListCreateAPIView):
    queryset = BookCondition.objects.all()
    serializer_class = BookConditionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookConditionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookCondition.objects.all()
    serializer_class = BookConditionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PickupLocationListCreate(generics.ListCreateAPIView):
    queryset = PickupLocation.objects.all()
    serializer_class = PickupLocationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Ensure that the pickup location is associated only with the authenticated user
        serializer.save(user=self.request.user)


class PickupLocationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PickupLocation.objects.all()
    serializer_class = PickupLocationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookRequestListCreate(generics.ListCreateAPIView):
    queryset = BookRequest.objects.all()
    serializer_class = BookRequestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        book = Book.objects.get(pk=self.request.data['book'])
        if book.owner == self.request.user:
            raise ValidationError("You can't request your own book.")
        serializer.save(user=self.request.user)


class BookRequestRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookRequest.objects.all()
    serializer_class = BookRequestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AcceptBookRequest(generics.GenericAPIView):
    queryset = BookRequest.objects.all()
    serializer_class = BookRequestSerializer
    lookup_url_kwarg = 'request_id'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        book_request = self.get_object()
        book = book_request.book

        if book.owner != request.user:
            raise PermissionDenied("You do not have permission to accept this request.")

        # Update the book status to Reserved
        book.status = 'Reserved'
        book.save()

        BookRequest.objects.filter(book=book).exclude(id=book_request.id).update(status=BookRequest.REJECTED)
        book_request.status = BookRequest.ACCEPTED
        book_request.save()

        return Response({"message": "Request accepted successfully."}, status=status.HTTP_200_OK)

