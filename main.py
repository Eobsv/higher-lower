import gamedata
import random

# TODO Jesli zawodnik mial racje losujemy dalej i przestawiamy druga pozycje na piersza, dodajemy punkt,
# TODO Losujemy dane na druga pozycje

def generate_random_data():
    random_data = gamedata.data[random.randint(0, len(gamedata.data) - 1)]
    return random_data


def higher_lower():
    point = 0
    random_choice_a = generate_random_data()
    print("Who has more followers on Insagram? Option A:")
    print(f"A, {random_choice_a['name']}, {random_choice_a['description']}, from {random_choice_a['country']}, cheats {random_choice_a['follower_count']}")
    random_choice_b = generate_random_data()
    while random_choice_b == random_choice_a:
        random_choice_b = generate_random_data()
    print("Or option B:")
    print(f"B, {random_choice_b['name']}, {random_choice_b['description']}, from {random_choice_b['country']}, cheats {random_choice_b['follower_count']}")
    answer = input("A or B???").upper()
    if answer == 'A' and random_choice_a['follower_count'] > random_choice_b['follower_count']:
        point += 1
        print('You\'re right! ' + str(point) + ' point')
        return point
    elif answer == 'B' and random_choice_b['follower_count'] > random_choice_a['follower_count']:
        point += 1
        print('You\'re right! ' + str(point) + ' point')
        return point
    else:
        print('You lost!')
        return 0


print("Welcome in Higher-Lower Game!")
print("If you are here you know the rules!")
chance = 1
score = 0
while chance > 0:
    pointaddifier = higher_lower()
    if pointaddifier == 1:
        score += pointaddifier
        print('Your score is: ' + str(score) + '!')
    else:
        print("You got " + str(score) + " points. Congratulations!")
        exit()



