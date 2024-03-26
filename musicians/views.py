from rest_framework.views import APIView, Response, Request, status
from musicians.models import Musician
from django.forms.models import model_to_dict
from django.http import Http404
from .serializers import MusicianSerializer
from rest_framework.pagination import PageNumberPagination


class MusicianView(APIView, PageNumberPagination):
    def post(self, request):
        serializer = MusicianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request: Request):
        musicians = Musician.objects.all()
        result_page = self.paginate_queryset(musicians, request, view=self)
        serializer = MusicianSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

class MusicianDetailView(APIView):
    def get_object(self, pk):
        try:
            return Musician.objects.get(pk=pk)
        except Musician.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        musician = self.get_object(pk)
        return Response(model_to_dict(musician))