from django.conf import settings
from django.http import JsonResponse

from rest_framework.views import APIView

from openai import OpenAI


class Openai(APIView):
    """
    This class use chatgpt
    """
    def post(self, request, format=None):

        client = OpenAI(
            api_key=settings.OPENAI_API_KEY,
        )
        
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={ "type": "json_object" },
            messages=[
                    {"role": "system", "content": "eres un experto en ia que contesta preguntas solo de temas relacionados a ella"},
                    {"role": "user", "content": f"{request.data['msg']} Responde con un json y que el valor tenga todo el texto"}
                ]
            )
        
        msg = chat_completion.choices[0].message.content
        return JsonResponse({'msg':msg})
