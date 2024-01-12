import json

from ..desing_patterns.creational_patterns.singleton.openai_singleton import OpenAISingleton 


__author__ = 'Ricardo'
__version__ = '0.1'


class OpenAIRepository():
    """
    This class send the data to the client
    """

    def post_user_message(self, array_chat_json, thread):
        
        # sending message
        OpenAISingleton.add_message(array_chat_json, thread)
    

    def post_retrieve_message(self, thread):

        OpenAISingleton.run_thread(thread)

        return OpenAISingleton.retrieve_message(thread)
    

    def post_create_thread(self):

        return OpenAISingleton.create_conversation_thread()
