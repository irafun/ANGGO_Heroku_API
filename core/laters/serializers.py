#rest framework
from rest_framework import *
from rest_framework.serializers import *

#local
from core.models import *

class LaterSerializer(ModelSerializer):
    class Meta:
        model = Later
        fields = "__all__"
        read_only_fields = ['createdDate','lastModifiedDate','isDelete']