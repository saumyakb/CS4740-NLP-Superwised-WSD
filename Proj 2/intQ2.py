import random

def random_deck(cards_in_deck):
    deck=[]
    card = ''
    length = 1
    while length < cards_in_deck:
        card=''
        card+=random.choice(Set)
        card+=random.choice(num)
        card=str(card)
        
        if card not in deck:
            deck.append(card)
            length +=1
    print deck



Set = ['hearts ','spades ','diamonds ','club ']
num = ['A','2','3','4','5','6','7','8','9','10','joker','queen','king']
random_deck(32)
