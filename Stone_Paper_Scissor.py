import random
import pygame 
pygame.init()

# Load sound effects
win_sound = pygame.mixer.Sound("win_sound.mp3")
lose_sound = pygame.mixer.Sound("loss_sound.mp3")

#random library to choose for computer
d1={"stone":"scissor","scissor":"paper","paper":"stone"}
d2=["stone","paper","scissor"]
choice_art = {
    "stone": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "paper": """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
    "scissor": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}
def play_sound(sound):
    channel = pygame.mixer.Channel(0)
    channel.set_volume(0.5)  # Set volume to 50%
    channel.play(sound)
    
def solve():
    flag=True
    count_p=0
    count_c=0
    total=0
    while flag:
        total +=1
        #stone =1 scissor=2 paper=3
        x=input("enter the choice of player : ")
        x=x.lower()
        if d2.count(x)<=0:
            print("Invalid Choice")
            x=input("If you want to exit Press : exit ")
            if x=="exit":
                flag=False
            else:
                continue
        temp1=random.randrange(0,3)
        #value of computer will be stored in pl2 as below
        pl2=d2[temp1]    
        #value of  player 1 will be stored in temp
        temp=d1.get(x)
        if x==pl2:
            print("It is Tie")
            
            print("the choice of player is : ",x," : ",choice_art.get(x))
            print("the choice of computer is : ",pl2," : ",choice_art.get(pl2))
            x=input("If you want to exit Press : exit ")
            if x=="exit":
                flag=False
            else:
                continue

        if temp==pl2:
            count_p +=1
            print("Player Won ",count_p,"times")
            play_sound(win_sound)
            print("the choice of player is : ",x,"  : ",choice_art.get(x))
            print("the choice of computer is : ",pl2," : ",choice_art.get(pl2))
        else:
            count_c +=1
            print("Computer Won , Player Loss")
            play_sound(lose_sound)
            print("the choice of player is : ",x," : ",choice_art.get(x))
            print("the choice of computer is : ",pl2," : ",choice_art.get(pl2))
        print("Percentage of Player 1 is ",(count_p/total)*100)
        print("Percentage of Computer is ",(count_c/total)*100)
        x=input("If you want to exit Press : exit ")
        if x=="exit":
            flag=False
        else:
            pass
    pygame.quit()
            
solve()