from rest_framework.serializers import ModelSerializer
from .models import Todo 
class ReadTodoListSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','title','completed','created_at')
        