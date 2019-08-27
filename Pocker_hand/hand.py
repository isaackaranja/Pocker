import re
import collections

def sorted_list(list_item):
    for i in range(len(list_item)):
        for j in range(i+1,len(list_item)):
            if list_item[i] > list_item[j]:
                temp = list_item[i]
                list_item[i] = list_item[j]
                list_item[j] = temp
    return list_item


def sequence(list):
    count = 0
    for c in range(len(list)):
        for j in range(c + 1, len(list)):
            if list[c] + 1 == list[j]:
                count += 1

    return count


def dup(li):
#li = ['c','c', 'c', 'c', 'c']
    count = 0
    for i in range(len(li)):
        if li[0] == li[i]:
            count += 1
    return count


def rem_charater(li):
    for i in li:
        if i[0] == 'A':
            i = "14" + i[1:]
            li.append(i)
        if i[0] == 'k':
            i = "13" + i[1:]
            li.append(i)
        if i[0] == 'Q':
            i = "12" + i[1:]
            li.append(i)
        if i[0] == 'J':
            i = "11" + i[1:]
            li.append(i)
    for c in li:
        if ord(c[0]) > 64:
            li.remove(c)
    return li

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(f'{self.suit} of {self.value}')

class Group_of_cards:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        #string_cards = "AC,3S,AS,3D,4C"
        string_cards = input("Enter cards to deal:   ")
        unclean_list = list(string_cards.split(' '))
        li = rem_charater(unclean_list)
        for i in range(len(li)):
            space, value, suit = re.split('(\d+)', li[i])
            self.cards.append(Card(suit, value))

        #fun = rem_charater(self.cards)
        # for i in self.cards:
        #     if i.value == 'A':
        #         i.value == 14
        #     if i.value == 'K':
        #         i.value == 13
        #     if i.value == 'Q':
        #         i.value == 12
        #     if i.value == 'J':
        #         i.value == 11
    def show(self):
        for cad in self.cards:
            cad.show()
    def winning_hand(self):
        vall = []
        count = 0
        for i in self.cards:
            v = int(i.value)
            vall.append(v)
        counter = collections.Counter(vall)
        k = list(counter.values())
        if len(k) > 2:
        #if 1 in k:
            #k.remove(1)
            for item in counter.values():
                if item == 2:
                    count += 1
                if item == 3:
                    count = 3
                if item == 4:
                    count = 4
            if count == 1:
                print("pair")
            elif count == 2:
                print("two pair")
            elif count == 3:
                print("THREE OF A KIND")
            #else:
                #print("high card")
        if len(k) == 2:
            if 3 and 2 in k:
                print("full house")
            else:
                print("FOUR OF A KIND")

        if len(k) == 5:
            sortedlist = sorted_list(vall)
            count_sequence = sequence(sortedlist)
            list_suit = []
            for s in self.cards:
                sut = s.suit
                list_suit.append(sut)
            sut_match = dup(list_suit)
            if count_sequence == len(vall)-1 and sut_match == len(list_suit):
                print("STRAIGHT FLASH")
            if count_sequence != len(vall)-1 and sut_match == len(list_suit):
                print("FLASH")
            if count_sequence == len(vall)-1 and sut_match != len(list_suit):
                print("STRAIGHT")
            else:
                print("HIGH CARD")





        #print(vall)




ret = Group_of_cards()
ret.winning_hand()

