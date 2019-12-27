import json
import os

from rest_framework.response import Response
from rest_framework.views import APIView

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class DbVersionView(APIView):
    def get(self, request):
        with open(f'{BASE_DIR}./five_hundred_eng/db_version') as f:
            db_version = f.readline()
        return Response(data=db_version)


class ContentsView(APIView):
    def get(self, request):
        with open(f'{BASE_DIR}./five_hundred_eng/content.json', encoding='utf-8') as f:
            contents = f.read()
        return Response(data=json.loads(contents))
