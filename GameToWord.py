# donnu -> university -> yellow -> window -> stop.
Words = list()
number_move = 0
print("Хід гравця #1.")
while True:
    word = input('Введіть слово: ')
    if word.isalpha() == True:
        break
    print("Слово має складатись виключно з літер.")
Words.append(word)  
previous_word = word
number_move = number_move + 1
while word != 'stop': # while not end_game:
    while True: # Хід гравця
        print("Хід гравця #%i." % (number_move % 2 + 1))
        word = input('Введіть слово: ')
        word = word.lower()
        if word == 'stop':
            break
        if word.isalpha() == False:
            print("Слово має складатись виключно з літер.")
        elif word[0] != previous_word[-1]:
            print("Слово має починатись з літери %c" % previous_word[-1])
        elif word in Words:
            print("Слово вже фігурувало під час гри.")
        else:
            previous_word = word
            Words.append(word)
            break
    number_move += 1
print('Переміг гравець #%i' % (number_move % 2 + 1))




"""# donnu -> university -> yellow -> window -> stop.


def Game():
    def PlayerMove(previous_word):
        while True: # Хід гравця
            print("Хід гравця #%i." % (number_move % 2 + 1))
            word = input('Введіть слово: ')
            word = word.lower()
            if word == 'stop':
                return word
            if word.isalpha() == False:
                print("Слово має складатись виключно з літер.")
            elif word[0] != previous_word[-1]:
                print("Слово має починатись з літери %c" % previous_word[-1])
            elif word in Words:
                print("Слово вже фігурувало під час гри.")
            else:
                previous_word = word
                Words.append(word)
                return word
    Words = list()
    number_move = 0
    print("Хід гравця #1.")
    while True:
        word = input('Введіть слово: ')
        if word.isalpha() == True:
            break
        print("Слово має складатись виключно з літер.")
    Words.append(word)  
    previous_word = word
    number_move = number_move + 1
    while word != 'stop': # while not end_game:
        word = PlayerMove(previous_word)
        previous_word = word
        number_move += 1
    print('Переміг гравець #%i' % (number_move % 2 + 1))

Game()
"""