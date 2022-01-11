from art import logo, vs
from game_data import data
from random import randint
from replit import clear


def random_one_dic():
    return data[randint(0, len(data) - 1)]


def print_two(a, b):
    clear()
    print(logo)
    print('Current score: ', score)
    print(f"Compare A: {a['name']}, {a['description']}, from {a['country']}.")
    print(vs)
    print(f"Against B: {b['name']}, {b['description']}, from {b['country']}.")


def score_count(score):
    if (c == 'b' and control == 'b') or (c == 'a' and control == 'a'):
        score += 1
    return score


finish = False
score = 0
a = random_one_dic()
b = random_one_dic()
while a == b or a['follower_count'] == b['follower_count']:
    b = random_one_dic()
while finish == False:

    if a['follower_count'] > b['follower_count']:
        control = 'a'
    else:
        control = 'b'

    print_two(a, b)
    c = input("Who has more followers? Type 'A' or 'B': ").lower()

    score_new = score_count(score)

    if score_new != score:
        score = score_new
    else:
        finish = True

    if c == 'b':
        a = b
    b = random_one_dic()
    while a == b or a['follower_count'] == b['follower_count']:
        b = random_one_dic()

clear()
print(logo)
print(f"Sorry, that's wrong. Final score: {score}")
