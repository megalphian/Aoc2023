filename = 'day7/input.txt'

import re

with open(filename) as f:
    lines = f.readlines()

def assign_card_val(hand):
    card_vals = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
    output = []
    for card in hand:
        for i, val in enumerate(card_vals):
            if card is val:
                output += [i]
    return(output)

def converting_matches(matches):
    if sum(matches) == 25: # 6 = five of a kind
        matches = 6
    elif sum(matches) == 17: # 5 = four of a kind
        matches = 5
    elif sum(matches) == 13: # 4 = full house
        matches = 4
    elif sum(matches) == 11: # 3 = three of a kind
        matches = 3
    elif sum(matches) == 9: # 2 = two pairs
        matches = 2
    elif sum(matches) == 7: # 1 = one pair
        matches = 1
    elif sum(matches) == 5: # 0 = no matches
        matches = 0
    return(matches)

def joker_conversion(joker_count, matches):
    if joker_count == 1:
        if matches == 0:
            matches += 1
        elif matches == 5:
            matches += 1
        else:
            matches += 2
    elif joker_count == 2:
        if matches == 1:
            matches += 2
        elif matches == 2:
            matches += 3
        elif matches == 4:
            matches += 2
    elif joker_count == 3:
        matches += 2
    elif joker_count == 4:
        matches += 1
    else:
        matches += 0
    return(matches)

ranking_list = []
n=0

for line in lines:
    joker_count = 0
    matches = []
    cards, bid = line.strip('\n').split()

    for i in range(5):
        if cards[i] == 'J':
            joker_count += 1
        matches += [len(re.findall(cards[i], cards))]

    matches = converting_matches(matches)
    matches = joker_conversion(joker_count, matches)

    hand_val = assign_card_val(cards)
   
    bid = int(bid)
    n+=1
    
    ranking_list += [(matches, hand_val, bid)]

ranking_list = (sorted(ranking_list))

product_list = []

for i in range(len(ranking_list)):
    product_list += [((i+1) * ranking_list[i][2])]

print(sum(product_list))
