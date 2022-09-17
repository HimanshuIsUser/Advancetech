from django.contrib import admin
from .models import Post,Icodercomment
# Register your models here.
admin.site.register((Post,Icodercomment))