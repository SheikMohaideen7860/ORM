from django.db import models
from django.contrib import admin
class bike_service(models.Model):
    bike_No=models.CharField(max_length=10)
    name=models.CharField(max_length=20)
    phone_no=models.IntegerField()
    address=models.CharField(max_length=30)
    bike_model=models.CharField(max_length=20)
    feedback=models.TextField()
    licence=models.CharField(max_length=20,primary_key=True)
class bike_serviceAdmin(admin.ModelAdmin):
    list_display=["bike_No","name","phone_no","address","bike_model","feedback","licence"]