from django.db import models

from django.contrib.auth import get_user_model

User=get_user_model()

class Todo(models.Model):
    name=models.CharField (max_length=120,verbose_name='Название')
    description= models.CharField(max_length=120, verbose_name='описание')
    created_at=models.DateField(auto_now_add=True)
    deadline= models.DateField(verbose_name='Дата окончания')
    image=models.ImageField(
        upload_to='todo/images/',verbose_name='картинка'
    )
    user=models.ForeignKey(
        User,on_delete=models.CASCADE,
        related_name='todoes',verbose_name='Пользователь'
    )
    is_done=models.BooleanField(
        default=False,verbose_name="сделано?"

    )
    def __str__(self) -> str:
        return self.name



    
    
