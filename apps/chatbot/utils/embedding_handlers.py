from ...chatbot.openai_singleton import OpenAISingleton


__author__ = 'Ricardo'
__version__ = '0.1'


def generate_embeddings(texts):
    """
    This function generate embeddings throught texts

    :param texts: a list of texts
    """

    client = OpenAISingleton()
    embeddings = []

    for text in texts:

        embedding = client.create_embedding(client(), text)
        embeddings.append(embedding)
    
    return embeddings
