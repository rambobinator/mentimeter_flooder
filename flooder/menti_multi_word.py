from .base_menti_question import BaseMentiQuestion

class MentiMulitWord(BaseMentiQuestion):

    needed_attr = ["max_nb_words"]
    max_char_per_word = 24

    def __init__(self, params=None):
        super().__init__(params)

    def flood(self):
        return "1 2 3"

__all__ = ["MentiMulitWord"]
