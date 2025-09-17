from django.db import models

# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20, blank=True)
    mobilephone = models.CharField(max_length=20)
    address = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=20)
    password = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at =models.DateTimeField(null=True, blank = True)

class Department(models.Model):
    name = models.CharField(max_length=20)
    abrev = models.CharField(max_length=5) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at =models.DateTimeField(null=True, blank = True)

class City(models.Model):
    name = models.CharField(max_length=255)
    abrev = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Country(models.Model):
    name = models.CharField(max_length=20)
    abrev = models.CharField(max_length=5) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
User.add_to_class(
    'city',
    models.ForeignKey("City", on_delete=models.CASCADE, related_name="users", null=True, blank=True)
)

City.add_to_class(
    'department',
    models.ForeignKey("Department", on_delete=models.CASCADE, related_name="cities", null=True, blank=True)
)

Department.add_to_class(
    'country',
    models.ForeignKey("Country", on_delete=models.CASCADE, related_name="departments", null=True, blank=True)
)