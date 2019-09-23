'''
Zeke Mostov
CS 302 Fall 2018 Prof. Dickerson
Implementation project 2
Implementation of the strategy game problem from the second exam
'''

rowsprint = None
collumsprint = None
#Function that loops to take in user input
def main():
    global rowsprint
    global collumsprint
    m = []

    print("WELCOME to a game!")
    print("Enter q to quit at any time")
    x = input("Please input an even number of integers (w spaces): ")

    list = x.split() #split on spaces and put into a list of ints
    for i in range(len(list)):
        m.append(int(list[i]))
    g = Game(m)
    g.build()

    while x != "q":
        x = input("Would you like to print tables (p) or get answer (a); ")
        if x == "a":
            print("Valid inputs for the next 2 question are 0 through ", len(m))
            x = input("Enter i as an int; ")
            i = int(x)
            x = input("Enter j as an int; ")
            j = int(x)
            print("Answer: choose the integer at index: " , g.c[i][j] )
        if x == "p":
            print("Valid inputs for the next two question are 0 through ",len(m))
            x = input("Enter # of rows you would like to print: ")
            rowsprint = int(x)
            x = input("Enter # of collums you would like to print: ")
            collumsprint = int(x)
            g.tables()
        #else:
            #print("Sorry, we did not recognize your input. ")

class Game:
    def __init__(self, m):
        l = (len(m))
        c = [["-"] *l for i in range(l)]
        b = [["-"] *l for i in range(l)]
        self.m = m #this is the array of integers for the game
        self.c = c #stores index of choice
        self.b = b #stores score

    #function to print out filled tables
    def tables(self):
        global rowsprint
        global collumsprint

        print("Below is the Choice table")
        print("-", end='')
        for j in range(len(self.m)):
              print(" ",j," ", end='')
        print('')
        for j in range(collumsprint):
            for i in range(rowsprint):
                if i == 0:
                    print(j, end='')
                print(" ",self.c[i][j]," ", end='')
                if i == (rowsprint - 1):
                    print("")

        print("Below is the score table")
        print("-", end='')
        for j in range(len(self.m)):
              print(" ",j," ", end='')
        print('')
        for j in range(collumsprint):
            for i in range(rowsprint):
                if i == 0:
                    print(j, end='')
                print(" ",self.b[i][j]," ", end='')
                if i == (rowsprint - 1):
                    print("")

    #initialize base cases and then build matrices c and b
    def build(self):
        #initialize base cases
        print("now building")
        for i in range (len(self.m)):
            #
            self.c[i][i] = i
            self.b[i][i] = self.m[i]

        #build out solution
        for j in range(1, len(self.m), 1):
            for i in range (j-1, -1, -1):
                #print("i is: ", i, " j is: ", j)
                if self.m[i]-self.b[i+1][j] > self.m[j]-self.b[i][j-1]:
                    self.b[i][j] = self.m[i]-self.b[i+1][j]
                    self.c[i][j] = i
                else:
                    self.b[i][j] = self.m[j]-self.b[i][j-1]
                    self.c[i][j] = j

#call to main() so program runs on its on when executed
main()
