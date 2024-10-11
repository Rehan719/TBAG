
class Charachter():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description 
        self.conversation = None

    def description(self):
        print(f"{self.name} is in this room!")
        print(self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print(f"{self.name} says: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you")

    def fight(self, combat_item):
        print(f"{self.name} doesn't want to fight with you")
        return True

    def describe(self):
        print(f"{self.name} is in this room!")
        print(self.description)

class Enemy(Charachter):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness

    def fight(self, combat_item):
        if combat_item.lower() == self.weakness:
            print(f"You fend {self.name} off with the {combat_item}!!")
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer!")
            return False

    # New interactions
    def steal(self):
        print(f"You attempt to steal from {self.name}, but they catch you! Now you must fight.")
        return False

    def bribe(self, item):
        if item == "gold":
            print(f"{self.name} accepts your bribe and lets you pass!")
            return True
        else:
            print(f"{self.name} scoffs at your attempt to bribe with {item}. Prepare to fight!")
            return False

# Add an additional friendly character subclass
class Friend(Charachter):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)

    def hug(self):
        print(f"{self.name} gives you a big warm hug!")

    def offer_gift(self, gift):
        print(f"You offer {self.name} a {gift}. They are very happy!")
