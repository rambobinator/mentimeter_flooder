from random import choice

from .base_menti_question import BaseMentiQuestion

class MentiChoice(BaseMentiQuestion):

    needed_attr = ["choices"]

    def __init__(self, params=None):
        super().__init__(params)

    def flood(self):
        return choice(self.choices).get("id")

__all__ = ["MentiChoice"]
