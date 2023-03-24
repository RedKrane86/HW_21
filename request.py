from extensions import InvalidRequest


class Request:
    def __init__(self, user_input: str):
        input_split = user_input.lower().split(' ')
        if len(input_split) != 7:
            raise InvalidRequest

        self.amount = int(input_split[1])
        self.product = input_split[2]
        self.store = input_split[4]
        self.shop = input_split[6]



