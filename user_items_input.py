#!/usr/bin/env python3
# user_food_input.py
"""
This script was made to take user input from any number of users and
find the consensus of what they want. This should be able to include any
category, and you can enter multiple items, such as multiple food choices etc.
"""

from collections import Counter


def user_input():
    """
    :return: Dictionary with keys as users & values as their input
    """
    num_guests = int(input('How many guests do you have: '))

    user_dict = dict()
    for i in range(1, num_guests + 1):
        items = input(f'What items do you want user {i}: ')
        list_of_items = items.split()
        user_dict[f'user_{i}'] = list_of_items

    return user_dict


def items_in_common(user_items_dict):
    """
    :param user_food_dict: Dictionary from user_input() function
    :return: Dictionary with the counts of each item from all users
    """
    full_items_list = []
    for user in user_items_dict:
        for item in user_items_dict[user]:
            full_items_list.append(item)

    items_count_dict = dict(Counter(full_items_list).items())

    return items_count_dict


def find_max_items(items_dict):
    """
    :param items_dict: Dictionary from items_in_common() function
    :return: integer of the maximum number of occurrences of an item
    """
    max_item_count = 0

    for item in items_dict:
        if items_dict[item] > max_item_count:
            max_item_count = items_dict[item]

    return max_item_count


def find_favorite_items(items_dict, max_item):
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


def main():
    """
    :return: Takes in user input & outputs what the users overall preferences are from the group
    """
    user_items = user_input()
    common_items = items_in_common(user_items)
    max_item = find_max_items(common_items)
    preferred_item = find_favorite_items(common_items, max_item)

    print(f'The item that the majority wants is {preferred_item}')


if __name__ == '__main__':
    main()
