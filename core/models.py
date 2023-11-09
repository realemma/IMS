from django.db import models

from store.models import Category,Location,Item

# Create your models here.


class Request(models.Model):
    UNCOM= 'uncompleted'
    APPROVED='approved'
    PENDING= 'pending'
    REJECTED = 'rejected'

    STATUS_CHOICES=(
        (UNCOM, 'uncompleted'),
        (PENDING, 'pending'),
        (REJECTED,'rejected'),
        (APPROVED, 'approved'),

    )
    item = models.ForeignKey(Item, related_name='request', on_delete=models.CASCADE )
    category = models.ForeignKey(Category, related_name='request', on_delete=models.CASCADE )
    location = models.ForeignKey(Location, related_name='request', on_delete=models.CASCADE )
    quantity = models.PositiveIntegerField(default=0)
    transaction_id = models.CharField(max_length=50,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comments = models.TextField(null=True)
    slug = models.SlugField(max_length=50, null=True, default='REQ001')
    status=models.CharField(max_length=50, choices=STATUS_CHOICES, default=UNCOM)


    def __str__(self):
        return self.category.title