from .menti_choice import MentiChoice
from .menti_hundred_points import MentiHundredPoints
from .menti_multi_word import MentiMulitWord
from .menti_text import MentiText
from .menti_two_dimensions import MentiTwoDimensions
from .menti_valid_choice import MentiValidChoice

QUESTION_TYPE = {
    MentiChoice: frozenset(["choices", "choices_images", "scales", "winner"]),
    MentiHundredPoints: frozenset(["prioritisation"]),
    MentiMulitWord: frozenset(["wordcloud"]),
    MentiText: frozenset(["open"]),
    MentiTwoDimensions: frozenset(["rating"]),
    MentiValidChoice: frozenset(["quiz"])
}

def get_question(params):
    question_type = params.get("type")
    for k, v in QUESTION_TYPE.items():
        if question_type in v:
            return k(params)
    return None

__all__ = ["get_question"]
