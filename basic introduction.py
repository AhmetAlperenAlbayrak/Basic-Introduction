import time
name = None

for i in range(10,0,-1):
    print(i)
    time.sleep(0.5)

print('Welcome to the interactive adventure')

while not name:
    name = input('Type your name: ')

print(f'Hello {name}, Are you ready to write your own story?')
time.sleep(1)
answer = input('Yes/No: ').lower()

if answer == 'Yes'.lower():
    print('Alright lets begin')
else:
    print('Alright thanks for trying...')
    time.sleep(2)
    exit

def story(name,surname,age,favoritefood, favoritemusic, personality):
    print(f'Hello my name is {name} {surname}. I am {age} years old. \
I like to eat {favoritefood} and along with it, I like to listen {favoritemusic}.\
I describe myself as {personality}.')
    time.sleep(3)

surname_ = input('What is your surname?\nSurname: ')
age_ = int(input('How old are you?\nAge: '))
favorite_food = input('What is your favorite food? Please choose one from above!\nFavorite Food: ')
favorite_music = input('What is your favorite music to listen?\nSong Name: ')
personality_ = input('How would you describe your personality?\nPersonality: ')
story(name,surname = surname_,favoritemusic= favorite_music,personality=personality_,age=age_,favoritefood=favorite_food)