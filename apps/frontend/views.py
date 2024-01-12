from django.views import View
from django.shortcuts import render


__author__ = 'Ricardo'
__version__ = '0.1'


class IndexView(View):

    def get(self, request, *args, **kwargs):
        """
        This method return our chatbot view
        """
        
        response = render(request, 'frontend/index.html')

        return response
