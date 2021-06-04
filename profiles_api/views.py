from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ Test Api View """

    def get(self, request, format=None):
        """RETURNS A LIST OF APIView features"""
        an_apiview = [
            'use HTTP metohods as function (get, post, path , etc...)',
            'Is similar to a tradicional Django View',
            'Gives you the most contorl over the app logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})