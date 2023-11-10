import os
import asyncio
import asyncpg
from django.db import connection
from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework import status
from .serializers import DocumentSerializers
from .services import DocumentService
from django.conf import settings

class DocumentUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    async def post(self, request, *args, **kwargs):
        file_serializer = DocumentSerializers(data=request.data)

        if file_serializer.is_valid():
            document, file_path = DocumentService.upload_document(request.data['file'])

            await self.call_stored_procedure(file_path)

            return JsonResponse(DocumentSerializers(document).data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

    async def call_stored_procedure(self, file_path):
        """Use an asynchronous connection to the database"""
        
        async with asyncpg.create_pool(
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            database=settings.DATABASES['default']['NAME'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        ) as pool:
            async with pool.acquire() as connection:
                async with connection.transaction():
                    # print(settings.DATABASES['default']['PORT'])
                    await connection.execute(
                        "SELECT public.sample_upload_file($1)",
                        file_path,
                    )
