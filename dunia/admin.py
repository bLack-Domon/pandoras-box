from django.contrib import admin
from .models import *  # Ganti dengan nama model Anda

# Register your models here.
admin.site.register(Profile)
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(Testimoni)
admin.site.register(Contact)
