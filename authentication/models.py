from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=20)
    abrev = models.CharField(max_length=5) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    

class Department(models.Model):
    name = models.CharField(max_length=20)
    abrev = models.CharField(max_length=5) 
    id_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="departments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at =models.DateTimeField(null=True, blank = True)
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=255)
    abrev = models.CharField(max_length=20)
    id_department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="cities")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20, blank=True)
    mobilephone = models.CharField(max_length=20)
    address = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=20)
    password = models.TextField()
    id_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="users")
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at =models.DateTimeField(null=True, blank = True)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
