from collections import Counter


# This class represents a party of users (Profiles)
class Party:
    # List of users in the party
    # party_members = []

    def __init__(self, host):
        self.host = host
        self.party_members = [host]

    def distribute_quiz(self, quiz):
        """
        Allow each user in the party to take the quiz and then return the quiz with each user's answers.
        :param quiz: Quiz with questions to determine which restaurant to suggest.
        :return: Quiz dictionary with the answers from each user.
        """
        group_answers = {}

        for user in self.party_members:
            user_answers = user.take_quiz(quiz)
            group_answers.update(user_answers)

        return group_answers

    def items_in_common(self, group_answers):
        """
        :param group_answers: Dictionary with each users' answers
        :return: Dictionary with the counts of each answer from all users
        """
        full_items_list = []
        for user in group_answers:
            for item in group_answers[user]:
                full_items_list.append(item)

        items_count_dict = dict(Counter(full_items_list).items())

        return items_count_dict

    def find_max_items(self, items_dict):
        """
        :param items_dict: Dictionary with the counts of each answer
        :return: integer of the maximum number of occurrences of an answer
        """
        max_item_count = 0

        for item in items_dict:
            if items_dict[item] > max_item_count:
                max_item_count = items_dict[item]

        return max_item_count

    def find_favorite_items(self, items_dict, max_item):
        """
        :param items_dict: Dictionary from items_in_common() function
        :param max_item: integer of the maximum number of occurrences
        of an item from find_max_items() function
        :return: List of most preferred items
        """
        most_common_items = []
        for item in items_dict:
            if items_dict[item] == max_item:
                most_common_items.append(item)

        return most_common_items
