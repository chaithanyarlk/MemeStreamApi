from core.models import MemeModel
from rest_framework import serializers

class MemeSerializer (serializers.ModelSerializer):
     class Meta:
          model = MemeModel
          fields = ['id','name','url','caption','timestamp']
class CreateMemeSerializer (serializers.ModelSerializer):
     class Meta:
          model = MemeModel
          fields = ['id']