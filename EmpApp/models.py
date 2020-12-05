from django.db import models

class registerData(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=12)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class projectData(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    projectName=models.CharField(max_length=100)
    projectPercenatge=models.CharField(max_length=100)
    upload =models.FileField()
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

class adminData(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=12)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.name
