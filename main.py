import pygame
import sys
from random import randint
from button import *
pygame.init()

screen_width, screen_height = 1024, 720
screen = pygame.display.set_mode((screen_width, screen_height+180))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,30)
run = True
y = screen_height 
fps = 60
speed = 100
n = 20 #length of arr
distance = screen_width/n
width = distance - 1
arr = [randint(1, screen_height) for p in range(0, n)]
arr_sorted = sorted(arr)
# Colors
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
arr_colors =[white]*n
a = False

speed_up_button = button(white, 110,screen_height+60,50,20,'Up')
speed_down_button = button(white, 110,screen_height+120,50,20,'Down')
length_up_button = button(white, 265,screen_height+60,50,20,'+')
length_down_button = button(white, 265,screen_height+120,50,20,'-')
generate_arr_button = button(white, 400,screen_height+70,100,20,'Generate')
stop_button = button(white, 400,screen_height+100,100,20,'Stop')
bubble_sort_button = button(white,600,screen_height+40,100,20,'Bubble Sort')
insert_sort_button = button(white,600,screen_height+70,100,20,'Insert Sort')
choise_sort_button = button(white, 600,screen_height+100,100,20,'Choise Sort')




def massage_to_screen(msg, color, msg_width, msg_height):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [msg_width, msg_height])

def draw():
    global speed
    global a
    global arr_colors
    global n
    global arr
    global arr_sorted
    global distance
    global width
    for i in range(len(arr)):
        pygame.draw.rect(screen, arr_colors[i], pygame.Rect(i * distance, y, width, -arr[i]))
    
    massage_to_screen('Speed: '+str(200 - speed), white, 50,screen_height+90)
    massage_to_screen('Length: '+str(n), white, 200,screen_height+90)

    speed_up_button.draw(screen)
    speed_down_button.draw(screen)
    length_up_button.draw(screen)
    length_down_button.draw(screen)
    bubble_sort_button.draw(screen)
    generate_arr_button.draw(screen)
    stop_button.draw(screen)
    insert_sort_button.draw(screen)
    choise_sort_button.draw(screen)
 

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:

            if bubble_sort_button.isOver(pos):
                arr_colors =[white]*n
                a = False
                buble_sort(arr)

            if(choise_sort_button.isOver(pos)):
                arr_colors =[white]*n
                a = False
                choise_sort(arr)

            if(insert_sort_button.isOver(pos)):
                arr_colors =[white]*n
                a = False
                insert_sort(arr)

            if stop_button.isOver(pos):
                a = True

            if speed_up_button.isOver(pos) and speed > 9:
                speed -=10

            if speed_down_button.isOver(pos) and speed<200:
                speed += 10

            if length_up_button.isOver(pos) and n < 300:
                a = True
                n+=1
                distance = screen_width/n
                width = distance - 1
                arr = [randint(1, screen_height) for p in range(0, n)]
                arr_sorted = sorted(arr)
                arr_colors =[white]*n

            if length_down_button.isOver(pos) and n > 2:
                a = True
                n-=1
                distance = screen_width/n
                width = distance - 1
                arr = [randint(1, screen_height) for p in range(0, n)]
                arr_sorted = sorted(arr)
                arr_colors =[white]*n

            if(generate_arr_button.isOver(pos)):
                a = True  
                distance = screen_width/n
                width = distance - 1
                arr = [randint(1, screen_height) for p in range(0, n)]
                arr_sorted = sorted(arr)
                arr_colors =[white]*n
                
                
                
               
                
def refill(): 
    screen.fill((0, 0, 0)) 
    draw() 
    pygame.display.update() 
    pygame.time.wait(speed) 

def buble_sort(arr):
    for i in range(1,len(arr)):
        for j in range(0, len(arr)-i):
            if a: return
            if(arr[j]>arr[j+1]):
                arr_colors[j] = blue
                arr_colors[j+1] = red
                refill()
                arr[j+1],arr[j] = arr[j], arr[j+1]
                arr_colors[j] = white
                arr_colors[j+1] = white
            else:
                arr_colors[j] = blue
                arr_colors[j+1] = blue
                refill()
                arr_colors[j] = white
                arr_colors[j+1] = white

def insert_sort(arr):
    for i in range(1, len(arr)):
        k = i 
        while k > 0 and arr[k-1] > arr[k]:
                arr_colors[k] = red
                arr_colors[i] = blue
                refill()
                arr[k],arr[k-1] = arr[k-1],arr[k]
                arr_colors[k] = white
                arr_colors[i] = white
                k-=1 
        

def choise_sort(arr):
    for i in range (0, len(arr)-1):
        for j in range(i+1,len(arr)):
            if(a):
                return 
            if(arr[i]>arr[j]):
                arr_colors[i] = blue
                arr_colors[j] = red
                refill()
                arr[i],arr[j] = arr[j],arr[i]
                arr_colors[i] = white
                arr_colors[j] = white
            else:
                arr_colors[i] = blue
                arr_colors[j] = blue
                refill()
                arr_colors[i] = white
                arr_colors[j] = white



while run:
    
    screen.fill((0, 0, 0))
   
    draw()
   
    pygame.display.flip()
    clock.tick(fps)