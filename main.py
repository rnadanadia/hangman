from typing import List

possible_words: List[str] = ['becode', 'learning', 'mathematics', 'session']

def start_game():
    lives: int = 5
    wrongly_guessed_letters: List = []
    word_to_find: str = possible_words[0]
    well_guessed_letters: List[str] = len(word_to_find) * [' _ ']
    error_count: int = 1
    turn_count: int = 1
    while lives > 0 and ' _ ' in well_guessed_letters:
        """ 
        Function that will perfom the operation based on the number of lives of player and the letter which is guessed.
        While lives is more than 0 OR there is underscore appears in a text: If the length of the letter is 1 and it is 
        an alphabet, if the letter is a part of the word, print "Letter is in the word". Then print "Turn" to calculate 
        how many turn the player has played.
        """
        play: str = input("Please write a letter: ")
        if len(play)!= 1 or not play.isalpha():
            print("The Input Must Contain 1 Alphabet.")
            continue
        if play in word_to_find:
            print(f"{play} is in the word")
            print(f"Turn :{turn_count}")
            for i, letter in enumerate(word_to_find):
                if letter == play:
                    well_guessed_letters[i] = letter
                    print("".join(well_guessed_letters))
                    turn_count += 1

        else:
            """
            If the letter is not a part of the word, print "(Letter) is not in the word". Print "Turn" to calculate
            how many turn the player has played. Print "Errors" to calculate the number of error. Print "Lives" to calculate 
            the number of lives remains. The wrong guessed letter will be added into wrong guessed letter list.
            """
            print("".join(well_guessed_letters)) 
            print(f"{play} not in the word") 
            print(f"Turn :{turn_count}") 
            print(f"Error :{error_count}") 
            print(f"Lives :{lives}") 
            wrongly_guessed_letters.append(play) 
            print(f"Wrong guessed letters: {wrongly_guessed_letters}") 
            error_count += 1
            lives -= 1 
            turn_count += 1

    if lives == 0: 
        print("Game Over")

    elif ' _ ' not in well_guessed_letters:
        print(f'You found the word: {word_to_find} in {turn_count} turns with {error_count} errors!')
        
        """
        If the lives is 0, print"Game Over"
        If the lives is more than 0 and the player has guessed all correct letters, it prints "You found The Word with number of
        Turns and Error"
        """

start_game()





