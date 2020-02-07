from django.db import models
from usuario.models import User

class Posts(models.Model):
    autor = models.ForeignKey(User,on_delete= models.CASCADE, verbose_name='autor')        
    text = models.TextField(unique=False)
    date = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='posts/' )

    

    def __str__(self):
        return f'Autor: {self.autor} | Data: {self.date} | id: {self.id}'

