
class Human:
    def tamil_lang(self):
        '''Languages humans talk in this class'''
        return "Speaking in Tamil"
class Dwarf:
    def dwarf_lang(self):
        '''Language Dwarves talk'''
        return "Speaking in Dwarvish"

class Elf:
    def elvish_lang(self):
        return "Speaking in Elvish"


class HumanAdapter:
    def __init__(self,human):
        self.human = human

    def translate_to_english(self):
        '''Takes the input from human tamil_lang and returns it for translates to english'''
        return self.human.tamil_lang()


class DwarfAdapter:
    def __init__(self, dwarf):
        self.dwarf = dwarf

    def translate_to_english(self):
        '''Takes the input from dwarf_lang and returns it for translates to english'''
        return self.dwarf.dwarf_lang()


class ElfAdapter:
    def __init__(self, elf):
        self.elf = elf

    def translate_to_english(self):
        '''Takes the input from elvish_lang() and returns it for translates to english'''
        return self.elf.elvish_lang()

if __name__ == '__main__':
    minions = [HumanAdapter(Human()),ElfAdapter(Elf()),DwarfAdapter(Dwarf())]

    for minion in minions:
        print minion.translate_to_english()