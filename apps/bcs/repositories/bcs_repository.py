from ..utils.web_scrappers.scrapper import BCSScrapper


__author__ = 'Ricardo'
__version__ = '0.1'


class BCSRepository():
    """
    This class retrieve information about baja california sur's web page
    """

    def get_bcs_list_procedures(self):

        return BCSScrapper().get_bcs_list_procedures()
