from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()
# Create your models here.



class Todo(models.Model):
    user=models.ForeignKey(User,related_name='todo',null=True,on_delete=models.CASCADE)
    completed=models.BooleanField(default=False)
    title=models.CharField(max_length=100, default="")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table="todo"



