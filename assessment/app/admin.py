from django.contrib import admin

# here we can import our models of the database
from .models import User, Order, Payment


# Register your models here.
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Payment)
