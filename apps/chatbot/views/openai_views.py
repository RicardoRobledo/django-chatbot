from django.conf import settings
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..repositories.openai_repository import OpenAIRepository
from ..desing_patterns.creational_patterns.singleton.openai_singleton import OpenAISingleton
from ...bcs.utils.web_scrappers.scrapper import BCSScrapper
#from ..desing_patterns.behavioral_design_patterns.state.conversation_flow import ConversationFlow


@api_view(['POST'])
def post_message(request):
    """
    This view post a message
    """

    # getting request data
    query_dict = request.data
    array_chat_str = query_dict.get('array_chat', '')
    thread_id = query_dict.get('thread_id', '')

    # become in json
    # {
    #    'role': 'user',
    #    'content': 'abc...'
    # }
    array_chat_json = json.loads(array_chat_str)
    template_procedure = BCSScrapper().get_bcs_procedure(request.data.get('index'))

    # linking user message with procedure content
    array_chat_json['content'] = f"{template_procedure}\n//duda\n{array_chat_json['content']}"

    # making conversation flow
    #conversation_flow = ConversationFlow()
    #conversation_flow.send_message(array_chat_json, thread_id)
    
    OpenAISingleton()
    openai_repository = OpenAIRepository()
    openai_repository.post_user_message(array_chat_json, thread_id)
    msg = openai_repository.post_retrieve_message(thread_id)

    return Response({'msg':msg})


@api_view(['POST'])
def post_clean(request):
    """
    This view close our connection
    """

    OpenAISingleton.close_connection(request.data.get('thread_id'))

    return Response({})


@api_view(['POST'])
def post_create_thread(request):
    """
    This view create a thread
    """

    OpenAISingleton()
    thread = OpenAIRepository().post_create_thread()

    return Response({'thread_id':thread.id})
