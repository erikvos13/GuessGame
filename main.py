# beginscherm met lege velden ___  speler kan (vrij of in invoerveld?) typen, doel van het spel is allemaal opnoemen
# to do:
# plek voor de lijst maken, maar allemaal onzichtbaar
# guessed lijst vullen en correcte zichtbaar maken
# waarom knippert de display van een goede gok?
# ----> doordat de blit / draw 2 of 3x per loop wordt gedaan --> veranderen: pass variabele van goede gok = true o.i.d. naar draw, zodat die bepaalt dat de tekst wordt weergegeven. dan kunnen de overige blit calls weg.
# mr. mime wordt bij de punt al goedgekeurd??
# speloptie laten kiezen: moet het op volgorde ja/nee
# speloptie laten kiezen: welke lijst wil je spelen?

import pandas as pd
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
   

#list1 = open("Alphabet.txt").read().split()

list1 = open("Pokemon.txt").read().split()


lclist1 = [x.lower() for x in list1]    #change to all lower case


WINNING_SCORE = len(lclist1)
print(WINNING_SCORE)

guessed = []        #deze lijst begint leeg maar wordt gevuld met goed geraden pokemon (of uberhaupt met alles wat wordt ingevoerd)

def initialize():

    pass    
   

def starting_menu():

    startmenu = True
    clock = pygame.time.Clock()

    startbtnx1 = 100
    startbtnx2 = 200
    startbtny1 = 100
    startbtny2 = 200

    startbtnrect

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
                    main()
                    
        clock.tick(FPS)
        draw_menu(WIN)
        
    pygame.quit()
    sys.exit()        


def draw_menu(win):
    win.fill(BLUE)
    
    #start button
    pygame.draw.rect(win, "Green", startbtnrect)
    startbtntext = MENUBUTTON_FONT.render("START", 1, WHITE)
    win.blit(startbtntext, (100, 100))
    
    pygame.display.update()

def draw(win, score, user_text):
    win.fill(BLACK)

    score_text = SCORE_FONT.render(f"{score}", 1, WHITE)
    win.blit(score_text, (WIDTH//4 - score_text.get_width()//2, 20))
    
        
    nrleft = WINNING_SCORE-score
    nrleft_text = SCORE_FONT.render(f"{nrleft}", 1, WHITE)
    win.blit(nrleft_text, (3 * WIDTH//4 - nrleft_text.get_width()//2, 20))
    
    text_surface = SCORE_FONT.render(user_text, True, (255, 255, 255))
    win.blit(text_surface, (input_rect.x, input_rect.y))

    pygame.draw.rect(win, "Green", input_rect1)         
    pygame.draw.rect(win, "Green", input_rect2)
    pygame.draw.rect(win, "Green", input_rect3)
    pygame.draw.rect(win, "Green", input_rect4)
    
    pygame.display.update()
    


def checkguess(user_text):
    if user_text == "Abra":
        return True
        #if in lijst & nog niet eerder genoemd
        ## if in gen1-lijst & NIET in 'al-genoemd' lijst

    if user_text.lower() in lclist1:
        if user_text.lower() in guessed:
            pass
        else:
            guessed.append(user_text.lower())
            return True

def main():
    run = True
    clock = pygame.time.Clock()
    score = 0
    user_text = ""
    input_rect = pygame.Rect(200, 200, 140, 32)
    message_end_time = 0
    
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
                
        draw(WIN, score, user_text)
        
        current_time = pygame.time.get_ticks()
        
        if checkguess(str(user_text)) == True:
            message_end_time = pygame.time.get_ticks() + 2000 # display for 2 seconds
            goodguess = SCORE_FONT.render("You did it!", 1, WHITE)
            
            score += 1   
            #pygame.time.wait(2000)
            user_text = ""
            
        if current_time < message_end_time:
            WIN.blit(goodguess, (WIDTH//2 - goodguess.get_width()//2, HEIGHT//2 - goodguess.get_height()//3))
            pygame.display.update()
            
        won = False
                
        if score == WINNING_SCORE:
            won = True            

        if won:
            text = SCORE_FONT.render("You did it!", 1, WHITE)
            WIN.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(5000)
            
        
    
    




if __name__ == "__main__":
    initialize()
    starting_menu()
    #main()
    pygame.quit()