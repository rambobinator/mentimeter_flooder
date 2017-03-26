from json import loads
from random import choice

from .base_menti_question import BaseMentiQuestion

QUOTES_PATH = 'quotes.json'

def get_quotes(filename=QUOTES_PATH):
    with open(filename) as f:
        return f.read()
    return ''

class MentiText(BaseMentiQuestion):

    max_text_len = 140
    needed_attr = []

    def __init__(self, params=None):
        super().__init__(params)
        self.dictionary = loads(get_quotes())

    def flood(self):
        quote = choice(self.dictionary)
        response = "{}: \"{}\"".format(quote.get("name", ''),
                                        quote.get("quote", ''))
        return response[:self.max_text_len]
