from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import AccountSerializer

from .models import Account


class AccountFindView(APIView):
    def get(self, request):
        sex = request.query_params.get("sex", None)
        name = request.query_params.get("name", None)

        accounts = Account.objects.filter(
            sex=sex, name=name
        )

        serializer = AccountSerializer(accounts, many=True)

        return Response(serializer.data)