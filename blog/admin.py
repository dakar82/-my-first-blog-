from django.contrib import admin
from .models import Post #имопрт модели(класса) созданой мной ранее
# Register your models here.
admin.site.register(Post) #обязательная регистрация класса