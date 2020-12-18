from rest_framework import serializers
from models import Cars

class carSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Cars
        fields=('id','carbrand','cartype','avilable')