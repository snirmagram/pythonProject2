class Card:
    def __init__(self,value,suit):
        self.value=value
        self.suit=suit

        self.suits={1:"Diamond",2:"Spade",3:"Heart",4:"Club"}
        self.values={11:"Jack",12:"Queen",13:"King",14:"ace"}


    def __str__(self):
        if self.value > 10:
            return f"{self.values[self.value]}:{self.suits[self.suit]}"
        return f"{self.value}:{self.suits[self.suit]}"

    def __repr__(self):
        if self.value > 10:
            return f"{self.values[self.value]}:{self.suits[self.suit]}"
        return f"{self.value}:{self.suits[self.suit]}"

    def __gt__(self, other):
        if self.value>other.value:
            return True
        elif self.value == other.value:
            if self.suit>other.suit:
                return True
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        if self.value > other.value:
            return True
        elif self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False
        else:
            return False