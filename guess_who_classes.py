class Person:
    # ["Male","Female","Glasses","Brown eyes","Bald","White hair",
    # "Small mouth","Mustache","Brown hair","Big mouth","Small nose",
    # "Blue eyes","Hat","Long hair","Black hair","Earrings","Blonde hair",
    # "Ginger hair","Beard","Big nose"]
    def __init__(self, name, gender, skin_color, hair_color, hair_length, eye_color,
                 teeth, earing=False, hat=False, mustache=False, beard=False, bald=False,
                 hairband=False, hair_accent=None, glasses=False):
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
        self.bald = bald
        self.hairband = hairband
        self.hair_accent = hair_accent
        self.glasses = glasses


def load_people():
    people = []
    #self, name, gender, skin_color, hair_color, hair_length, eye_color,
    #  teeth, earing=False, hat=False, mustache=False, beard=False, bald=False,
    #  hairband=False, glasses=False):
    people.append(Person("Laura", "female", "brown", "black",
                         "long", "green", True, earing=True))
    people.append(Person("Mike", "male", "white", "black",
                         "short", "brown", True, hat=True))
    people.append(Person("Lily", "female", "black",
                         "brown", "long", "green", True, hat=True))
    people.append(Person("Sam", "male", "brown", "black",
                         "short", "green", False, hat=True))
    people.append(Person("Carmen", "female", "black", "white",
                         "short", "brown", True, earing=True))
    people.append(Person("Jordan", "male", "black", [
                  "black", "brown"], "short", "brown", False, mustache=True, beard=True, hair_accent="yellow"))
    people.append(Person("Rachel", "female", "white", "brown",
                         "long", "blue", False, earing=True, glasses=True))
    people.append(Person("Ben", "male", "white", "brown", "short",
                         "brown", False, earing=True, glasses=True))
    # people.append(Person("Daniel", "male", "white", "brown",
    #                      "long", "?", "big", False, beard=True, mustache=True))
    # people.append(Person("Lily", "female", "black", "black",
    #                      "long", "?", "small", True, hat=True))
    # people.append(Person("Liz", "female", "white", "white",
    #                      "long", "?", "small", True, glasses=True))

    return people
