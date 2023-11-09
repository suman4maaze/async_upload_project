import asyncio
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Document
from .serializers import DocumentSerializers
from .services import DocumentService
# Create your views here.

class DocumentUploadView(generics.GenericAPIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = DocumentSerializers

    async def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        loop = asyncio.get_event_loop()
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status= status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

