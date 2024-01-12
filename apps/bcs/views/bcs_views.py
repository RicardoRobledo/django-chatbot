#from asgiref.sync import sync_to_async

from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..repositories.bcs_repository import BCSRepository


__author__ = 'Ricardo'
__version__ = '0.1'


#@sync_to_async
@api_view(['GET'])
def get_bcs_list_procedures(request):

    bsc_repository = BCSRepository()
    data = bsc_repository.get_bcs_list_procedures()

    return Response(data)
