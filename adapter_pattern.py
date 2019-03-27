
class human:

    def call_me(self):
        return ("Tamil Language")
class dwarf:

    def call_me(self):
        return ("Dwarvish")

class elves:


    def call_me(self):
        return ("Elvish")

if __name__ == '__main__':
    minions = [human(),dwarf(),elves()]
    for minion in minions:
        print minion.call_me()

