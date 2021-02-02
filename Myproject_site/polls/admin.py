from django.contrib import admin
from .models import Question
# Register your models here.
#las preguntas tienen que ser desde la interfaz de admin,
admin.site.register(Question)