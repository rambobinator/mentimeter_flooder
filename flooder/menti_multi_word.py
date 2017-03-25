from random import sample

from .base_menti_question import BaseMentiQuestion

DICT_PATH = "/usr/share/dict/words"

def get_dict(filename=DICT_PATH):
    with open(filename) as f:
        return list(f)
    return []

class MentiMulitWord(BaseMentiQuestion):

    needed_attr = ["max_nb_words"]
    max_char_per_word = 24

    def __init__(self, params=None):
        super().__init__(params)
        self.dictionary = get_dict()

    def flood(self):
        return ' '.join(sample(self.dictionary, self.max_nb_words))

__all__ = ["MentiMulitWord"]
