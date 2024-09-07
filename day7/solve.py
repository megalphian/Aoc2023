filename = 'day7/input.txt'

import re

with open(filename) as f:
    lines = f.readlines()

def assign_card_val(hand):
    card_vals = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    output = []
    for card in hand:
        for i, val in enumerate(card_vals):
            if card is val:
                output += [i]
    return(output)

def converting_matches(matches):
    if sum(matches) == 25:
        matches = 6
    elif sum(matches) == 17:
        matches = 5
    elif sum(matches) == 13:
        matches = 4
    elif sum(matches) == 11:
        matches = 3
    elif sum(matches) == 9:
        matches = 2
    elif sum(matches) == 7:
        matches = 1
    elif sum(matches) == 5:
        matches = 0
    return(matches)

ranking_list = []
n=0
for line in lines:
    matches = []
    cards, bid = line.strip('\n').split()

    for i in range(5):
        matches += [len(re.findall(cards[i], cards))]

    matches = converting_matches(matches)
    hand_val = assign_card_val(cards)
   
    hand_val = assign_card_val(cards)

    bid = int(bid)
    n+=1
    
    ranking_list += [(matches, hand_val, bid)]

ranking_list = (sorted(ranking_list))

product_list = []

for i in range(len(ranking_list)):
    product_list += [((i+1) * ranking_list[i][2])]

print(sum(product_list))