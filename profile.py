# Each Profile class instance represents an individual user. Must create a Profile in order to use the app.
class Profile:
    # Friends list
    friends = []

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
        Take in a quiz as a list of questions and allow the user to answer the questions.
        *** Will have to modify the return dictionary to allow for multiple questions. ***
        *** Nested dictionary probably: {user: {question: answer}} ***
        :param quiz: list of questions for the user to answer.
        :return: dictionary with the user as the key and answers as the values.
        """
        user_answers = {}

        answers = input(quiz[0])
        list_of_answers = answers.split()
        user_answers[self] = list_of_answers

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
