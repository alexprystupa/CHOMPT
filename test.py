import profile
import party


def main():
    """
    Testing with a 1-question quiz and a party of users.
    :return: Asks each user what food items they want for dinner and outputs the most common response
    """
    arthur = profile.Profile('Arthur', 'Xiao', 'axiao72', '908', '02/11/1999')
    alex = profile.Profile('Alex', 'Prystupa', 'alexp987', '908', '08/25/1999')
    aedan = profile.Profile('Aedan', 'Collins', 'aed23867', '908', '01/31/1999')

    lit_squad = party.Party(arthur)
    lit_squad.party_members.append(alex)
    lit_squad.party_members.append(aedan)

    quiz = ['What food items would you want for dinner?: ']

    party_answers = lit_squad.distribute_quiz(quiz)
    common_answers = lit_squad.items_in_common(party_answers)
    max_answer = lit_squad.find_max_items(common_answers)
    preferred_answer = lit_squad.find_favorite_items(common_answers, max_answer)

    print(f'The food everyone wants is {preferred_answer}')


if __name__ == '__main__':
    main()
