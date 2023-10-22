from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    pass
class BaseMode(models.Model):
    create_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateField(auto_now=True, null=True)
    active = models.BooleanField(default=True)
    class Meta:
        abstract = True
class Category(BaseMode):
    name = models.CharField(max_length=50, null = False)
    def __str__(self):
        return self.name
class Course(BaseMode):
    subjects = models.CharField(max_length=50, null = False)
    des = models.TextField()
    image = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


# Create your models here.
