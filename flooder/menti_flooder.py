import json
import requests as rqst

from .menti_questions import get_question

API_URL = "https://www.menti.com/api/"

class MentiFlooder:

    def __init__(self, vote_id):
        _ = int(vote_id) # check is_digit or raise ValueError
        self.vote_id = vote_id
        self.questions = None

    @property
    def identifier(self):
        return next(self.get_new_identifier())

    def get_new_identifier(self):
        url = "{}{}".format(API_URL, "identifier")
        r = rqst.post(url)
        if r.status_code == rqst.codes.ok:
            yield r.json().get("identifier")
        yield None

    def retrieve_questions(self):
        url = "{}{}{}".format(API_URL, "objects/vote_ids/" ,self.vote_id)
        r = rqst.get(url)
        if r.status_code == rqst.codes.ok:
            self.questions = [get_question(params)
                for params in r.json().get("questions", [])]
        else:
            self.questions = []

    def send_response(self, question):
        response = question.response
        data = json.dumps(response)
        headers = { "content-type": "application/json",
                    "x-identifier": self.identifier}
        url = "{}{}".format(API_URL, "vote")
        r = rqst.post(url=url, data=data, headers=headers)
        print("[{}] {} -> {}".format(r.status_code,
                                    question.type,
                                    response.get("vote")))

    def send_responses(self):
        for question in self.questions:
            self.send_response(question)

__all__ = ["MentiFlooder"]
