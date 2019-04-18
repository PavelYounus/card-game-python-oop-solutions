from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

#mycards=[(s,r) for s in SUITE for r in RANKS]

class Deck():
    def __init__(self):
        print("Creating new ordered Deck")
        self.allCards = [(s, r) for s in SUITE for r in RANKS]


    def shuffle(self):
        print("Shuffling Deck")
        shuffle(self.allCards)

    def split_in_half(self):
        return (self.allCards[:26], self.allCards[26:])



class Hand():
    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_cards(self):
        return self.cards.pop()




class Player():
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_cards()
        print("{} has placed {}".format(self.name, drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards=[]
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.remove_cards())
            return war_cards

    def still_has_cards(self):
        '''

        :return:
        '''
        return len(self.hand.cards) != 0




print("Welcome to war game")

#create new deck and split in half

deck = Deck()
deck.shuffle()
half1, half2 = deck.split_in_half()


#create players

comp = Player("Computer",Hand(half1))

name = input("Whats your name? ")

user = Player(name,Hand(half2))


war_count = 0
total_rounds = 0


while user.still_has_cards() and comp.still_has_cards():
    total_rounds +=1
    print("Time for a new round")
    print("here are the current standing")
    print(user.name+" has cards count: "+str(len(user.hand.cards)))
    print(comp.name + " has cards count: " + str(len(comp.hand.cards)))
    print("Play a card")
    print('\n')

    table_cards=[]

    c_cards=comp.play_card()
    p_cards=user.play_card()

    table_cards.append(c_cards)
    table_cards.append(p_cards)


    if c_cards[1]==p_cards[1]:
        war_count +=1

        print("WAR!")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if RANKS.index(c_cards[1]) < RANKS.index(p_cards[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

    else:
        if RANKS.index(c_cards[1]) < RANKS.index(p_cards[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)


print("Game over, number of rounds " + str(total_rounds))
print(" a war happened "+str(war_count)+" times")

print("Does computer has card?")
print(str(comp.still_has_cards()))

print("Does user has card?")
print(str(user.still_has_cards()))

