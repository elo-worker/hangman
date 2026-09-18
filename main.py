import random 
word_list = ["яблоко", "лемон", "свобода", "обезьяна", "человек", "деньги"]


def get_word():
    return random.choice(word_list).upper()


def display_hangman(tries):
    stages = [# финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
                ]
    return stages[tries]


def play(word):
   word_completion = ['_'] * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
   guessed = False                    # сигнальная метка
   guessed_letters = []               # список уже названных букв
   guessed_words = []                 # список уже названных слов
   tries = 6                          # количество попыток
    
   print('Давайте играть в угадайку слов!')
   print(display_hangman(tries))
   print(' '.join(word_completion))              
   print()

   while guessed == False and tries > 0:
         guess = input("Введите букву или слово целиком").upper()
         if len(guess) == 1:
            if not guess in guessed_letters:
               guessed_letters.append(guess)
               if guess in word:
                  print("Эта буква есть в слове!")
                  for i in range(len(word)):
                     if word[i] == guess:
                        word_completion[i] = guess
               else:
                  print("Этой буквы нет в слове!")
                  tries -= 1
            else:
               print("Вы уже вводили эту букву!")
               continue
         elif len(guess) == len(word):
            if not guess in guessed_words:
               guessed_words.append(guess)
               if guess == word:
                  guessed = True
                  word_completion = list(word)
               else:
                  print("Неправильное слово")
                  tries -= 1
            else:
               print("Вы уже вводили это слово")   
               continue
         else:
            print("Недопустимый ввод, попробуйте ещё раз")
            continue

         print(display_hangman(tries))
         print(' '.join(word_completion))
         print()

         if '_' not in word_completion:
            guessed = True                

   if guessed:
      print("Поздравляем, вы выиграли! Загаданное слово:", word)
   else:
      print("Вы проиграли. Попытки закончились. Загаданное слово было:", word)                


while True:
   random_word = get_word()
   play(random_word)
        
   # Спрашиваем игрока, хочет ли он продолжить
   again = input("Хотите сыграть еще раз? (да/нет): ").lower()
   if again not in ['да', 'д', 'yes', 'y']:
      print("Спасибо за игру! До встречи.")
      break
