from django.conf import settings
from django.http import StreamingHttpResponse
import json

from rest_framework.views import APIView

from openai import OpenAI


class Openai(APIView):
    """
    This class use chatgpt
    """
    def post(self, request, format=None):

        '''client = OpenAI(
            api_key=settings.OPENAI_API_KEY,
        )

        x = [x for x in request.FILES.getlist('file')]

        with x[0].open('rb') as f:
            
            f = client.files.create(
                file=f.read(),
                purpose="assistants"
            )
            print(f)
        
        
        assistant = client.beta.assistants.create(
            instructions="You are a customer support chatbot. Use your knowledge base to best respond to customer queries.",
            model="gpt-4-1106-preview",
            tools=[{"type": "retrieval"}],
            file_ids=['asst_iFQFvMUjdRfWxnd1uGmvn256']
        )

        print(assistant)'''

        # file-hZlBEnJ27XT498PDOgIeX4UW
        # thread_2wghxgEOpoVNZBpjJyawf63B
        
        #thread = client.beta.threads.create()
        #print(thread)
        
        '''
        thread_messages = client.beta.threads.messages.list("thread_elVhilWVysWxFVDVlADwiiLP")
        print(thread_messages.data)

        run = client.beta.threads.create_and_run(
            assistant_id="asst_PjSuAmCgYXAIIkbzuSoC0V5k",
            thread={
                "messages": [
                    {"role": "user", "content": "Hola"}
                ]
            }
        )
        print(run)'''

        #print(client.files.list())

        '''
        msg = client.beta.threads.messages.create(
            thread_id="thread_2wghxgEOpoVNZBpjJyawf63B",
            role="user",
            content="Que es un modelo de lenguaje en una línea",
            file_ids=['file-hZlBEnJ27XT498PDOgIeX4UW']
        )

        print('--------------------')
        print(msg)
        
        run = client.beta.threads.runs.create(
            thread_id='thread_2wghxgEOpoVNZBpjJyawf63B',
            assistant_id='asst_iFQFvMUjdRfWxnd1uGmvn256'
        )

        print(run)
        print()
        
        runs = client.beta.threads.messages.list(
            thread_id="thread_2wghxgEOpoVNZBpjJyawf63B"
        )

        print('--------------------')
        
        for i in runs:
            print(i)
            print()
        '''

        #response = client.beta.threads.delete("thread_VSmPqANN0bxDqvmbA74HOsHv")
        #print(response)
        
        #asst_iFQFvMUjdRfWxnd1uGmvn256
        #print(messages)
        
        #print(client.files.list())

        '''f1 = client.files.create(
            file=uploaded_file,
            purpose="message"
        )'''

        query_dict = request.data
        array_chat_str = query_dict.get('array_chat', '')
        array_chat_json = json.loads(array_chat_str)

        client = OpenAI(
            api_key=settings.OPENAI_API_KEY,
        )
        
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": "eres un experto conversador de ia que solo responde cosas relacionadas sobre ia"},
                {"role": "user", "content": f"{array_chat_json['content']}. Responde con un json y que el valor tenga todo el texto"}
            ],
            stream=True
        )

        def generate_content():
            for chunk in chat_completion:
                if chunk.choices[0].delta.content is not None:
                    #print(chunk.choices[0].delta.content)
                    yield chunk.choices[0].delta.content

        response = StreamingHttpResponse(generate_content(), content_type="text/plain")
        response['Cache-Control'] = 'no-cache'
        response['Content-Disposition'] = 'inline; filename="stream_data.json"'
        #return JsonResponse({'msg':msg})
        return response
