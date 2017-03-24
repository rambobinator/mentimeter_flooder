from .base_menti_question import BaseMentiQuestion

class MentiValidChoice(BaseMentiQuestion):

	needed_attr = ["choices", "countdown_to_vote"]

	def __init__(self, params=None):
		super().__init__(params)

	def get_correct_answer(self):
		for choice in self.choices:
			if choice.get("correct_answer"):
				return choice
		return None

	def flood(self):
		correct_choice = self.get_correct_answer()
		if correct_choice is not None:
			return correct_choice.get("id")
		return None

__all__ = ["MentiValidChoice"]
