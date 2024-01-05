import re


__author__ = 'Ricardo'
__version__ = '0.1'


def clean_data(tags):
    """
    clean data to save in a .csv file

    :param tags: a list of 'a' tags
    :return: a tuple with separated texts, urls and embeddings
    """

    #client = OpenAISingleton()
    texts = []
    hrefs = []
    #embeddings = []

    for tag in tags:

        # cleaning text
        text = re.sub(r'[^áéíóúña-zA-Z0-9 ]', '', tag.text.lower())

        # cleaning hrefs
        href = re.sub(re.compile(r'"'), '', tag['href'])

        if(href[0]=='/'):
            href = f'https://tramites.bcs.gob.mx{href}'

        # creating embedding
        #embedding = client.create_embedding(client(), text)

        # adding results in lists
        texts.append(text)
        hrefs.append(href)
        #embeddings.append(embedding)
    
    return (texts, hrefs)
