# beginscherm met lege velden ___  speler kan (vrij of in invoerveld?) typen, doel van het spel is allemaal opnoemen
# to do:
# plek voor de lijst maken, maar allemaal onzichtbaar
# guessed lijst vullen en correcte zichtbaar maken
# mr. mime wordt gesplitst in "mr." en "mime" ! daardoor totaal 152... komt omdat split ook op de spatie afgaat?
# speloptie laten kiezen: moet het op volgorde ja/nee


import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 700, 500           #zo kun je meerdere variabelen definieren op 1 tekstlijn
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess all Gen 1 Pokemon!")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 50, 200)

SCORE_FONT = pygame.font.SysFont("comicsans", 50)
MENUBUTTON_FONT = pygame.font.SysFont("comicsans", 50)

#this is where the text goes
input_rect = pygame.Rect(250, 300, 200, 50)

#these tell where the lines around the text box should go
input_rect1 = pygame.Rect(200, 300, 300, 3)
input_rect2 = pygame.Rect(200, 300, 3, 80)
input_rect3 = pygame.Rect(200, 380, 300, 3)
input_rect4 = pygame.Rect(500, 300, 3, 80)
startbtnrect = pygame.Rect(100, 100, 200, 80)
abcbtnrect = pygame.Rect(100, 200, 200, 80)   

with open("Alphabet.txt") as f:
    abclistraw = f.read().split()
    abclist = [x.lower() for x in abclistraw]    #change to all lower case

with open("Pokemon.txt") as f:
    pkmnlistraw = f.read().split()
    pkmnlist = [x.lower() for x in pkmnlistraw]    #change to all lower case

guessed = []        #deze lijst begint leeg maar wordt gevuld met goed geraden pokemon (of uberhaupt met alles wat wordt ingevoerd)

def initialize():

    pass    
   

def starting_menu():

    startmenu = True
    clock = pygame.time.Clock()

    startbtnx1, startbtnx2 = 100, 300
    startbtny1, startbtny2 = 100, 180

    abcbtnx1, abcbtnx2 = 100, 300
    abcbtny1, abcbtny2 = 200, 280


    startbtnrect
    abcbtnrect

    while startmenu:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                startmenu = False
                break
                
        # if the key is physically pressed down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    main()

            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                if (startbtnx1 < m_x < startbtnx2) & (startbtny1 < m_y < startbtny2):
                    main("pkmn")
                elif (abcbtnx1 < m_x < abcbtnx2) & (abcbtny1 < m_y < abcbtny2):
                    main("abc")

                    
        clock.tick(FPS)
        draw_menu(WIN)
        
    pygame.quit()
    sys.exit()        


def draw_menu(win):
    win.fill(BLUE)
    
    #start button
    pygame.draw.rect(win, "Green", startbtnrect)
    startbtntext = MENUBUTTON_FONT.render("PKMN", 1, WHITE)
    win.blit(startbtntext, (100, 100))

    #game 2 button
    pygame.draw.rect(win, "Green", abcbtnrect)
    abcbtn_text = MENUBUTTON_FONT.render("ABC", 1, WHITE)
    win.blit(abcbtn_text, (100, 200))
    
    pygame.display.update()

def draw(win, score, user_text, compliment, chosengame, winning_score):
    win.fill(BLACK)

    score_text = SCORE_FONT.render(f"{score}", 1, WHITE)
    win.blit(score_text, (WIDTH//4 - score_text.get_width()//2, 20))
    
    nrleft = winning_score-score
    nrleft_text = SCORE_FONT.render(f"{nrleft}", 1, WHITE)
    win.blit(nrleft_text, (3 * WIDTH//4 - nrleft_text.get_width()//2, 20))
    
    text_surface = SCORE_FONT.render(user_text, True, (255, 255, 255))
    win.blit(text_surface, (input_rect.x, input_rect.y))

    pygame.draw.rect(win, "Green", input_rect1)         
    pygame.draw.rect(win, "Green", input_rect2)
    pygame.draw.rect(win, "Green", input_rect3)
    pygame.draw.rect(win, "Green", input_rect4)
    
    if compliment == True:
        goodguess = SCORE_FONT.render("Correct!", 1, WHITE)
        WIN.blit(goodguess, (WIDTH//2 - goodguess.get_width()//2, HEIGHT//2 - goodguess.get_height()//3))
    
    pygame.display.update()
    


def checkguess(user_text, activelist):

    if user_text == "Abra":
        return True
        #if in lijst & nog niet eerder genoemd
        ## if in gen1-lijst & NIET in 'al-genoemd' lijst
    
    if user_text.lower() in activelist:
        if user_text.lower() in guessed:
            pass
        else:
            guessed.append(user_text.lower())
            return True

def main(chosengame):
    if chosengame == "pkmn":
        activelist = pkmnlist
    elif chosengame == "abc":
        activelist = abclist
    
    WINNING_SCORE = len(activelist)
    
    run = True
    clock = pygame.time.Clock()
    score = 0
    user_text = ""
    message_end_time = 0
    compliment = False
    
    while run:
        clock.tick(FPS)
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
            # if the key is physically pressed down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    # stores text except last letter
                    user_text = user_text[0:-1]
                else:
                    user_text += event.unicode
                
        draw(WIN, score, user_text, compliment, chosengame, WINNING_SCORE)
        
        current_time = pygame.time.get_ticks()
        
        if checkguess(str(user_text), activelist) == True:
            message_end_time = pygame.time.get_ticks() + 2000 # display for 2 seconds
                    
            score += 1   
            user_text = ""
            
        if current_time < message_end_time:
            compliment = True
        else:
            compliment = False
            
        won = False
                
        if score == WINNING_SCORE:
            won = True            

        if won:
            WIN.fill(BLACK)
            text = SCORE_FONT.render("Great job !!", 1, WHITE)
            WIN.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(4000)
            pygame.quit()
            sys.exit()
                 
    



if __name__ == "__main__":
    initialize()
    starting_menu()
    #main()
    pygame.quit()