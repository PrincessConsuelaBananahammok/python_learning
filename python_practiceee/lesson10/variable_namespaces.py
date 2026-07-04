# global
# local
# none local
# build in functions

# global:
dog_name = "Richi"


def dog_actions(name):
    # none local:
    dog_name = name

    def make_sound():
        global dog_name
        print(dog_name)

        # local:
        dog_name = "naida"
        print(dog_name)

    make_sound()
    print(dog_name)

dog_actions("Jack")
print(dog_name)

# local -> none local -> global