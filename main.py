#Woo or Doom, by Jola Oke

import time
import random

likeMeter = 0 # Variable that determines how much the girl likes you
girl = '' # The girl you decide to woo
food = '' # The food you buy
alreadyInside = False # Already inside the house from having to collect your shirt that she washed or to return her shirt

def printText(string): # Function to print text letter-by-letter, easy for player to read
    for c in string:
        print(c,end='')
        time.sleep(0.025)

printText("WOO OR DOOM - a text-based adventure game.\n")
printText("Press Enter to play.")
play = input() # Start the game


# Variables such as run1, text1, input1 are named so just to know where in the game the certain event is
                            
def intro(): # Introduction of the game
    print("----------------------------------------------------------------------------------------------------")
    text1 = '''

You are a 16 year-old boy named Kosuke Okumura, and you are a junior at Kyoto High Prepatory School.
It is 6:30 AM on a Tuesday morning, and you just woke up. You get out of your bed and go to
the bathroom to brush your teeth and shower. When you come back to your room, something is
different. There is a golden envelope with your name on it on your bed. You walk cautiously
towards your bed and slowly pick up the envelope. Curious, you open it and see a piece of
paper. It's a letter! It says:

"Dear Kosuke,

I am writing from the future to warn you gravely that the world is soon about to end.
In the year 2033, the Earth will be attacked by a powerful demon. This beast will bring
upon us mass destruction and annihilation. Many of your friends and family will die.
However, you have the power to prevent this from happening.

This demon manifested itself from the heart of a young woman, who happens to be one of the
girls who currently attends your school, Kyoto High Prepatory School. The demon resides in
her heart and gradually becomes more powerful as the girl ages. However, the demon can be
driven away by the most powerful force in the world . . . love.

Kosuke, you need to win the heart of this girl right now, otherwise the world as you know
it will cease to exist. Unfortunately, I don't know the name of this girl, but I can give
you some clues. This girl is in your class, has blonde hair, has green eyes, loves cosplaying
anime characters, and has a pair.

I hope you take on this heavy responsibility. The fate of mankind rests in your hand.

All the best,
Kosuke Okumura

P.S. Don't get rid of your Pikachu pajamas. I know you love them."
'''

    text2 = '''
Since nobody knows you are thinking of throwing away your Pikachu pajamas, you believe that this
letter really is from the future. You narrow down the list of girls that fit the description from
the letter. The girl with the demon in her heart is either Eli Aize or Mei Temuri, and you must win
the hearts of one of them.

But what does he mean by she has a pair?

'''
    printText(text1)
    time.sleep(0.5)
    printText(text2)

def mapOne(): # School map
    global likeMeter
    global girl
    
    text3 = '''
You arrive at school and you are now standing in the hallway in front of your locker. Mei walks down
the hall to her locker, appearing to ignore the people around her. Eli is walking up the stairs, with
her two pigtails dnagling as she walks.
'''
    printText(text3)
    text4 = '''
You have to make a decision right now. It's either Eli or Mei? You must woo one of these ladies.
Who would it be?
[A]: Eli
[B]: Mei
'''
    run1 = True
    while run1:
        printText(text4)
        girl = input().upper()
        if girl == 'A':
            mapEli()
            run1 = False
        elif girl == 'B':
            mapMei()
            run1 = False
        else:
            printText("I don't understand. Please select A or B.\n")
            run1 = True

def mapEli(): # School map with Eli
    global likeMeter
    global alreadyInside

    text5 = '''
It is lunch time and you are in the cafeteria. Eli is in line to get her food. You want to find a way to
approach her. Do you want to sit next to her on a table, or bump into her when she's walking with her food?
[A]: Sit next to her
[B]: Bump into her
'''
    run2 = True
    while run2:
        printText(text5)
        input2 = input().upper()
        if input2 == 'A':
            text6 = '''
Eli is sitting on table alone, eating her foot. You walk up to her and ask, "May I sit here?"
"Sure." She says, half-heartedly.
You put your tray on the table and sit next to her.
'''
            lunchEli()
            run2 = False
        elif input2 == 'B':
            text9 = '''
Eli is walking to a table with her lunch tray in hand. You walk towards her, and quickly turn your head
away before you reach her. You then collide into her, her food spills over your shirt, and you both fall.
"Oh my gosh! I'm so sorry! Are you okay?" She says.
[A]: Say, "Oh, it was my fault. I'm sorry for bumping into you. I'm too clumsy."
[B]: Shout, "What's wrong with you! Are you blind or something? You got your food all over me, you idiot!"
'''
            run2 = False
            run5 = True
            while run5:
                printText(text9)
                input5 = input().upper()
                if input5 == 'A':
                    likeMeter += 2
                    text16 = '''
You get up, saying, "Oh, it was my fault. I'm sorry for bumping into you. I'm too clumsy."
You offer Eli a hand, she takes it, and you pull her up.
"Thank you." She says as she gets up.
A moment later, she notices your shirt.
"Oh my gosh! I'm so sorry about your shirt! I have a spare shirt in my locker. It will be a little small
but do you want to wear that?" She asks.
[A]: Say, "Yeah sure, I'll appreciate that."
[B]: Say, "Oh don't worry, it'll be fine."
'''
                    run5 = False
                    run7 = True
                    while run7:
                        printText(text16)
                        input7 = input().upper()
                        if input7 == 'A':
                            likeMeter += 1
                            text17 = '''
"Yeah sure, I'll appreciate that." You say.
You follow Eli to her locker. She opens her locker and grabs a small white shirt. She gives you the shirt and you
change in the bathroom nearby. A minute later, you step out of the bathroom. The shirt is very small and is
extremely tight on you. Do you want to complain about the shirt being too small or make a joke of it?
[A]: Complain
[B]: Make joke
'''
                            run7 = False
                            run8 = True
                            while run8:
                                printText(text17)
                                input8 = input().upper()
                                if input8 == 'A':
                                    likeMeter -= 2
                                    text18 = '''
You exclaim, "Oh my! This shirt is so smsall!"
"I'm so sorry. I know it must be uncomfortable." Eli says. "I'm really sorry."
You sigh, continuing to look at the shirt.
Eli says, "Maybe I could wash your shirt. You could come get it from my house later today."
[A]: Say. "Yeah, that would be nice. I could come get it later."
[B]: Say, "No, no, no. I don't want to cause you so much trouble. I'll handle it. I'll return your shirt later today."
'''
                                    run8 = False
                                    run9 = True
                                    while run9:
                                        printText(text18)
                                        input9 = input().upper()
                                        if input9 == 'A':
                                            text19 = '''
You say, "Yeah, that would be nice. I could come get it later."
She says, "Sure, that'll be fine."
Eli writes down her address on a piece of paper and hands the paper to you.
"See you later." She says, and walks away.

You have to find a way to woo her when you go to her house to get her shirt. It's your only chance.
'''
                                            run9 = False
                                            printText(text19)
                                            buyFood()
                                            washShirt()
                                            alreadyInside = True
                                            mapHouseEli()
                                        elif input9 == 'B':
                                            likeMeter += 3
                                            text20 = '''

"No, no, no. I don't want to cause you so much trouble. I'll handle it. I'll return your shirt later today." You say.
She says, "Wow, thank you. Again, I'm really sorry about it."
Eli writes down her address on a piece of paper and hands you the paper, "Here's my address. See you then."
You take the paper, and Eli walks away.

You have to find a way to woo her when you go to her house to return her shirt. It's your only chance.
'''
                                            run9 = False
                                            printText(text20)
                                            buyFood()
                                            returnShirt()
                                            alreadyInside = True
                                            mapHouseEli()
                                        else:
                                            printText("I don't understand. Please select A or B.\n")
                                            run9 = True
                                elif input8 == 'B':
                                    likeMeter += 3
                                    text21 = '''
You laugh and say, "Okay, this shirt actuallly makes me look muscular."
Eli bursts into laughter and says, "That's real cute. You actually look like this character from this anime. I can't
quite place my finger on it."
"You watch anime?" I ask.
"Yeah." She says. "Do you?"
"Yes, I love anime!" I answer.
"Do you cosplay?" She asks.
I reply, "No, but I've always wanted to. Haven't really had the time or money to do so."
"Really? You should come by my house later today then. I could show you this huge cosplay selection I have." She says.
This is a perfect chance! This will help in wooing her.
"Oh yeah, most definitely! I'd love to come." You say.
She writes down her address on a piece of paper and hands it over to you.
"Well, I'll see you later." She says, then walks away.

'''
                                    printText(text21)
                                    buyFood()
                                    mapHouseEli()
                                    run8 = False
                                else:
                                    printText("I don't understand. Please select A or B.\n")
                                    run = True
                        elif input7 == 'B':
                            likeMeter += 1
                            text22 = '''
"Oh don't worry, it'll be fine." You say
"Are you sure?" She asks.
"Yeah, it's fine." You pause. "Hey I can still get lunch. Since yours spilled, do you want to share?"
She smiles ans says, "Yeah sure. I'd like that."

You get your lunch and the two of you sit down on a table.

'''
                            printText(text22)
                            lunchEli()
                            run7 = False
                        else:
                            printText("I don't understand. Please select A or B.\n")
                            run7 = True
                elif input5 == 'B':
                    text15 = '''
"What's wrong with you! Are you blind or something? You got your food all over me, you idiot!" You shout at her.
"I said I was sorry!" Eli screams, and gets up and runs the other way.

What a mistake you've made. There goes all your chances of winning her heart.
'''
                    printText(text15)
                    run5 = False
                    loseFailedToWoo()
                    
                else:
                    printText("I don't understand. Please select A or B.\n")
                    run5 = True
        else:
            printText("I don't understand. Please select A or B.\n")
            run2 = True

def mapMei(): # School map with Mei
    global likeMeter
    global alreadyInside

    text5 = '''
It is lunch time and you are in the cafeteria. Mei is in line to get her food. You want to find a way to
approach her. Do you want to sit next to her on a table, or bump into her when she's walking with her food?
[A]: Sit next to her
[B]: Bump into her
'''
    run2 = True
    while run2:
        printText(text5)
        input2 = input().upper()
        if input2 == 'A':
            text6 = '''
Mei is sitting on table alone, eating her foot. You walk up to her and ask, "May I sit here?"
"Sure." She says, half-heartedly.
You put your tray on the table and sit next to her.
'''
            lunchMei()
            run2 = False
        elif input2 == 'B':
            text9 = '''
Mei is walking to a table with her lunch tray in hand. You walk towards her, and quickly turn your head
away before you reach her. You then collide into her, her food spills over your shirt, and you both fall.
"Oh my gosh! I'm so sorry! Are you okay?" She says.
[A]: Say, "Oh, it was my fault. I'm sorry for bumping into you. I'm too clumsy."
[B]: Shout, "What's wrong with you! Are you blind or something? You got your food all over me, you idiot!"
''' 
            run2 = False
            run5 = True
            while run5:
                printText(text9)
                input5 = input().upper()
                if input5 == 'A':
                    likeMeter += 2
                    text16 = '''
You get up, saying, "Oh, it was my fault. I'm sorry for bumping into you. I'm too clumsy."
You offer Mei a hand, she takes it, and you pull her up.
"Thank you." She says as she gets up.
A moment later, she notices your shirt.
"Oh my gosh! I'm so sorry about your shirt! I have a spare shirt in my locker. It will be a little small
but do you want to wear that?" She asks.
[A]: Say, "Yeah sure, I'll appreciate that."
[B]: Say, "Oh don't worry, it'll be fine."
'''
                    run5 = False
                    run7 = True
                    while run7:
                        printText(text16)
                        input7 = input().upper()
                        if input7 == 'A':
                            likeMeter += 1
                            text17 = '''
"Yeah sure, I'll appreciate that." You say.
You follow Mei to her locker. She opens her locker and grabs a small white shirt. She gives you the shirt and you
change in the bathroom nearby. A minute later, you step out of the bathroom. The shirt is very small and is
extremely tight on you. Do you want to complain about the shirt being too small or make a joke of it?
[A]: Complain
[B]: Make joke
'''
                            run7 = False
                            run8 = True
                            while run8:
                                printText(text17)
                                input8 = input().upper()
                                if input8 == 'A':
                                    likeMeter -= 2
                                    text18 = '''
You exclaim, "Oh my! This shirt is so smsall!"
"I'm so sorry. I know it must be uncomfortable." Mei says. "I'm really sorry."
You sigh, continuing to look at the shirt.
Mei says, "Maybe I could wash your shirt. You could come get it from my house later today."
[A]: Say. "Yeah, that would be nice. I could come get it later."
[B]: Say, "No, no, no. I don't want to cause you so much trouble. I'll handle it. I'll return your shirt later today."
'''
                                    run8 = False
                                    run9 = True
                                    while run9:
                                        printText(text18)
                                        input9 = input().upper()
                                        if input9 == 'A':
                                            text19 = '''
You say, "Yeah, that would be nice. I could come get it later."
She says, "Sure, that'll be fine."
Mei writes down her address on a piece of paper and hands the paper to you.
"See you later." She says, and walks away.

You have to find a way to woo her when you go to her house to get her shirt. It's your only chance.
'''
                                            run9 = False
                                            printText(text19)
                                            buyFood()
                                            washShirt()
                                            alreadyInside = True
                                            mapHouseMei()
                                        elif input9 == 'B':
                                            likeMeter += 3
                                            text20 = '''

"No, no, no. I don't want to cause you so much trouble. I'll handle it. I'll return your shirt later today." You say.
She says, "Wow, thank you. Again, I'm really sorry about it."
Mei writes down her address on a piece of paper and hands you the paper, "Here's my address. See you then."
You take the paper, and Mei walks away.

You have to find a way to woo her when you go to her house to return her shirt. It's your only chance.
'''
                                            run9 = False
                                            printText(text20)
                                            buyFood()
                                            returnShirt()
                                            alreadyInside = True
                                            mapHouseMei()
                                        else:
                                            printText("I don't understand. Please select A or B.\n")
                                            run9 = True
                                elif input8 == 'B':
                                    likeMeter += 3
                                    text21 = '''
You laugh and say, "Okay, this shirt actuallly makes me look muscular."
Mei bursts into laughter and says, "That's real cute. You actually look like this character from this anime. I can't
quite place my finger on it."
"You watch anime?" I ask.
"Yeah." She says. "Do you?"
"Yes, I love anime!" I answer.
"Do you cosplay?" She asks.
I reply, "No, but I've always wanted to. Haven't really had the time or money to do so."
"Really? You should come by my house later today then. I could show you this huge cosplay selection I have." She says.
This is a perfect chance! This will help in wooing her.
"Oh yeah, most definitely! I'd love to come." You say.
She writes down her address on a piece of paper and hands it over to you.
"Well, I'll see you later." She says, then walks away.

'''
                                    printText(text21)
                                    buyFood()
                                    mapHouseMei()
                                    run8 = False
                                else:
                                    printText("I don't understand. Please select A or B.\n")
                                    run = True
                        elif input7 == 'B':
                            likeMeter += 1
                            text22 = '''
"Oh don't worry, it'll be fine." You say
"Are you sure?" She asks.
"Yeah, it's fine." You pause. "Hey I can still get lunch. Since yours spilled, do you want to share?"
She smiles ans says, "Yeah sure. I'd like that."

You get your lunch and the two of you sit down on a table.

'''
                            printText(text22)
                            lunchMei()
                            run7 = False
                        else:
                            printText("I don't understand. Please select A or B.\n")
                            run7 = True
                elif input5 == 'B':
                    text15 = '''
"What's wrong with you! Are you blind or something? You got your food all over me, you idiot!" You shout at her.
"I said I was sorry!" Mei screams, and gets up and runs the other way.

What a mistake you've made. There goes all your chances of winning her heart.
'''
                    run5 = False
                    loseFailedToWoo()
                    
                else:
                    printText("I don't understand. Please select A or B.\n")
                    run5 = True
        else:
            printText("I don't understand. Please select A or B.\n")
            run2 = True

def lunchEli(): # Lunch with Eli
    global likeMeter
    
    text7 = '''
As you turn your head towards her, you notice her outfit. You think to yourself that she looks like the
typical school girls in anime. Also, you see her phone case, which has a really cool, and ominous, picture
of Kaneki from Tokyo Ghoul. Do you want to comment on her outfit or phone case?
[A]: Outfit
[B]: Phone case
'''
    global run2
    run2 = False
            
    run3 = True
    while run3:
        printText(text7)
        input3 = input().upper()
        if input3 == 'A':
            likeMeter += 2
            text8 = '''
"You look like those school girls in animes." You say, jokingly.
She laughs slightly, "Really? Do you watch anime?"
[A]: Say, "Yeah! I love anime. My favorite is Death Note."
[B]: Say, "Yeah! And I really enjoyed Tokyo Ghoul! It was so sad!"
'''
            run3 = False
            run4 = True
            while run4:
                printText(text8)
                input4 = input().upper()
                if input4 == 'A':
                    likeMeter += 4
                    text11 = '''
"Yeah! I love anime. My favorite is Death Note." You say.
"Oh, nice! Death Note was one of the first ones that I watched. It was pretty good. I was blown away with how
smart they were. It was crazy!" She says.
"I know, right? That anime was so good." You reply.
"You know, I actually have a cosplay collection. If you want, you could come over today and I could show you."
She says.
This is a perfect chance! This will help in wooing her.
"Oh yeah, most definitely! I'd love to come." You say.
She writes down her address on a piece of paper and hands it over to you.
"Well, I'll see you later." She says, then gets up and leaves.
'''
                    run4 = False
                    printText(text11)
                    buyFood()
                    mapHouseEli()
                    
                elif input4 == 'B':
                    likeMeter += 5
                    text12 = '''
"Yeah! And I really enjoyed Tokyo Ghoul! It was so sad!" You say.
She replies, "I know, right? To be honest, I cried at the end."
"Yeah, same. The opening song is the greatest of all time." You say.
"I actually have a cosplay outfit of Kaneki. I have a lot of cosplay outfits at home." She says, brightening up.
"What? That's so cool! I've always wanted to cosplay." You say.
"You know what?" She pauses. "You should come over after school. I could show you my collection."
This is a perfect chance! This will help in wooing her.
"Oh yeah, most definitely! I'd love to come." You say.
She writes down her address on a piece of paper and hands it over to you.
"Well, I'll see you later." She says, then gets up and leaves.
'''
                    run4 = False
                    printText(text12)
                    buyFood()
                    mapHouseEli()
                    
                else:
                    printText("I don't understand. Please select A or B.\n")
                    run4 = True
            
        elif input3 == 'B':
            likeMeter += 3
            text10 = '''
"Your phone case is so cool! I really like it." You say.
"Really? Thanks! I didn't know you watched anime." She says.
[A]: Say, "Oh, I love anime. My favorite is Death Note."
[B]: Say, "Yeah, I do! And I really enjoyed Tokyo Ghoul. It was so sad!"
'''
            run3 = False

            run6 = True
            while run6:
                printText(text10)
                input6 = input().upper()
                if input6 == 'A':
                    likeMeter += 4
                    text13 = '''
"Oh, I love anime. My favorite is Death Note." You say.
"Oh, nice! Death Note was one of the first ones that I watched. It was pretty good. I was blown away with how
smart they were. It was crazy!" She says.
"I know, right? That anime was so good." You reply.
"You know, I actually have a cosplay collection. If you want, you could come over today and I could show you."
She says.
This is a perfect chance! This will help in wooing her.
"Oh yeah, most definitely! I'd love to come." You say.
She writes down her address on a piece of paper and hands it over to you.
"Well, I'll see you later." She says, then gets up and leaves.
'''
                    run6 = False
                    printText(text13)
                    buyFood()
                    mapHouseEli()
                    
                elif input6 == 'B':
                    likeMeter += 5
                    text14 = '''
"Yeah, I do! And I really enjoyed Tokyo Ghoul! It was so sad!" You say.
She replies, "I know, right? To be honest, I cried at the end."
"Yeah, same. The opening song is the greatest of all time." You say.
"I actually have a cosplay outfit of Kaneki. I have a lot of cosplay outfits at home." She says, brightening up.
"What? That's so cool! I've always wanted to cosplay." You say.
"You know what?" She pauses. "You should come over after school. I could show you my collection."
This is a perfect chance! This will help in wooing her.
"Oh yeah, most definitely! I'd love to come." You say.
She writes down her address on a piece of paper and hands it over to you.
"Well, I'll see you later." She says, then gets up and leaves.
'''
                    run6 = False
                    printText(text14)
                    buyFood()
                    mapHouseEli()
                else:
                    printText("I don't understand. Please select A or B.\n")
                    run6 = True
        else:
            printText("I don't understand. Please select A or B.\n")
            run3 = True
    run2 = False

def lunchMei(): # Lunch with Mei
    global likeMeter
    
    text7 = '''
As you turn your head towards her, you notice her outfit. You think to yourself that she looks like the
typical school girls in anime. Also, you see her phone case, which has a really cool, and ominous, picture
of Kaneki from Tokyo Ghoul. Do you want to comment on her outfit or phone case?
[A]: Outfit
[B]: Phone case
'''
    global run2
    run2 = False
            
    run3 = True
    while run3:
        printText(text7)
        input3 = input().upper()
        if input3 == 'A':
            likeMeter += 2
            text8 = '''
"You look like those school girls in animes." You say, jokingly.
She laughs slightly, "Really? Do you watch anime?"
[A]: Say, "Yeah! I love anime. My favorite is Death Note."
[B]: Say, "Yeah! And I really enjoyed Tokyo Ghoul! It was so sad!"
'''
            run3 = False
            run4 = True
            while run4:
                printText(text8)
                input4 = input().upper()
                if input4 == 'A':
                    likeMeter += 4
                    text11 = '''
"Yeah! I love anime. My favorite is Death Note." You say.
"Oh, nice! Death Note was one of the first ones that I watched. It was pretty good. I was blown away with how
smart they were. It was crazy!" She says.
"I know, right? That anime was so good." You reply.
"You know, I actually have a cosplay collection. If you want, you could come over today and I could show you."
She says.
This is a perfect chance! This will help in wooing her.
"Oh yeah, most definitely! I'd love to come." You say.
She writes down her address on a piece of paper and hands it over to you.
"Well, I'll see you later." She says, then gets up and leaves.
'''
                    run4 = False
                    printText(text11)
                    buyFood()
                    mapHouseMei()
                    
                elif input4 == 'B':
                    likeMeter += 5
                    text12 = '''
"Yeah! And I really enjoyed Tokyo Ghoul! It was so sad!" You say.
She replies, "I know, right? To be honest, I cried at the end."
"Yeah, same. The opening song is the greatest of all time." You say.
"I actually have a cosplay outfit of Kaneki. I have a lot of cosplay outfits at home." She says, brightening up.
"What? That's so cool! I've always wanted to cosplay." You say.
"You know what?" She pauses. "You should come over after school. I could show you my collection."
This is a perfect chance! This will help in wooing her.
"Oh yeah, most definitely! I'd love to come." You say.
She writes down her address on a piece of paper and hands it over to you.
"Well, I'll see you later." She says, then gets up and leaves.
'''
                    run4 = False
                    printText(text12)
                    buyFood()
                    mapHouseMei()
                    
                else:
                    printText("I don't understand. Please select A or B.\n")
                    run4 = True
            
        elif input3 == 'B':
            likeMeter += 3
            text10 = '''
"Your phone case is so cool! I really like it." You say.
"Really? Thanks! I didn't know you watched anime." She says.
[A]: Say, "Oh, I love anime. My favorite is Death Note."
[B]: Say, "Yeah, I do! And I really enjoyed Tokyo Ghoul. It was so sad!"
'''
            run3 = False

            run6 = True
            while run6:
                printText(text10)
                input6 = input().upper()
                if input6 == 'A':
                    likeMeter += 4
                    text13 = '''
"Oh, I love anime. My favorite is Death Note." You say.
"Oh, nice! Death Note was one of the first ones that I watched. It was pretty good. I was blown away with how
smart they were. It was crazy!" She says.
"I know, right? That anime was so good." You reply.
"You know, I actually have a cosplay collection. If you want, you could come over today and I could show you."
She says.
This is a perfect chance! This will help in wooing her.
"Oh yeah, most definitely! I'd love to come." You say.
She writes down her address on a piece of paper and hands it over to you.
"Well, I'll see you later." She says, then gets up and leaves.
'''
                    run6 = False
                    printText(text13)
                    buyFood()
                    mapHouseMei()
                    
                elif input6 == 'B':
                    likeMeter += 5
                    text14 = '''
"Yeah, I do! And I really enjoyed Tokyo Ghoul! It was so sad!" You say.
She replies, "I know, right? To be honest, I cried at the end."
"Yeah, same. The opening song is the greatest of all time." You say.
"I actually have a cosplay outfit of Kaneki. I have a lot of cosplay outfits at home." She says, brightening up.
"What? That's so cool! I've always wanted to cosplay." You say.
"You know what?" She pauses. "You should come over after school. I could show you my collection."
This is a perfect chance! This will help in wooing her.
"Oh yeah, most definitely! I'd love to come." You say.
She writes down her address on a piece of paper and hands it over to you.
"Well, I'll see you later." She says, then gets up and leaves.
'''
                    run6 = False
                    printText(text14)
                    buyFood()
                    mapHouseMei()
                else:
                    printText("I don't understand. Please select A or B.\n")
                    run6 = True
        else:
            printText("I don't understand. Please select A or B.\n")
            run3 = True
    run2 = False

def buyFood(): # Buy food to eat with Mei/Eli at their house
    global likeMeter
    global food

    text1 = '''

You are on Main Street. To your right, there is a candy shop where you can buy chocolates and cakes. To your left,
there is a restaurant famous for its rice and curry. You want to buy something to eat while at her house.
What do you want to buy?
[A]: Rice and curry
[B}: Chocolates and cakes
'''
    run1 = True
    while run1:
        printText(text1)
        input1 = input().upper()
        if input1 == 'A':
            text2 = '''
You go into the restaurant and buy rice and curry for two people. It smells great!
'''
            food = 'rice and curry'
            printText(text2)
            run1 = False
        elif input1 == 'B':
            text3 = '''
You go into the candy shop and buy a lot of chocolates and small cakes. They look gorgeous!
'''
            food = 'chocolates and cakes'
            printText(text3)
            run1 = False
        else:
            print("I don't understand. Please select A or B.\n")
            run1 = True
            
    
def returnShirt(): # Return Mei/Eli's shirt
    global likeMeter

    text1 = '''
It's 5 PM and you knock on her door. She opens the door and says, "Hey!"
"Hey, how are you doing? May I come in?" You ask.
"Yeah, sure!" She says, and she lets you in her house.
Once inside, you give her shirt and say, "Thanks for letting me wear it. I really appreciate it."
She takes the shirt and say, "Oh no problem. I'm glad I could help anyway."
'''
    printText(text1)

def washShirt(): # Collect your shirt from Mei/Eli
    global likeMeter

    text1 = '''
It's 5 PM and you knock on her door. She opens the door and says, "Hey!"
"Hey, how are you doing? May I come in?" You ask.
"Yeah, sure!" She says, and she lets you in her house.
Once inside, she grabs your washed shirt and hands it to you.
You take the shirt and say, "Thanks so much. I really appreciate it."
She says, "Oh no problem. I'm glad I could help anyway."
'''
    printText(text1)

def chooseCosplay(): # Choose what anime you want Mei/Eli to cosplay from. A chance to win or lose her heart
    global likeMeter
    global girl

    animeList = ['A','B','C','D'] # Elements correspond with the options in text1 below
    goodAnime1 = random.choice(animeList)
    goodAnime2 = random.choice(animeList)
    
    text1 = '''
"So..." She starts. "What anime do you want me to cosplay from?"
[A]: Say, "Sword Art Online."
[B]: Say, "Death Note."
[C]: Say, "Tokyo Ghoul."
[D]: Say, "Monogatori Series."
'''
    run1 = True
    while run1:
        printText(text1)
        input1 = input().upper()
        if input1 == goodAnime1 or input1 == goodAnime2:
            likeMeter += 4
            text2 = '''
Her eyes light up and brighten. A smiles crosses her face as she says, "Oh I love that anime!"
"Give me a moment!" She says as she rushes off to get the outfit, and then to the bathroom to change
After a few moments, she comes out and stands in front of you. You are awe-struck, breath-taken!
"Well," She says with a twirl. "What do you think?"
[A]: Say, "You look absolutely beautiful."
[B]: Say, "You look just like the character! Awesome!"
'''
            run1 = False
            run2 = True
            while run2:
                printText(text2)
                input2 = input().upper()
                if input2 == 'A':
                    if likeMeter >= 10:
                        text4 = '''
"You look absolutely beautiful." You say.
Her faces blushes! She lowers her head as a smile trickles across her face.
She pauses, then says, "Thank you so much!"
She runs and hugs you.
A moment passes, then you pull her head closer to yours. You give her a passionate kiss. She returns the kiss!
"I love you." You say.
"I love you too, Kosuke!" She says, beaming.
'''
                        printText(text4)
                        # If girl is Eli (A), you win. If the girl is Mei (B), you lose because Mei is the wrong girl
                        if girl == 'A':
                            win()
                            run2 = False
                        if girl == 'B':
                            loseWrongGirl()
                            run2 = False
                    else:
                        text5 = '''
"You look absolutely beautiful." You say.
She takes a step back.
"Oh, sorry." She says. "I didn't know that's how you thought of me. Sorry, but I wasn't thinking that way.
I think we should just be friends, nothing more."
"Oh-" You start.
"I think it'll be best if you go home now. Sorry." She says, and walks away.
You sigh, and leave her house.
'''
                        printText(text5)
                        loseFailedToWoo()
                        run2 = False
                elif input2 == 'B':
                    if likeMeter >= 10:
                        text6 = '''
"You look just like the character! Awesome!" You say.
Her facial expression saddens.
"Oh..." She starts. "I'm such a fool!"
"What? Why?" You ask.
"I was foolish enough to think that you saw me in a different way. I'm sorry, this is my fault. This is getting
weird now." She says.
"Wait-" You start.
"I think you should go home." She says, and runs away with her head in her hands.
'''
                        printText(text6)
                        loseFailedToWoo()
                        run2 = False
                    else:
                        text7 = '''
"You look just like the character! Awesome!" You say.
"Really? Thank you!" She says, excited. "You're such a cool friend!"
It was at this moment you realized you have been friendzoned, and have failed this mission.
After a moment, you look at your watch and say, "Oh, it's getting late. I should I should start heading home."
"Yeah, sure. Good night!" She says.
"Good night." You say, and you leave her house.
'''
                        printText(text7)
                        loseFailedToWoo()
                        run2 = False
                else:
                    printText("I don't understand. Please select A or B.")
                    run2 = True
        elif input1 != goodAnime1 or input1 != goodAnime2:
            likeMeter -= 2
            text3 = '''
Her expression saddens. She says, "Oh I actually don't like that anime, sorry. I don't have a cosplay outfit
for it."
"Oh..." You say, embarassed.
"Maybe we should eat the food you brought, and I'll look for an outfit afterwards." She suggests.
'''
            printText(text3)
            dinner()
            run1 = False
        else:
            print("I don't understand. Please select A, B, C, or D.\n")
            run1 = True


def mapHouseEli(): #Eli's House map
    global likeMeter
    global food
    global alreadyInside

    if alreadyInside == True:
        printText('''
"So..." You say. "I heard that you have a realy cool cosplay collection. Would it be cool if I see it, since I'm already here?"
Excitement flashes in her eyes, and she says, "Sure! That'll be great!"
"Awesome!" You say.
''')
    if alreadyInside == False:
        printText('''
It's 5 PM and you knock on Eli's door. Eli opens the door and says, "Hey! Come in!"
"Hey, how's it going?" You say as you walk inside her house

''')

    text1 = '''
"Hey, Eli." You say. "I brought some ''' + food + ''' for us to eat."
You raise up a plastic bag with the food you bought.
"Oh that's great! Why'd you buy all that though?" She says.
[A]: Say, "We could have dinner and call it our little first date."
[B]: Say, "Just in case we got hungry."
'''
    run1 = True
    while run1:
        printText(text1)
        input1 = input().upper()
        if input1 == 'A':
            likeMeter += 4
            text2 = '''
"We could have dinner and call it our little first date." You say, with a little smirk.
Eli smiles hysterically and says, "Awn that's so cute. You sure do know you to woo a lady."
"I try, I try." You say jokingly.
Both of you laugh, as Eli takes the plastic bag and sets it down on a table.
'''
            printText(text2)
            run1 = False
        elif input1 == 'B':
            likeMeter += 1
            text3 = '''
"Just in case we got hungry." You say.
"Oh, well I guess you come prepared." She says jokingly.
Both of you laugh, as Eli takes the plastic bag and sets it down on a table.
'''
            printText(text3)
            run1 = False
        else:
            printText("I don't understand. Please select A or B.\n")
            run1 = True

    text4 = '''
"Do you want to come up to my room to see me cosplay? Or do you want to stay down here?" She asks.
[A]: Say, "Sure, let's go to your room."
[B]: Say, "I'll rather stay here in the living room."
'''
    run2 = True
    while run2:
        printText(text4)
        input2 = input().upper()
        if input2 == 'A':
            text5 = '''
"Sure, let's go to your room." You say.
Eli leads you up to her room. Her room is very neat and orderly, while still packed with uncountable anime
posters and figures. At the edge of her room, there is a heavily secured door. The door is locked with a
chain and a padlock. This is weird. What do you want to do?
[A]: Ask Eli about the door
[B]: Ignore the door
'''
            run2 = False
            run3 = True
            while run3:
                printText(text5)
                input3 = input().upper()
                if input3 == 'A':
                    securedDoor()
                    run3 = False
                elif input3 == 'B':
                    printText("You ignore the locked door.")
                    chooseCosplay()
                    run3 = False
                else:
                    print("I don't understand. Please select A or B.\n")
                    run3 = True
        elif input2 == 'B':
            text6 = '''
"I'll rather stay here in the living room." You say.
"Okay, sure." She says. "Give me a minute."
Eli runs upstairs to her room for a moment.
While she's gone, you take a look around the living room. You notice there a lot of family pictures. You count at least
12 pictures of Eli, her mom, and her dad. This interests you. You also notice something strnage. In a dark corridor,
there is a heavily secured door. The door is locked with a chain and a padlock. This makes you quite curious.
Eli comes back downstairs.
[A]: Ask Eli about the door
[B]: Talk about the many family pictures
[C]: Remain silent
'''
            run2 = False
            run4 = True
            while run4:
                printText(text6)
                input4 = input().upper()
                if input4 == 'A':
                    securedDoor()
                    run4 = False
                elif input4 == 'B':
                    text7 = '''
"You sure have a lot of family pictures. You guys must be close, I guess." You say.
Eli's face hardens.
"I'll rather not talk about my family." She says. "Excuse me."
She goes to the bathroom.

'''
                    text8 = '''
You sense something strange. Eli is definitely hiding something, and that door seems very suspicious.
What do you want to do?
[A]: Inspect the door
[B]: Drop the suspicion
'''
                    printText(text7)
                    run4 = False
                    run5 = True
                    while run5:
                        printText(text8)
                        input5 = input().upper()
                        if input5 == 'A':
                            text9 = '''
While she's in the bathroom, you inspect the locked door. You walk towards the door and notice a small hole in the door.
You peep through the hole and see what's behind the door. You gasp and jump back as you see what is behind the door.
Behind the door are two skeletons with a large painting of Eli's mom and dad.
"This is crazy." You say to yourself.
"Yes it is."
You spin around, startled, to find Eli standing right behind you, wielding a knife.
"Whoa, ELi! What are you doing with that?" You scream.
"You just couldn't mind your business, could you?" She says.
"I'm sorry! I swear I'll forget everything!" You beg.
"And you were such a nice guy. I'll actually miss you." She says.
"Eli, noooooooo!!!" You shout.
With tremendous speed, Eli impales you with the knife. You fall to the ground, bleeding profusely, coughing out blood.
In a moment, you are dead.
'''
                            printText(text9)
                            dead()
                            run5 = False
                        elif input5 == 'B':
                            printText("You let go of the suspicion and curiousity you have./nEli comes back from the bathroom.")
                            chooseCosplay()
                            run5 = False
                        else:
                            printText("I don't understand. Please select A or B.\n")
                            run5 = True
                elif input4 == 'C':
                    printText("You don't comment about the things you noticed.")
                    chooseCosplay()
                    run4 = False
                else:
                    print("I don't understand. Please select A, B, or C.\n")
                    run4 = True
        else:
            print("I don't understand. Please select A or B.\n")
            run2 = True

def mapHouseMei(): # Mei's House map
    global likeMeter
    global food
    global alreadyInside

    if alreadyInside == True:
        printText('''
"So..." You say. "I heard that you have a realy cool cosplay collection. Would it be cool if I see it, since I'm already here?"
Excitement flashes in her eyes, and she says, "Sure! That'll be great!"
"Awesome!" You say.
''')
    if alreadyInside == False:
        printText('''
It's 5 PM and you knock on Mei's door. Mei opens the door and says, "Hey! Come in!"
"Hey, how's it going?" You say as you walk inside her house

''')

    text1 = '''
"Hey, Mei." You say. "I brought some ''' + food + ''' for us to eat."
You raise up a plastic bag with the food you bought.
"Oh that's great! Why'd you buy all that though?" She says.
[A]: Say, "We could have dinner and call it our little first date."
[B]: Say, "Just in case we got hungry."
'''
    run1 = True
    while run1:
        printText(text1)
        input1 = input().upper()
        if input1 == 'A':
            likeMeter += 4
            text2 = '''
"We could have dinner and call it our little first date." You say, with a little smirk.
Mei smiles hysterically and says, "Awn that's so cute. You sure do know you to woo a lady."
"I try, I try." You say jokingly.
Both of you laugh, as Mei takes the plastic bag and sets it down on a table.
'''
            printText(text2)
            run1 = False
        elif input1 == 'B':
            likeMeter += 1
            text3 = '''
"Just in case we got hungry." You say.
"Oh, well I guess you come prepared." She says jokingly.
Both of you laugh, as Mei takes the plastic bag and sets it down on a table.
'''
            printText(text3)
            run1 = False
        else:
            printText("I don't understand. Please select A or B.\n")
            run1 = True
            
    chooseCosplay()

def dinner(): # Dinner with Mei/Eli at their house, usually happens if you choose the wrong anime to cosplay from. A chance to recover and win her heart again, or still lose it
    global likeMeter
    global food
    global girl

    text1 = '''
The two of you go into the dining room. You take out the ''' + food + ''' and set them on the table. Both of you then start
eating, without speaking for a long period of time. To break the awkward silence, what do you want to say?
[A]: Say, "I guess this is our first date."
[B]: Say, "This food tastes great."
'''
    run1 = True
    while run1:
        printText(text1)
        input1 = input().upper()
        if input1 == 'A':
            if likeMeter >= 10:
                text2 = '''
"I guess this is our first date." You say with a little giggle.
She laughs, and even blushes a little. She drops her fork, and looks you in the eye.
"If this is our first date, then let's finish it in style." She says, while leaning toward you.
She gives you a passionate kiss, and you return the kiss.
"Can we have a second date sometime?" You ask.
"Most definitely." She says, smiling.
'''
                printText(text2)
                if girl == 'A':
                    win()
                    run1 = False
                if girl == 'B':
                    loseWrongGirl()
                    run1 = False
            else:
                text3 = '''
"I guess this is our first date." You say with a little giggle.
She laughs and says jokingly, "Yeah! So cute!"
You laugh. The awkward silence continues.
Eventually, she looks at the clock and says, "I think it's getting late. I think you should start heading home."
She gets up and clears the table. You leave her house.
'''
                printText(text3)
                loseFailedToWoo()
                run1 = False
        elif input1 == 'B':
            text4 = '''
"This food tastes great." You say.
"Yeah, thanks for bringing it." She says.
The awkward silence continues.
Eventually, she looks at the clock and says, "I think it's getting late. I think you should start heading home."
She gets up and clears the table. You leave her house.
'''
            printText(text4)
            loseFailedToWoo()
            run1 = False
        else:
            printText("I don't understand. Please select A or B.\n")

def securedDoor(): # Ask Eli about the locked door in her room/living room. A chance to either win or lose her heart
    global likeMeter

    text1 = '''
"Eli, what's up with that locked door?" You ask.
Her eyes widen and she seems to get nervous.
"Oh, it's nothing. Just nothing." She says nervously.
She's definitely hiding something. What do you want to do?
[A]: Confess to her and convince her to trust you
[B]: Drop the subject
'''
    run1 = True
    while run1:
        printText(text1)
        input1 = input().upper()
        if input1 == 'A':
            likeMeter += 2
            text2 = '''
"Eli, trust me." You say. "To be honest, I really like you and I have for a while. I've always wanted to get closer to you
and mean somthing to you. I know you're hiding something, and I don't know if you have anyone to tell it to. But I want
you to know that you can trust me. No matter what is behind that door, I won't judge you or leave you; I'll stay right by
your side. There's something special inside you, and I only want to help you. You can trust me, Eli. I'll stay by your side
no matter what."
'''
            printText(text2)
            if likeMeter >= 13:
                text3 = '''
Eli's face turns bright red. A tear drops from her eye.
"Okay." She says softly.
Slowly, she turns and leads you to the locked door. She grabs a key from a drawer and unlocks the door.
"Here." She says as she opens the door.
Eli opens the door, and your eyes widen as you see what's behind the door. Behind the door are two skeletons and a large painting
of what seem to be Eli's parents.
"What's this?" You ask, shocked.
"It was all my fault!" She cries.
You quickly pull her into a hug, and caress her fair, telling her to calm down.
"Don't worry, Eli. I'm here, I'm here. I'm not going anywhere. I'm right here for you." You say soothingly.
She lifts her head, and slowly leans towards yours. She gives you a passionate kiss, and you return the kiss.
"Thank you so much." She sobs.
'''
                printText(text3)
                win()
                run1 = False
            else:
                text4 = '''
Eli takes a few steps back.
"No, no, no. Kosuke, this isn't what I wanted. I'm not looking to get into a relationship, and all of this is moving just too fast!
I have my problems that I need to sort out; I don't want to involve you in this." She says.
"Eli-" You start.
"No, Kosuke. I think you should go home now." She says. "Please."
You sigh, and slowly turn around and leave, defeated.
'''
                printText(text4)
                loseFailedToWoo()
                run1 = False
        elif input1 == 'B':
            printText("You drop the subject, much to Eli's relief.")
            chooseCosplay()
            run1 = False
        else:
            print("I don't understand. Please select A or B.")
            run1 = True

def win(): # Text to display if player wins the game
    text = '''

You won Eli's heart! The two of you continue to have a relationship as you help her with her problem and help her recover...

Moments after kissing her, a large, black demonic figure emerges from her chest.
"Curse you, boy!" It bellows as it fades into nothingness.
It looks like Eli was the girl with the demon in her heart, and you just exterminated that demon. In 2033 and beyond, Earth
does not fall under attack, and everyone is safe.
You have saved humanity.
'''
    time.sleep(1)
    print("----------------------------------------------------------------------------------------------------------------------------")
    printText(text)

def loseWrongGirl(): # Text to display if player wins the heart of the wrong girl (Mei)
    text = '''

You won Mei's heart! The two of you continue to have a relationship and eventually get married...

One day in 2033, you and Mei are taking a walk in the park. All of a sudden, you hear a huge explosion. A large, black
demonic figure appears and soars above the buildings. The demon has the face of Eli, but soon Eli's face is engulfed in
darkness. The demon bellows and releases a furnace into all directions. You and Mei try to run, but its flames reach the
park and burn everything.
"Meeeeeiiiiii!!!!" You shout, burning in anguish.
"Kosuke, I love you!" Mei screams what would be her final words.
You watch the love of your life die, and you die next to her. Everyone dies in this merciless attack and Eartb becomes
nothing but ashes.
You have failed humanity.
'''
    time.sleep(1)
    print("--------------------------------------------------------------------------------------------------------------------------")
    printText(text)

def loseFailedToWoo(): # Text to display if player fails to win the heart of any girl
    text = '''

You failed to win her heart...

One day in 2033, you are taking a walk in the park. All of a sudden, you hear a huge explosion. A large, black
demon appears and soars above the buildings. The demon has the face of Eli, but soon Eli's face is engulfed in
darkness. The demon bellows and releases a furnace into all directions. You try to run, but its flames reach the
park and burn everything. You are caught in the flames and die, along with everyone else on the face of the planet.
You have failed humanity.
'''
    time.sleep(1)
    print("----------------------------------------------------------------------------------------------------------------------")
    printText(text)

def dead(): # Text to display if player dies
    text = '''

You are dead...

In 2033, Earth falls under attack. A huge demon emerges and bruns everything, killing everyone. There were no survivors
in this massive onslaught. Earth is now a desolate planet.
You have failed humanity.
'''
    time.sleep(1)
    print("-------------------------------------------------------------------------------------------------------------------------")
    printText(text)

# Run the game
runGame = True
while runGame:
    intro()
    mapOne()
    time.sleep(1)
    printText("\nWould you like to play again?\n[A]: Yes\n[B]: No\n")
    runPlayAgain = True
    while runPlayAgain: # Ask player to play again
        playAgain = input().upper()
        if playAgain == 'A' or playAgain == 'YES':
            # Play again
            likeMeter = 0
            girl = ''
            alreadyInside = False
            food = ''
            runPlayAgain = False
            runGame = True            
        elif playAgain == 'B' or playAgain == 'NO':
            runGame = False
            runPlayAgain = False # Quit game
        else:
            printText("Please select A or B.\n")
            runPlayAgain = True
