import profile
import party
import quiz


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

    q = quiz.Quiz("What's the occasion today?", 'What cuisine are you thinking for today?',
                  'How big is your party?',
                  ['Take-out', 'Dinner with friends', 'Anniversary', 'Dinner with the fam'],
                  ['Chinese', 'Mexican', 'Italian', 'Thai', 'Mediterranean', 'Middle Eastern', 'American', 'Pub Grub'],
                  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    party_answers = lit_squad.distribute_quiz(q)
    common_answers = lit_squad.items_in_common(party_answers, q)
    max_answer = lit_squad.find_max_items(common_answers)
    preferred_answer = lit_squad.find_favorite_items(common_answers, max_answer, q)
    prompts = [*preferred_answer]

    print(f'The occasion today is {preferred_answer[prompts[0]]}')
    print(f'The cuisine for today will be {preferred_answer[prompts[1]]}')
    print(f'There will be {preferred_answer[prompts[2]]} guests')


if __name__ == '__main__':
    main()
