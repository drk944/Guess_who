'''
Progress Notes: (aka Jira)
- [x] Create a dictionary of lists for each characteristic
- [x] Finish adding people to guess_who_classes.py
- [ ] Make a way to propose a question that equally splits the list
    - [ ] Start with simple case of gender
    - [ ] Then work on combining groups with unions and intersections
- [ ] Formulate question and enter response
- [ ] Implement cheater method done solely by alphabet
- [ ] map characteristics to questions
'''

from guess_who_classes import *
import random

characteristics = ['gender', 'skin_color', 'hair_color', 'hair_length', 'eye_color',
                   'teeth', 'earing', 'hat', 'mustache', 'beard',
                   'hairtie', 'hair_accent', 'glasses']

characteristics_types = ["male", "female", "s_white", "s_black", "s_brown", "h_white", "h_brown",
                         "h_black", "h_blonde", "h_red", "h_short", "h_long", 'h_bald', "e_green", "e_blue",
                         "e_brown", 'teeth_t', 'teeth_f', 'earing_t', 'earing_f', 'hat_t',
                         'hat_f', 'mustache_t', 'mustache_f', 'beard_t', 'beard_f',
                         'hairtie_t', 'hairtie_f', 'hair_accent_t', 'hair_accent_f',
                         'glasses_t', 'glasses_f']

attributes_to_characteristics = {'male': 'gender', 'female': 'gender', "s_white": 'skin_color', "s_black": 'skin_color', "s_brown": 'skin_color', "h_white": 'hair_color', "h_brown": 'hair_color',
                                 "h_black": 'hair_color', "h_blonde": 'hair_color', "h_red": 'hair_color', "h_short": 'hair_length', "h_long": 'hair_length', "h_bald": "hair_length", "e_green": 'eye_color', "e_blue": 'eye_color',
                                 "e_brown": 'eye_color', 'teeth_t': 'teeth', 'teeth_f': 'teeth', 'earing_t': 'earing', 'earing_f': 'earing', 'hat_t': 'hat',
                                 'hat_f': 'hat', 'mustache_t': 'mustache', 'mustache_f': 'mustache', 'beard_t': 'beard', 'beard_f': 'beard',
                                 'hairtie_t': 'hairtie', 'hairtie_f': 'hairtie', 'hair_accent_t': 'hair_accent', 'hair_accent_f': 'hair_accent',
                                 'glasses_t': 'glasses', 'glasses_f': 'glasses'}

char_dict = dict.fromkeys(characteristics_types)


def generate_dictionaries(people):
    char_dict = dict.fromkeys(characteristics_types)
    for attribute in char_dict:
        char_dict[attribute] = []
    # for i in characteristics_types:
    for j in people:
        # Gender
        if j.gender == 'male':
            char_dict['male'].append(j)
        elif j.gender == 'female':
            char_dict['female'].append(j)
        # Skin Color
        if j.skin_color == 's_white':
            char_dict['s_white'].append(j)
        elif j.skin_color == 's_brown':
            char_dict['s_brown'].append(j)
        elif j.skin_color == 's_black':
            char_dict['s_black'].append(j)
        # Hair Color
        if j.hair_color == 'h_white':
            char_dict['h_white'].append(j)
        elif j.hair_color == 'h_brown':
            char_dict['h_brown'].append(j)
        elif j.hair_color == 'h_black':
            char_dict['h_black'].append(j)
        elif j.hair_color == 'h_blonde':
            char_dict['h_blonde'].append(j)
        elif j.hair_color == 'h_red':
            char_dict['h_red'].append(j)
        # Hair Length
        if j.hair_length == 'h_short':
            char_dict['h_short'].append(j)
        elif j.hair_length == 'h_long':
            char_dict['h_long'].append(j)
        elif j.hair_length == 'h_bald':
            char_dict['h_bald'].append(j)
        # Eye Color
        if j.eye_color == 'e_green':
            char_dict['e_green'].append(j)
        elif j.eye_color == 'e_blue':
            char_dict['e_blue'].append(j)
        elif j.eye_color == 'e_brown':
            char_dict['e_brown'].append(j)
        # Teeth
        if j.teeth == 'teeth_t':
            char_dict['teeth_t'].append(j)
        elif j.teeth == 'teeth_f':
            char_dict['teeth_f'].append(j)
        # Earing
        if j.earing == 'earing_t':
            char_dict['earing_t'].append(j)
        elif j.earing == 'earing_f':
            char_dict['earing_f'].append(j)
        # Hat
        if j.hat == 'hat_t':
            char_dict['hat_t'].append(j)
        elif j.hat == 'hat_f':
            char_dict['hat_f'].append(j)
        # Mustache
        if j.mustache == 'mustache_t':
            char_dict['mustache_t'].append(j)
        elif j.mustache == 'mustache_f':
            char_dict['mustache_f'].append(j)
        # Beard
        if j.beard == 'beard_t':
            char_dict['beard_t'].append(j)
        elif j.beard == 'beard_f':
            char_dict['beard_f'].append(j)
        # Hairband
        if j.hairtie == 'hairtie_t':
            char_dict['hairtie_t'].append(j)
        elif j.hairtie == 'hairtie_f':
            char_dict['hairtie_f'].append(j)
        # Hair Accent
        if j.hair_accent == 'hair_accent_t':
            char_dict['hair_accent_t'].append(j)
        elif j.hair_accent == 'hair_accent_f':
            char_dict['hair_accent_f'].append(j)
        # Glasses
        if j.glasses == 'glasses_t':
            char_dict['glasses_t'].append(j)
        elif j.glasses == 'glasses_f':
            char_dict['glasses_f'].append(j)
    return char_dict

# Iterate through and print the names of each characteristic


def get_names_from_characteristics(char_dict):
    for key in char_dict:
        print(key)
        for i in char_dict[key]:
            print("    ", i.name)

# Iterate through and get quantiy of each characteristic


def get_quantity_from_characteristics(char_dict, num_people):
    target_split = num_people / 2
    closest_keys = []
    closest_key_value = 99
    char_split = dict.fromkeys(characteristics_types)
    for key in char_dict:
        quantity = len(char_dict[key])
        dist = abs(quantity - target_split)
        if dist < closest_key_value:
            closest_keys = [key]
            closest_key_value = dist
        elif dist == closest_key_value:
            closest_keys.append(key)
        # print(key, quantity)
        char_split[key] = quantity
    if len(closest_keys) == 1:
        return closest_keys[0]
    else:
        if 's_brown' in closest_keys:
            closest_keys.remove('s_brown')
        if len(closest_keys) > 1 and 's_black' in closest_keys:
            closest_keys.remove('s_black')

        choice = random.choice(closest_keys)
        if choice[-2:] == '_f':
            # choice[-1] = 't' # Cheap way to change the last character
            list1 = list(choice)
            list1[-1] = 't'
            choice = ''.join(list1)
        return choice

        # Need to create a map, mapping attributes to the characteristics


def clean_list(people, attribute_inquiry, attribute_response):
    characteristic = attributes_to_characteristics[attribute_inquiry]
    people_to_remove = []
    for i in people:
        if attribute_response == True:
            if getattr(i, characteristic) != attribute_inquiry:
                people_to_remove.append(i)
        else:
            if getattr(i, characteristic) == attribute_inquiry:
                people_to_remove.append(i)
    for i in people_to_remove:
        people.remove(i)
    return people


def alphabet_approach(people):
    people_names = []
    for i in people:
        people_names.append(i.name)
    people_names = sorted(people_names)
    middle_char_idx = int(len(people_names) / 2)
    middle_char = people_names[int(len(people_names) / 2)][0]
    chars_forward = 0
    chars_backward = 0
    i = middle_char_idx
    # Need to check bounds
    while people_names[i][0] == middle_char:
        chars_forward += 1
        i += 1

    while people_names[i][0] == middle_char:
        chars_backward += 1
        i -= 1
    if chars_forward > chars_backward:
        end_char = people_names[middle_char_idx + chars_forward - 1][0]
    else:
        end_char = people_names[middle_char_idx - chars_backward + 1][0]
    print("A -", end_char, 'y/n')
    response = input()
    people_to_remove = []
    if response == 'y':
        for i in people:
            if i.name[0] > end_char:
                people_to_remove.append(i)
    else:
        for i in people:
            if i.name[0] <= end_char:
                people_to_remove.append(i)

    for i in people_to_remove:
        people.remove(i)
    return people


def main():
    cheater_method = False
    people = load_people()

    print('Would you like to cheat? y/n')
    cheater_response = input()
    if cheater_response == 'y':
        cheater_method = True
    while len(people) > 1:
        if cheater_method:
            people = alphabet_approach(people)

        else:
            attributes = generate_dictionaries(people)
            num_people = len(people)
            attribute_inquiry = get_quantity_from_characteristics(
                attributes, num_people)
            # print(attribute_inquiry)
            print("Is your character", attribute_inquiry, "?")
            response = input()
            if response == "y":
                people = clean_list(people, attribute_inquiry, True)
            elif response == "n":
                people = clean_list(people, attribute_inquiry, False)
            else:
                print("Please enter y or n")
                # Todo, create a way to queiry another question
        for i in people:
            print(i.name)

    print("Your character is", people[0].name)

    # get_names_from_characteristics(attributes)


if __name__ == "__main__":
    main()
