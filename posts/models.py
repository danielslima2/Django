from django.db import models
from usuario.models import User

class Posts(models.Model):
    autor = models.ForeignKey(User,on_delete= models.CASCADE, verbose_name='autor')        
    text = models.TextField(unique=False)
    date = models.DateTimeField(auto_now_add=True)
    def myMethod(self, num):
        return num+3
    def __str__(self):
        return f'Autor: {self.autor} | {self.myMethod(10)}| Data: {self.date}'

class Meta:
    verbose_name_plural='Posts'