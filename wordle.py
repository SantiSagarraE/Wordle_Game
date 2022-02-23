# Play wordle game!!
# You can choose to play in spanish or english
# You have to guess the random word chosen by the computer between 30 words
# GOOD LUCK!!

import random

words_es = ['arbol', 'carta', 'oreja', 'botas', 'cerdo', 'juego', 'gorra', 'cuero', 'libro', 'animo',
            'hueso', 'fuego', 'epoca', 'yogur', 'zurdo', 'video', 'ovulo', 'malta', 'morro', 'cueva',
            'monja', 'multa', 'palta', 'dados', 'grave', 'fallo', 'sabia', 'crema', 'pluma', 'apodo']

words_en = ['pizza', 'paper', 'crazy', 'bazar', 'shark', 'monky', 'quiet', 'clear', 'mouse', 'cheap',
            'light', 'adult', 'chief', 'death', 'dream', 'dress', 'earth', 'fruit', 'green', 'level',
            'night', 'point', 'prize', 'sheep', 'smile', 'state', 'stone', 'issue', 'crime', 'chair']

random_number = random.randint(0,29)

while True:
    leng = input("Select your lenguaje\nEnglish 'EN' or Spanish 'ES':")
    if leng.upper() == 'EN':
        word = words_en[random_number].lower()
        break
    elif leng.upper() == 'ES':
        word = words_es[random_number].lower()
        break
    else:
        print("Please select 'EN' or 'ES'")

large = len(word)
board = []

for i in range(large):
    board.append(['_' for l in range(large)]) # Making the board

for i in board:
    print(" ".join(i))       # Replacing the "," for spaces

colors = {                   # Dictionary to colour the letters
    'green': '\033[92m',
    'yellow': '\033[93m',
    'red': '\033[91m',
    'ENDC': '\033[0m',
}
def color_letter(letter, color):
    return colors[color] + letter + colors['ENDC']

try_counter = 0

while True:
    if try_counter == 5:
        print(f"You lose, the word was {word} try again!")
        break
    guess = input("Guess the word: ").lower()
    if len(guess) != len(word):
        print(f"The word has {len(word)} letters")
    else:
        try_counter += 1
        if guess == word:
            green_guess = []
            for j in range(large):
                green_guess.append(color_letter(guess[j], 'green'))
            board[try_counter-1] = green_guess
            for i in board:
                print(" ".join(i))
            print(f"WIN! \n{try_counter} tries")
            break
        else:
            aux_guess = []
            for j in range(large):
                if guess[j] == word[j]:
                    aux_guess.append(color_letter(guess[j], 'green'))
                elif guess[j] in word:
                    aux_guess.append(color_letter(guess[j], 'yellow'))
                else:
                    aux_guess.append(color_letter(guess[j], 'red'))
            board[try_counter-1] = aux_guess
            for i in board:
                print(" ".join(i))

