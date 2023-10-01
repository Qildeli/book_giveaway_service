from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Model for storing book details
class Book(models.Model):
    BOOK_STATUS_CHOICES = (
        ('Available', 'Available'),
        ('Reserved', 'Reserved'),
        ('Given Away', 'Given Away')
    )

    title = models.CharField(max_length=200, blank=False, db_index=True)
    description = models.TextField()
    published_date = models.DateField()
    genre = models.ManyToManyField('Genre')
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    condition = models.ForeignKey('BookCondition', on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='book_covers/')  # For storing book cover images
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pickup_location = models.ForeignKey('PickupLocation', on_delete=models.SET_NULL, null=True)  # Location details for book retrieval
    status = models.CharField(max_length=20, choices=BOOK_STATUS_CHOICES, default='Available')
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="received_books")  # For ownership decisions


    def __str__(self):
        return self.title


# Model for storing author details
class Author(models.Model):
    name = models.CharField(max_length=200, blank=False, db_index=True)
    biography = models.TextField(blank=True)  # Can be blank
    birth_date = models.DateField(null=True, blank=True)  # Can be null

    def __str__(self):
        return self.name


# Model for book genres
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)  # Unique genre name

    def __str__(self):
        return self.name


# Model for storing condition of the book (e.g. New, Used, etc.)
class BookCondition(models.Model):
    condition_label = models.CharField(max_length=100, unique=True, blank=False) # Unique condition label

    def __str__(self):
        return self.condition_label


# Model to manage book pickup location tied to each user
class PickupLocation(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=245)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    additional_details = models.TextField(blank=True)  # Can be blank

    def __str__(self):
        return f"{self.address}, {self.city}, {self.state}, {self.country}"


# Model to manage and track book requests and owner's decisions
class BookRequest(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected')
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='requests')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='book_requests')
    request_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True) # Can be blank
    owner_response = models.TextField(blank=True)  # Owner's response message
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Request for {self.book.title} by {self.user.username} - {self.status}"
