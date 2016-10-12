from django.contrib import admin
from .models import Credentials , Subject , Assignment, Notes

# Register your models here.
admin.site.register(Credentials)
admin.site.register(Subject)
admin.site.register(Assignment)
admin.site.register(Notes)