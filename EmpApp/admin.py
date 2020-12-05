from django.contrib import admin
from . models import registerData,projectData,adminData
# Register your models here.
admin.site.register(registerData)
admin.site.register(projectData)
admin.site.register(adminData)


