import os
from django.conf import settings
from .models import Document


class DocumentService:
    @staticmethod
    def upload_document(file):
        document = Document.objects.create(file = file)
        file_path = os.path.join(settings.MEDIA_ROOT, str(document.file))

        return document, file_path