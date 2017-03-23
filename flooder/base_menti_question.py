class BaseMentiQuestion:

    basic_attr = ["active", "id", "slug", "type"]

    def __init__(self, params):
        try:
            required_attr = self.basic_attr + self.needed_attr
        except AttributeError:
            raise NotImplementedError
        for attr in required_attr:
            self.__dict__[attr] = params.get(attr)

    def flood(self):
        raise NotImplementedError

    @property
    def response(self):
        return {"question": self.id,
                "question_type": self.type,
                "vote": self.flood()}

__all__ = ["BaseMentiQuestion"]
