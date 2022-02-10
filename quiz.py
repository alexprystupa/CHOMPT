# This class represents a quiz of prompts that will be given to each user in order to reach a restaurant decision.
# STORE THE NUMBER OF OCCURRENCES FOR EACH ANSWER IN HEREEEEEEE
class Quiz:
    def __init__(self, p1, p2, p3, c1, c2, c3):
        self.prompts_choices = {p1: c1, p2: c2, p3: c3}