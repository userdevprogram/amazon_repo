from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField(max_length=64)
    group_core = models.BooleanField(default=False)
    group_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField(max_length=256)
    group_core = models.BooleanField(default=False)
    category_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    group_id = models.ForeignKey(Group, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.name


class List(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField(max_length=1024)
    group_core = models.BooleanField(default=False)
    category_id = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.name