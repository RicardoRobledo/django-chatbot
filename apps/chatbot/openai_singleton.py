from django.conf import settings

from openai import OpenAI


__author__ = 'Ricardo'
__version__ = '0.1'


class OpenAISingleton():


    __client = None


    def __get_connection(self):
        
        client = OpenAI(api_key=settings.OPENAI_API_KEY,)
        return client


    def __call__(cls, *args, **kwargs):
        
        if cls.__client==None:
            cls.__client = cls.__get_connection()
        
        return cls.__client


    @classmethod
    def create_embedding(cls, client, text):

        response = client.embeddings.create(
            input=text,
            model=settings.EMBEDDINGS_MODEL
        )

        return response.data[0].embedding
