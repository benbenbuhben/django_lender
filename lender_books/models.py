from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils import timezone


class Book(models.Model):
    STATES = [
        ('available', 'Available'),
        ('checked out', 'Checked Out'),
    ]

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=48)
    author = models.CharField(max_length=4096)
    year = models.CharField(max_length=48)
    status = models.CharField(choices=STATES, default='available', max_length=48)
    date_added = models.DateTimeField(auto_now_add=True, blank=True)
    last_borrowed = models.DateTimeField(blank=True, null=True)
    pre_save_status = models.CharField(max_length=48, editable=False)

    def __str__(self):
        return f'Book: {self.title} ({self.status})'

    def __repr__(self):
        return f'Book: {self.title} ({self.status})'


@receiver(models.signals.post_save, sender=Book)
def set_book_borrowed_date(sender, instance, **kwargs):
    if instance.status == 'checked out' and instance.pre_save_status == 'available':
        instance.last_borrowed = timezone.now()
        instance.pre_save_status = 'checked out'
        instance.save()


@receiver(models.signals.pre_save, sender=Book)
def set_pre_save_status(sender, instance, **kwargs):
    if instance.status == 'available':
        instance.pre_save_status = 'available'

