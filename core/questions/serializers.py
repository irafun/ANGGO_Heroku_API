#rest framework
from rest_framework import *
from rest_framework.serializers import *

#local
from core.models import *

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"
        read_only_fields = ['createdDate','lastModifiedDate','isDelete']