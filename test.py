import profile
import party
import quiz
import yelp

API_KEY = 'AQuSIIDGMQZ4l7SBHegjnoggcHOoh_mImR8Zatvg0a14fXNo1BK3mhKnPGK9t0wc-' \
          '4fIZIJA7A_D6AQ-YddfqffCSpQ0Pbus-iXJeQ9x8H3ehGf49RD_sFAiM3f9YXYx'

ENDPOINT = 'https://api.yelp.com/v3/businesses/search'

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

    '''
    q = quiz.Quiz("What's the occasion today?", 'What cuisine are you thinking for today?',
                  'How big is your party?',
                  ['Take-out', 'Dinner with friends', 'Anniversary', 'Dinner with the fam'],
                  ['Chinese', 'Mexican', 'Italian', 'Thai', 'Mediterranean', 'Middle Eastern', 'American', 'Pub Grub'],
                  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    '''

    q = quiz.Quiz({"Food Type?": ['Chinese', 'Mexican', 'Italian', 'Thai',
                                  'Mediterranean', 'Middle Eastern', 'American'],
                   'Distance (miles)?': ['1-5'],
                   'Location?': ['Enter city name'],
                   'Price?': ['1-4']})

    party_decisions = lit_squad.distribute_quiz(q)
    #prompts = [*party_decisions]

    lads_are_hungry = yelp.Yelp(party_data=party_decisions, api_key=API_KEY, endpoint=ENDPOINT)

    api_data = lads_are_hungry.call_api()
    lads_are_hungry.print_data(api_data)


if __name__ == '__main__':
    main()
