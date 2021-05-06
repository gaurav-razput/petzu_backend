from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

@api_view(['GET'])
def index(request):
    date = datetime.now().strftime('%d/%m/%y %H:%M:%S')
    massage = 'Server ie live current time is: '
    return Response(data=massage+date,status=status.HTTP_200_OK)