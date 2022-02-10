from datetime import date


# Each Profile class instance represents an individual user. Must create a Profile in order to use the app.
class Profile:
    # Friends list
    friends = []
    # To keep records of answers from all previous quizzes this user has taken
    old_quizzes = {}

    # Required fields to create a Profile (so far, update as needed. Think sign-up screen):
    #   - First name
    #   - Last name
    #   - Email Address
    #   - Phone Number
    #   - Birthday
    def __init__(self, first_name, last_name, email_address, phone_number, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.phone_number = phone_number
        self.birthday = birthday

    def take_quiz(self, quiz):
        """
        Take in a Quiz object and allow the user to answer the prompts with the given choices.
        *** Will have to modify the return dictionary to allow for multiple prompts. ***
        *** Nested dictionary probably: {user: {prompt: answer}} ***
        :param quiz: list of prompts for the user to answer.
        :return: Nested dictionary - {user: {prompt: answer}}
        """
        user_answers = {}
        p_c = quiz.prompts_choices

        # initialize empty dict in order to just be able to update later.
        # user_answers[self] = {}
        self.old_quizzes[date.today()] = {}
        for key in p_c:
            # Print the prompt
            print(key)
            # Print the choices
            print(p_c[key])
            answers = input('Type in your choices separating each choice by a single space: ')
            list_of_answers = answers.split()
            # user_answers[self].update({key: list_of_answers})
            user_answers.update({key: list_of_answers})
            # Record this quiz
            self.old_quizzes[date.today()].update({key: list_of_answers})

        return user_answers

    def send_invite(self, profile, party):
        """
        Send another user an invite to join your party.
        If the invitee accepts, his Profile object is returned to the caller to be added to the party.
        Once in a party, each member can submit their own answers to the quiz
        and receive a group restaurant suggestion based on all of their answers.
        :param profile: Profile of the intended invitee
        :param party: Host's Party that the invitee will be added to
        :return: profile: Profile of the invitee if he/she accepted
        """
        pass

    def __str__(self):
        return self.first_name + ' ' + self.last_name
