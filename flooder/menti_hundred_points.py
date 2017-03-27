from random import choice

from .base_menti_question import BaseMentiQuestion

class MentiHundredPoints(BaseMentiQuestion):

    needed_attr = ["choices"]
    max_value = 100
    step_value = 10

    def __init__(self, params=None):
        super().__init__(params)

    def flood(self):
        return {choice(self.choices).get("id"): self.max_value}

__all__ = ["MentiHundredPoints"]
