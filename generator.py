import secrets as s


def create_pw(digits, small, big, numbers, symbols, ambiguous):
    alphabets = {}
    number_of_chosen_alphabets = 0
    s_choice_list = []

    # create lists with chars
    if small is True:
        alphabets["small"] = "abcdefghijklmnopqrstuvwxyz"
    if big is True:
        alphabets["big"] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if numbers is True:
        alphabets["numbers"] = "0123456789"
    if symbols is True:
        alphabets["symbols"] = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    if ambiguous is False:  # remove ambiguous characters (01lIO)
        if small is True:
            alphabets["small"] = "abcdefghijkmnopqrstuvwxyz"
        if big is True:
            alphabets["big"] = "ABCDEFGHJKLMNPQRSTUVWXYZ"
        if numbers is True:
            alphabets["numbers"] = "23456789"

    for key in alphabets.keys():
        s_choice_list.append(key)

    # if the number of ticked boxes > digits generate pw that does not necessarily contain at least 1 character of the ticket boxes
    if len(alphabets.keys()) > digits:
        return_value = ''.join(s.choice(alphabets[s.choice(s_choice_list)]) for i in range(digits))
    else:
        while True:
            return_value = ''.join(s.choice(alphabets[s.choice(s_choice_list)]) for i in range(digits))
            if any(char.islower() for char in return_value):
                number_of_chosen_alphabets += 1
            if any(char.isupper() for char in return_value):
                number_of_chosen_alphabets += 1
            if any(char.isdigit() for char in return_value):
                number_of_chosen_alphabets += 1
            if any(not char.islower() and not char.isupper() and not char.isdigit() for char in return_value):
                number_of_chosen_alphabets += 1

            if number_of_chosen_alphabets == len(alphabets.keys()):
                break
            number_of_chosen_alphabets = 0

    return return_value
