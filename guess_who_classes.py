class Person:
    # ["Male","Female","Glasses","Brown eyes","Bald","White hair",
    # "Small mouth","Mustache","Brown hair","Big mouth","Small nose",
    # "Blue eyes","Hat","Long hair","Black hair","Earrings","Blonde hair",
    # "Ginger hair","Beard","Big nose"]
    def __init__(self, name, gender, skin_color, hair_color, hair_length, eye_color,
                 nose, teeth, earing=False, hat=False, mustache=False, beard=False, glasses=False):
        self.name = name
        self.gender = gender
        self.skin_color = skin_color
        self.hair_color = hair_color
        self.hair_length = hair_length
        self.eye_color = eye_color
        self.nose = nose
        self.teeth = teeth
        self.earing = earing
        self.hat = hat
        self.mustache = mustache
        self.beard = beard
        self.glasses = glasses

    def load_people(abc):
        print("Hello my name is " + abc.name)


def load_people():
    people = []
    people.append(Person("Daniel", "Male", "White", "Brown",
                         "long", "?", "big", False, beard=True, mustache=True))
    people.append(Person("Lily", "Female", "black", "black",
                         "long", "?", "small", True, hat=True))
    people.append(Person("Liz", "Female", "white", "white",
                         "long", "?", "small", True, glasses=True))

    return people
