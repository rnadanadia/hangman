Class Hangman:

    possible_words = ["becode", "learning", "mathematics,", "sessions"]
    def __init__(self):
        self.word_to_find = list(random.choice(self.possible_words))
        print("DEBUG: Word to find selected: ", self.word_to_find)
        #lives
        self.lives = 5
        self.correctly_guessed_letters = ""
        self.correctly_guessed_letters = self.create_correct_letter()
        print("DEBUG: Correctly guessed letters: ". self.correctly_guessed_letters)

        self.wrongly_guessed_letters = None
        self.turn_count = 0
        self.error_count = 0

    def create_correct_letter(self):
        empty_letter = ""
        for _ in self.word_to_find:
            empty_letter += "_"
        return list(empty_letter)
    
    def play(self):
        """"
        Getting a letter from user and match it the word to find.
        1. Ask input from user.
        2. Check if user's input is valid.
        3. Change the value of turn_count, error_count, lives, correctly_guessed_letters, wrongly_guessed_letters
        """"
        guessed_letter = self.get_user_input()
        print("user choosed: ", guessed_letter)
        if guessed_letter in self.word_to_find:
            print("correct")
            for i, letter in enumerate(self.word_to_find):
                if letter == guessed_letter:
                    self.correctly_guessed_letter[i] = guessed_letter
        else:
            print("wrong guess")
            if self.wrongly_guessed_letters == None:
                self.wrongly_guessed_letters = []
                self.wrongly_guessed_letters.append(guessed_letter)
                self.error_count += 1
                self.lives -= 1
            self.turn_count += 1

    def play_game(self):
        while self.lives > 0 and self.correcyly_guessed_letter != self.word_to_find:
            self.play()
        if self.lives == 0:
            self.game_over()
        else:
            self.well_played()
            
    def game_over(self):
        print("Game over")
    
    def well_played(self):
        print("Well played!")
        
    
    def get_user_input(self):
    """"
    Ask the user to put an input.
    If it doesn't provide a single letter, ask again. 
    """"
        player_input = ""
        while not re.match("^[a-z]$", player_input):
            player_input = input("Please enter a letter: ").lower()
            if len(player_input) != 1:
                print("Only 1 letter")
            if not re.match("^[a-z]$)", player_input):
                print("Only text")
            
            return player_input

game_test(Hangman)
game_test.play_game()
