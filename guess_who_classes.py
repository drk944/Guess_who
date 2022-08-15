class Person:
    # ["Male","Female","Glasses","Brown eyes","Bald","White hair",
    # "Small mouth","Mustache","Brown hair","Big mouth","Small nose",
    # "Blue eyes","Hat","Long hair","Black hair","Earrings","Blonde hair",
    # "Ginger hair","Beard","Big nose"]
    def __init__(self, name, gender, skin_color, hair_color, hair_length, eye_color,
                 teeth='teeth_f', earing='earing_f', hat='hat_f', mustache='mustache_f', beard='beard_f',
                 hairtie='hairtie_f', hair_accent='hair_accent_f', glasses='glasses_f'):
        self.name = name
        self.gender = gender
        self.skin_color = skin_color
        self.hair_color = hair_color
        self.hair_length = hair_length
        self.eye_color = eye_color
        # self.nose = nose
        self.teeth = teeth
        self.earing = earing
        self.hat = hat
        self.mustache = mustache
        self.beard = beard
        self.hairtie = hairtie
        self.hair_accent = hair_accent
        self.glasses = glasses

    def __str__(self):
        return self.name


def load_people():
    people = []
    # self, name, gender, skin_color, hair_color, hair_length, eye_color,
    #  teeth, earing='false', hat='false', mustache='false', beard='false',
    #  hairtie='false', glasses='false'):
    people.append(Person("Laura", "female", "s_brown", "h_black",
                         "h_long", "e_green", teeth='teeth_t', earing='earing_t'))
    people.append(Person("Mike", "male", "s_white", "h_black",
                         "h_short", "e_brown", teeth='teeth_t', hat='hat_t'))
    people.append(Person("Lily", "female", "s_black",
                         "h_brown", "h_long", "e_green", teeth='teeth_t', hat='hat_t'))
    people.append(Person("Sam", "male", "s_brown", "h_black",
                         "h_short", "e_green", hat='hat_t'))
    people.append(Person("Carmen", "female", "s_black", "h_white",
                         "h_short", "e_brown", teeth='teeth_t', earing='earing_t'))
    people.append(Person("Jordan", "male", "s_black",
                         "h_black", "h_short", "e_brown", mustache='mustache_t', beard='beard_t', hair_accent='hair_accent_t'))
    people.append(Person("Rachel", "female", "s_white", "h_brown",
                         "h_long", "e_blue", earing='earing_t', glasses='glasses_t'))
    people.append(Person("Ben", "male", "s_white", "h_brown", "h_short",
                         "e_brown", earing='earing_t', glasses='glasses_t'))
    people.append(Person('Katie', 'female', 's_white',
                         'h_blonde', 'h_long', 'e_blue', hat='hat_t'))
    people.append(Person('Joe', 'male', 's_black', 'h_white', 'h_bald',
                         'e_brown', 'teeth_t', mustache='mustache_t', glasses='glasses_t'))
    people.append(Person('Amy', 'female', 's_white', 'h_black', 'h_short',
                         'e_brown', glasses='glasses_t', hair_accent='hair_accent_t'))
    people.append(Person('Gabe', 'male', 's_brown',
                         'h_black', 'h_short', 'e_brown'))
    people.append(Person('Emma', 'female', 's_white',
                         'h_red', 'h_long', 'e_brown', hairtie='hairtie_t'))
    people.append(Person('Al', 'male', 's_black', 'h_white', 'h_bald',
                         'e_green', mustache='mustache_t', beard='beard_t', glasses='glasses_t'))
    people.append(Person('Mia', 'female', 's_black',
                         'h_black', 'h_long', 'e_brown', 'teeth_t'))
    people.append(Person('Leo', 'male', 's_brown', 'h_white',
                         'h_short', 'e_brown', 'teeth_t', mustache='mustache_t'))
    people.append(Person('Farah', 'female', 's_black', 'h_black',
                         'h_long', 'e_blue', hairtie='hairtie_t'))
    people.append(Person('Daniel', 'male', 's_white', 'h_red', 'h_long',
                         'e_green', hairtie='hairtie_t', mustache='mustache_t', beard='beard_t'))
    people.append(Person('Sofia', 'female', 's_brown', 'h_brown',
                         'h_short', 'e_green', 'teeth_t', earing='earing_t'))
    people.append(Person('David', 'male', 's_white', 'h_blonde', 'h_short',
                         'e_brown', 'teeth_t', hat='hat_t', mustache='mustache_t'))
    people.append(Person('Olivia', 'female', 's_black', 'h_black', 'h_long',
                         'e_brown', hairtie='hairtie_t', hair_accent='hair_accent_t'))
    people.append(Person('Eric', 'male', 's_brown', 'h_black',
                         'h_short', 'e_blue', hair_accent='hair_accent_t'))
    people.append(Person('Liz', 'female', 's_white', 'h_white',
                         'h_long', 'e_blue', 'teeth_t', glasses='glasses_t'))
    people.append(Person('Nick', 'male', 's_white', 'h_brown',
                         'h_short', 'e_brown', earing='earing_t'))

    # people.append(Person("Daniel", "male", "white", "brown",
    #                      "long", "?", "big", 'false', beard='true', mustache='true'))
    # people.append(Person("Lily", "female", "black", "black",
    #                      "long", "?", "small", 'true', hat='true'))
    # people.append(Person("Liz", "female", "white", "white",
    #                      "long", "?", "small", 'true', glasses='true'))

    return people
