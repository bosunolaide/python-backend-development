from rest_framework import serializers
from links.models import Link

class LinkSerializer(serializers.ModelSerializer):
    model = Link
    fields = "__all__"