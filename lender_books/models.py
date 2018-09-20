from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    STATES = [
        ('incomplete', 'Incomplete'),
        ('complete', 'Complete'),
    ]

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=48)
    author = models.CharField(max_length=4096)
    year = models.CharField(max_length=48)
    status = models.CharField(choices=STATES, default='incomplete', max_length=48)
    date_added = models.DateTimeField(auto_now_add=True, blank=True)
    last_borrowed = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f'Book: {self.title} ({self.status})'

    def __repr__(self):
        return f'Book: {self.title} ({self.status})'
