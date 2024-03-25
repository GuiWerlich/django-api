from rest_framework.views import APIView, Response, Request
from musicians.models import Musician
from django.forms.models import model_to_dict
from django.http import Http404


class MusicianView(APIView):
    def post(self, request: Request) -> Response:
        musician = Musician.objects.create(**request.data) #acessando o metodo create da models para criar uma nova entidade no banco de dados.
        return Response(model_to_dict(musician), 201) #metodo quebra galho para que seja possivel renderizar a resposta da models

    def get(self, request: Request) -> Response:
        musicians = Musician.objects.all()
        musicians_dict = []

        for musician in musicians:
            musicians_dict.append(model_to_dict(musician))
        
        return Response(musicians_dict, 200)

class MusicianDetailView(APIView):
    def get_object(self, pk):
        try:
            return Musician.objects.get(pk=pk)
        except Musician.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        musician = self.get_object(pk)
        return Response(model_to_dict(musician))