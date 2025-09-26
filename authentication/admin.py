from django.contrib import admin
from .models import Country, Department, City, User
# Register your models here.
admin.site.register(Country)
admin.site.register(Department)
admin.site.register(City)
admin.site.register(User)