from rest_framework import serializers
from .models import Document


class DocumentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields =['file', 'uploaded_at']