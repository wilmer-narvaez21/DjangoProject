##estos importe es de a libreria de python estandar de datetime 
#para manejar la sona horaria
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
#creacion de los modelos para la base de datos SQLite(prueba)

#los modelos y los datos publicos(preguntas)
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
   #este metodo es para representar el objeto que se usan en todo sitio administrativo generado por Django
    def __str__(self):
        return self.question_text
    #se agrega el nuevo metodo de la zona horaria
    #fue publicado resientemente
    def was_published_reciently(self):
        return self.pub_date >= timezone.now() -  datetime.timedelta(days=1)

#las elecciones del modelo
class Choice(models.Model):
    question = models.ForeignKey(Question, 
    on_delete = models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text