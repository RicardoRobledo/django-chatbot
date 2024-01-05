import pandas as pd
import requests
from bs4 import BeautifulSoup

from . import cleaners
from ...chatbot.utils import embedding_handlers


__author__ = 'Ricardo'
__version__ = '0.1'


def retrieve_a_tags():
    """
    This funcion get web 'a' tags from a web page
    """

    # getting data
    response = requests.get('https://tramites.bcs.gob.mx/servicios/')

    # getting web content
    soup = BeautifulSoup(response.text, 'html.parser')
    tags = [tag for tag in soup.body.find('div', id='primary').find_all('a')]

    return tags


def read_csv(path):
    """
    This function read a .csv file

    :param path: path to read the .csv file
    """

    existent_df = pd.read_csv(path)

    # getting tags
    tags = retrieve_a_tags()

    # cleaning data
    cleaned_tags = cleaners.clean_data(tags)
    
    # getting missing texts and creating embeddings
    missing_tags = [
        (text, href)
        for text, href in zip(cleaned_tags[0], cleaned_tags[1])
        if not text in existent_df['Texts'].values
    ]
    #embeddings = embedding_handlers.generate_embeddings([missing_tag[0] for missing_tag in missing_tags])
    print([missing_tag[0] for missing_tag in missing_tags])


def create_csv(path):
    """
    This function create a .csv file getting all data in a web page

    :param path: path to create the .csv file
    """
    
    # getting tags
    tags = retrieve_a_tags()

    # cleaning data and creating embeddings
    cleaned_tags = cleaners.clean_data(tags)
    embeddings = embedding_handlers.generate_embeddings(cleaned_tags[0])

    # append in .csv file
    df = pd.DataFrame({
        'Texts':cleaned_tags[0],
        'Hrefs':cleaned_tags[1],
        'Embeddings':embeddings
    })
    df.to_csv(path, index=False)
