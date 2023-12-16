from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response

from openai import OpenAI


class Openai(APIView):
    """
    This class use chatgpt

    :param : list
    """
    def get(self, request, format=None):

        client = OpenAI(
            api_key=settings.OPENAI_API_KEY,
        )
        
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={ "type": "json_object" },
            messages=[
                    {"role": "system", "content": "eres un experto en ia que contesta preguntas solo de temas relacionados a ella"},
                    {"role": "user", "content": f"{request.GET['msg']} Responde con un json y que el valor tenga todo el texto"}
                ]
            )
        
        msg = chat_completion.choices[0].message.content
        return Response(msg)
