from collections import Counter

# This class represents a quiz of prompts that will be given to each user in order to reach a restaurant decision.
# STORE THE NUMBER OF OCCURRENCES FOR EACH ANSWER IN HEREEEEEEE
class Quiz:
    def __init__(self, prompts_choices):
        self.prompts_choices = prompts_choices

    def calculate(self, answers):
        """

        :param answers: Dictionary of all answers for each prompt - {prompt: [answers]}
        :return: Dictionary with the final decisions for each prompt.
        """
        # {prompt: {answer: count}}
        answer_counts = {}
        # Get the count of each answer for each prompt
        for prompt in answers:
            answer_counts[prompt] = dict(Counter(answers[prompt]).items())

        max_answer_count = 0
        prompts_max_answer = {}
        # Get the maximum answer count for each prompt
        for prompt in answer_counts:
            for answer in answer_counts[prompt]:
                if answer_counts[prompt][answer] > max_answer_count:
                    max_answer_count = answer_counts[prompt][answer]
            # {prompt: max_answer_count}
            prompts_max_answer[prompt] = max_answer_count
            max_answer_count = 0

        # Dictionary to hold the deciding answers for the group
        # {prompt: [answers]}
        prompt_final_dec = {}
        # Find which answers match the maximum answer count for each prompt
        # and store as the final decisions for that prompt
        for prompt in answer_counts:
            prompt_final_dec[prompt] = []
            for answer in answer_counts[prompt]:
                if answer_counts[prompt][answer] == prompts_max_answer[prompt]:
                    prompt_final_dec[prompt].append(answer)

        return prompt_final_dec
