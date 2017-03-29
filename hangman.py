import random, re, os
import hangman_gui

NUM_GUESSES = 6

class Game():

    def __init__(self, word):
        self.lenw = len(word)
        self.word = [[0]*2 for i in range(self.lenw)]
        for i in range(0,self.lenw):           
            self.word[i][0] = word[i]
            if (word[i] == ' '):
                self.word[i][1] = 1
        self.guesses = ""
        self.guessleft = NUM_GUESSES

    def guess(self, g):
        if (g in self.guesses):
            self.guessleft -= 1
            print("You already guessed the letter {}".format(g))
            print("Guesses: {}".format(self.guesses))
            return
        matches = 0
        if (len(self.guesses) > 0):
            self.guesses += ","
        self.guesses += g
        for i in range(0,self.lenw):
            if ((self.word[i][0]).lower() == g):
                matches += 1
                self.word[i][1] = 1
        print("Letter {} had {} matches".format(g,matches))
        print("Guesses: {}".format(self.guesses))
        if (matches == 0):
            self.guessleft -= 1

    def is_solved(self):
        for i in range(0,self.lenw):
            if (self.word[i][1] == 0):
                return False
        return True

    def show(self):
        outstr = ""
        for i in range(0,self.lenw):
            outstr += str(self.word[i][0])
        return outstr

def random_word():
    word_ar = ['Capitals','Blackhawks','Blues','Wild','Rangers','Penguins','Blue Jackets','Hurricanes','Canadians','Bruins',
                'Senators','Maple Leafs','Lightning','Islanders','Predators','Ducks','Sharks','Oilers','Flames','Kings']
    return word_ar[random.randrange(0,len(word_ar))]

def init_prompt():
    while True:
        userin = input("Welcome to Hangman, press 1 for new game or 0 to quit : ")
        if (userin == '1'):
            return random_word()
        elif (userin == '0'):
            quit()
    
def output_word(g):
    outstr = "Your word is "
    for i in range(0,g.lenw):
        if (g.word[i][1] == 1):
            outstr += "'"+str(g.word[i][0])+"'"
        else :
            outstr += "__ "
    print(outstr)

def play(gleft):
    while True:
        userin = (input("Please guess a letter : ")).lower()
        if (len(re.findall('([a-z]{1})',userin)) == 1):
            os.system('cls' if os.name == 'nt' else 'clear')
            return userin

def main():
    '''
    this is a multiline
    comment
    '''
    while True:
        nw = init_prompt()
        g = Game(nw)
        hangman_gui.print_gui(g.guessleft)
        #print(nw)
        while (g.guessleft > 0 and g.is_solved() == False):
            output_word(g)
            usrguess = play(g.guessleft)
            g.guess(usrguess)
            hangman_gui.print_gui(g.guessleft)
        if (g.guessleft == 0):
            print("Game over, sorry you lost! Word was {}".format(g.show()))
        else :
            print("Good job! word was: {}".format(g.show()))
        
 

if __name__ == "__main__":main()