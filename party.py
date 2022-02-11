from collections import Counter


# This class represents a party of users (Profiles)
class Party:
    # List of users in the party
    # party_members = []

    def __init__(self, host):
        self.host = host
        self.party_members = [host]

    def distribute_quiz(self, quiz) -> dict[str:list]:
        """
        Allow each user in the party to take the quiz and then return the quiz with each users's answers.
        :param quiz: Quiz with prompts to determine which restaurant to suggest.
        :return: Final decisions for each prompt.
        """
        # {prompt: [answers]}
        group_answers = {}

        for profile in self.party_members:
            profile_answers = profile.take_quiz(quiz)
            if not group_answers:
                group_answers.update(profile_answers)
            else:
                for prompt in profile_answers:
                    for answer in profile_answers[prompt]:
                        group_answers[prompt].append(answer)

        return quiz.calculate(group_answers)

    '''
    def items_in_common(self, group_answers, quiz):
        """
        Splits up all answers by prompt and counts the occurrence of each answer for each prompt.
        :param group_answers: Dictionary with each users' answers
        :param quiz: Quiz that was given to the party
        :return: Nested dictionary with the counts of each answer for each prompt from all users -
                    {prompt: {answer: count}}
        """
        prompts = [*quiz.prompts_choices]

        prompt1_answers = []
        prompt2_answers = []
        prompt3_answers = []

        # Counter to keep track of which prompt the loop is on.
        # Should be okay to be hardcoded because we'll have a fixed number of prompts
        # If needs to be dynamic we could definitely find a way eventually...
        counter = 1
        # Gather the lists of answers for each prompt
        for user in group_answers:
            for prompt in group_answers[user]:
                for answer in group_answers[user][prompt]:
                    if counter == 1:
                        prompt1_answers.append(answer)
                    elif counter == 2:
                        prompt2_answers.append(answer)
                    else:
                        prompt3_answers.append(answer)
                counter += 1
            counter = 1

        # Create a dictionary for each prompt that shows the counts for each answer
        prompt1_answer_cnt = dict(Counter(prompt1_answers).items())
        prompt2_answer_cnt = dict(Counter(prompt2_answers).items())
        prompt3_answer_cnt = dict(Counter(prompt3_answers).items())

        # Combine into one nested dictionary - {prompt: {answer: count}}
        prompts_dict = {prompts[0]: prompt1_answer_cnt, prompts[1]: prompt2_answer_cnt, prompts[2]: prompt3_answer_cnt}

        return prompts_dict

    def find_max_items(self, prompts_dict):
        """
        :param prompts_dict: Dictionary with the counts of each answer to each prompt
        :return: dictionary with the prompts as the keys and
                the maximum number of occurrences for that prompt as the values
        """
        max_answer_count = 0
        prompts_max_answer = {}
        # Get the maximum answer count for each prompt
        for prompt in prompts_dict:
            for answer in prompts_dict[prompt]:
                if prompts_dict[prompt][answer] > max_answer_count:
                    max_answer_count = prompts_dict[prompt][answer]
            # {prompt: max_answer_count}
            prompts_max_answer[prompt] = max_answer_count
            max_answer_count = 0

        return prompts_max_answer

    def find_favorite_items(self, prompts_dict, prompts_max_answer, quiz):
        """
        :param prompts_dict: Dictionary from items_in_common() function
        :param prompts_max_answer: dictionary of the maximum number of occurrences
        of an answer for each prompt from find_max_items() function
        :param quiz: Quiz that was given to the party
        :return: Dictionary with prompts as the keys and the decisions for each prompt as the values
        """
        total_prompt_decisions = {}
        prompt1_decisions = []
        prompt2_decisions = []
        prompt3_decisions = []

        prompts = [*quiz.prompts_choices]

        # Counter to keep track of prompt
        counter = 1
        for prompt in prompts_dict:
            for answer in prompts_dict[prompt]:
                if prompts_dict[prompt][answer] == prompts_max_answer[prompt]:
                    if counter == 1:
                        prompt1_decisions.append(answer)
                    elif counter == 2:
                        prompt2_decisions.append(answer)
                    else:
                        prompt3_decisions.append(answer)
            counter += 1

        total_prompt_decisions[prompts[0]] = prompt1_decisions
        total_prompt_decisions[prompts[1]] = prompt2_decisions
        total_prompt_decisions[prompts[2]] = prompt3_decisions

        return total_prompt_decisions
    '''