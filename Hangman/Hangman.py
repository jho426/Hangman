#Assignment 6 - Hangman
#Jacqueline Ho
#ICS201
from graphics import *
import time


score = 0
def main():
    #OPENING SCREEN:
    win1 = GraphWin("Opening Screen", 700, 500)
    win1.setBackground("black")
    openingScreen = Image(Point(350, 250), "images/openingscreen.png")
    openingScreen.draw(win1)

    scoreText = Text(Point(380, 325), score)
    scoreText.draw(win1)
    scoreText.setFace('courier')
    scoreText.setSize(30)
    scoreText.setTextColor("white")
    startGame = win1.getMouse()
    x = startGame.getX()
    y = startGame.getY()
    
    if x >= 221 and x <= 464 and y >= 264 and y <= 301:   
    #PICKING A THEME:
        theme = 0
        win1.close()
        win5 = GraphWin("Themes", 700, 500)
        win5.setBackground("silver")
        chooseTheme = Image(Point(350, 50), "images/choosetheme.png")
        chooseTheme.draw(win5)
        themes = Image(Point(350, 300), "images/theme.png")
        themes.draw(win5)

        #Choosing a theme:
        while theme == 0:
            themeChoice = win5.getMouse()
            xTheme = themeChoice.getX()
            yTheme = themeChoice.getY()
            #User picks Ms. Wong theme:
            if xTheme >= 258 and xTheme <= 442 and yTheme >= 197 and yTheme <= 213:
                theme = 1
            #User picks Math theme:
            elif xTheme >= 230 and xTheme <= 466 and yTheme >= 259 and yTheme <= 270:
                theme = 2
            #User picks food theme:
            elif xTheme >= 298 and xTheme <= 380 and yTheme >= 314 and yTheme <= 330:
                theme = 3
            #User picks Marvel theme
            elif xTheme >= 275 and xTheme <= 406 and yTheme >= 377 and yTheme <= 391:
                theme = 4

    #GAME SCREEN:
        def newGame():
            win5.close()
            win2 = GraphWin("Hangman Game", 700, 500)
            win2.setBackground("silver")

            #keyboard: 
            alphabetList=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
            alphabetList2=['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            x = 50
            keyList = []
            letterList = []

            for i in range(13):
                key = Image(Point(x, 350), "images/key.png")
                key.draw(win2)
                keyList.append(key)
                letter = Text(Point(x, 350), alphabetList[i])
                letter.setFace('courier')
                letter.setSize(20)
                letter.draw(win2)
                letterList.append(letter)
                x = x + 50

            x = 50
            keyList2 = []
            letterList2 = []
            for i in range(13):
                key = Image(Point(x, 400), "images/key.png")
                key.draw(win2)
                keyList2.append(key)
                letter = Text(Point(x, 400), alphabetList2[i])
                letter.setFace('courier')
                letter.setSize(20)
                letter.draw(win2)
                letterList2.append(letter)
                x = x + 50

            #menu buttons: 
            newGameButton = Image(Point(75, 25), "images/newGame.png")
            newGameButton.draw(win2)

            exitGameButton = Image(Point(200, 25), "images/exitGame.png")
            exitGameButton.draw(win2)

            hintButton = Image(Point(625, 25), "images/revealhint.png")
            hintButton.draw(win2)

            #words based on theme:
            if theme == 1:
                #Ms. Wong Theme
                wordList = ["kumon", "julian", "justin", "jennifer", "python", "markville", "teacher", "coffee", "piano", "ipad", "rhythm"]
                hintList = ["The one thing that ruins your social life", "the kumon master of the wong household", "the child prodigy",  "the person who is going to give me a 10% mark boost", "the program that makes you scream at a computer screen for hours just to realize you were missing a semi colon", "prison but more depressing", "Ms. Wong's occupation", "the one thing that keeps me alive", "every asian parents dream instrument", "finish the sentence: do kumon or no more ____", "Ms. Wong's favourite word"]

            elif theme == 2:
                #Math Theme
                wordList = ["factoring", "parabolas", "vertex", "roots", "quadratic", "geometry", "altitude", "linear", "variables", "midpoint"]
                hintList = ["something jacqueline does not know how to do", "the thing that curves on a graph", "the maximum/minimum point", "the solution to a quadratic", "the most uesless math topic ever", "the most pointless math topic ever", "height of a triangle", "not curvy", "the letters you use in math", "the middle point"]
                
            elif theme == 3:
                #Food theme
                wordList = ["baguette", "papaya", "cilantro", "tomato", "mcdonalds", "blueberry", "banana", "steak", "avacado", "asparagus"]
                hintList = ["a quintessential french icon", "a tropical fruit with a bunch of seeds", "it looks like parsely", "its a fruit, not a vegetable", "jacqueline's second home", "this fruit has a color in the name", "you can get these for free at loblaws", "the rich version of beef", "finish the sentence: oh it's an _______, thankss", "a really slimey vegetable that tastes weird"]
                            
            else:
                #Marvel theme
                wordList = ["spiderman", "ironman", "endgame", "thor", "hulk", "avengers", "antman", "thanos", "guantlet", "deadpool"]
                hintList = ["two words: tom holland", "the most iconic superhero", "the movie that made Jacqueline cry for 3 days", "the guy who can control thunder", "green", "a pretty cool group of people", "he is very tiny", "purple man", "the snap", "his costume looks like spiderman but isn't"]
        
            from random import randint
            num = randint(0, len(wordList)-1)
            word = wordList[num]

            #lines for the letters:
            x = 50
            for i in range(len(word)): 
                line = Line(Point(x, 300), Point((x+30), 300))
                line.setWidth(3)
                line.draw(win2)
                x = x + 40

            #hangman:
            hangStand = Image(Point(590, 210), "images/hangstand.png")
            hangStand.draw(win2)

            #running the game:
            turns = 0
            correct = 0
            clicked = False
            while turns <10:
                guess = win2.getMouse()
                xGame = guess.getX()
                x = round(guess.getX()/50, 0)
                y = guess.getY()
                x = int(x//1)
                
                #guessed a letter in the first row
                if y <= 370 and y >= 332:
                    character = alphabetList[x-1]
                    #clicked a blank key:
                    if character == "_":
                        clicked = False
                    else:
                        clicked = True
                        n = word.find(character)
                        (letterList[x-1]).undraw()
                        (keyList[x-1]).undraw()
                        alphabetList.pop(x-1)
                        alphabetList.insert(x-1, '_')

                #guessed a letter in the second row
                elif y >= 375 and y <= 418:
                    character = alphabetList2[x-1]
                    #clicked a blank key:
                    if character == "_":
                        clicked = False
                    else:
                        clicked = True
                        n = word.find(character)
                        (letterList2[x-1]).undraw()
                        (keyList2[x-1]).undraw()
                        alphabetList2.pop(x-1)
                        alphabetList2.insert(x-1, '_')

                #if user clicks new game button
                elif xGame >= 28 and xGame <= 122 and y >= 18 and y<= 37:
                    win2.close()
                    newGame()

                #if user clicks exit game button
                elif xGame >= 153 and xGame <= 247 and y >= 18 and y <= 37:
                    win2.close()
                    main()
                    
                #if user clicks hint button
                elif xGame >= 576 and xGame <= 673 and y >= 18 and y <= 37:
                    hint = hintList[num]
                    revealHint = Text(Point(350, 80), hint)
                    revealHint.setFace('courier')
                    revealHint.setStyle('bold')
                    revealHint.setTextColor('crimson')
                    revealHint.setSize(15)
                    revealHint.draw(win2)
                    clicked = False
                    
                #clicked another area on the screen
                else:
                    clicked = False   
               
                #if user clicks on a key:
                if clicked == True:
                    if n >= 0:  #guess is correct
                        while n>=0:
                            correct = correct + 1
                            letter = Text(Point((n+1)*40+25, 290), character)
                            letter.setFace('courier')
                            letter.setSize(20)
                            letter.draw(win2)
                            word = (word[0:n]) + "_" + (word[(n+1): len(word) + 1])
                            n = (word.find(character))
                            
                        #if user guessed the word:
                        if correct == len(word):
                            youWin = Image(Point(350, 250), "images/youwin.png")
                            global score
                            score = score + 1
                            time.sleep(0.3)
                            youWin.draw(win2)
                            time.sleep(1)
                            youWin.undraw()
                            win2.close()
                            win3 = GraphWin("Game Over", 700, 500)
                            win3.setBackground("black")
                            gameOver = Image(Point(350, 200), "images/gameover.png")
                            gameOver.draw(win3)
                            playAgain = Image(Point(190, 400), "images/playagain.png")
                            playAgain.draw(win3)
                            quitButton = Image(Point(510, 400), "images/quit.png")
                            quitButton.draw(win3)

                            userChoice = win3.getMouse()
                            userX = userChoice.getX()
                            userY = userChoice.getY()

                            if userX >= 58 and userX <=323 and userY >= 375 and userY <= 425:
                                win3.close()
                                main()
                                
                            elif userX >= 378 and userX <= 641 and userY >= 379 and userY <= 422:
                                win3.close()
                                win4 = GraphWin("End Game", 700, 500)
                                win4.setBackground("silver")
                                thankYou = Text(Point(350, 200), "Thank you for playing Hangman")
                                thankYou.draw(win4)
                                thankYou.setFace("courier")
                                thankYou.setSize(30)
                                time.sleep(2)
                                exit()
                            
                    #guess is wrong
                    else:
                        turns = turns + 1
                        if turns == 1:
                            head = Circle(Point(535, 175), 25)
                            head.setWidth(5)
                            head.draw(win2)
                        elif turns == 2:
                            body = Line(Point(535, 200), Point(535, 270))
                            body.setWidth(5)
                            body.draw(win2)
                        elif turns == 3:
                            arm1 = Line(Point(535, 210), Point(500, 230))
                            arm1.setWidth(5)
                            arm1.draw(win2)
                        elif turns == 4:
                            arm2 = Line(Point(535, 210), Point(570, 230))
                            arm2.setWidth(5)
                            arm2.draw(win2)
                        elif turns == 5:
                            leg1 = Line(Point(535, 269), Point(500, 300))
                            leg1.setWidth(5)
                            leg1.draw(win2)
                        elif turns == 6:
                            leg2 = Line(Point(535, 269), Point(570, 300))
                            leg2.setWidth(5)
                            leg2.draw(win2)
                        elif turns == 7:
                            eye1 = Circle(Point(525, 165), 3)
                            eye1.setFill("black")
                            eye1.draw(win2)
                        elif turns == 8:
                            eye2 = Circle(Point(545, 165), 3)
                            eye2.setFill("black")
                            eye2.draw(win2)
                        elif turns == 9:
                            nose = Polygon(Point(535, 170), Point(530, 180), Point(535, 180))
                            nose.setWidth(3)
                            nose.draw(win2)
                        else:
                            mouth = Line(Point(525, 190), Point(545, 190))
                            mouth.setWidth(3)
                            mouth.draw(win2)
                            eye1.undraw()
                            eye2.undraw()
                            #new eyes:
                            eye1x1 = Line(Point(520, 160), Point(530, 170))
                            eye1x2 = Line(Point(530, 160), Point(520, 170))
                            eye1x1.draw(win2)
                            eye1x1.setWidth(3)
                            eye1x2.draw(win2)
                            eye1x2.setWidth(3)
                            eye2x1 = Line(Point(540, 160), Point(550, 170))
                            eye2x2 = Line(Point(550, 160), Point(540, 170))
                            eye2x1.draw(win2)
                            eye2x1.setWidth(3)
                            eye2x2.draw(win2)
                            eye2x2.setWidth(3)
                            
                            #losing screen:
                            time.sleep(0.5)
                            win3 = GraphWin("Game Over", 700, 500)
                            win2.close()
                            win3.setBackground("black")
                            gameOver = Image(Point(350, 200), "images/gameover.png")
                            gameOver.draw(win3)
                            playAgain = Image(Point(190, 400), "images/playagain.png")
                            playAgain.draw(win3)
                            quitButton = Image(Point(510, 400), "images/quit.png")
                            quitButton.draw(win3)

                            userChoice = win3.getMouse()
                            userX = userChoice.getX()
                            userY = userChoice.getY()

                            #user plays again
                            if userX >= 58 and userX <=323 and userY >= 375 and userY <= 425:
                                win3.close()
                                main()

                            #users quits game
                            elif userX >= 378 and userX <= 641 and userY >= 379 and userY <= 422:
                                win3.close()
                                win4 = GraphWin("End Game", 700, 500)
                                win4.setBackground("silver")
                                thankYou = Image(Point(350, 250), "images/thankyou.png")
                                thankYou.draw(win4)
                                time.sleep(2)
                                win4.close()
                                exit()
        newGame()
main()             
                
                
                
                
                
                
                
           
                
                
                

