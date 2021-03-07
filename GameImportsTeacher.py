import time
import teacher

class Game:
    def __init__(self, file):
        self.file = file
        self.time_score = 0
        self.accuracy_score = 0
        self.current_line = ""

    # This method should display a line for the user to type and return the
    # user's input and the amount of time it took to type

    def play(self):
        start_time = time.time()
        text = input(self.current_line)
        end_time = time.time()
        total = end_time - start_time
        return text, total

    # This method should take the user's input and time and set the score attributes
    def calculate_score(self, input, time):
        pass

    # This method runs the game as long as there are lines in the file

    def full_game(self):
        lines = self.file.readlines()

        for line in lines:
            # If line doesn't end in '\n', add '\n'
            if line[-1] == '\n':
                self.current_line = line
            else:
                self.current_line = line + '\n'
            user_input, time = self.play()
            self.calculate_score(time, user_input)


def main(file):
    game = Game(file)
    game.full_game()


teacherName, className, filename = teacher.get_info()
# filename = "text.txt"
file = open(filename, 'r')
main(file)
