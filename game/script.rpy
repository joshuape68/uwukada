# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narrator", who_color="#99ffcc")#mint
define y = Character("You")
define c = Character("Cheng-Hau", who_color="#b3b3b3")#gray
define j = Character("Jihyeon", who_color="#ffcc00")#yellow
define jp = Character("Josh", who_color="#ff4d4d")#red
define m = Character("Manisha", who_color="#6666cc")#purple-blue
define p = Character("Pao", who_color="#5cd65c")#green
define h = Character("Huanvy", who_color="#1ad1ff")#blue
define d = Character("Edwin", who_color="#df80ff")#purple
define ys = Character("Ysabel", who_color="#ff9933")#orange

init python:
    #Progress_One is for if the player has successfully interacted.
    #The flag turns true to allow for progress in the next section
    Jihyeon_Progress_One = False
    Manisha_Progress_One = False
    Cheng_Hau_Progress_One = False
    Pao_Progress_One = False
    Edwin_Progress_One = False
    Ysabel_Progress_One = False
    Huanvy_Progress_One = False

    #These are flags for if a person has interacted completely through
    #the interaction with a character, whether they went through the
    #positive route or not
    Jihyeon_Part_One = False
    Manisha_Part_One = False
    Cheng_Hau_Part_One = False
    Pao_Part_One = False
    Edwin_Part_One = False
    Ysabel_Part_One = False
    Huanvy_Part_One = False

    #These are for introductions of people who haven't been introduced
    #yet in label start
    Jihyeon_Introduction_Dialogue = False
    Manisha_Introduction_Dialogue = False
    Pao_Introduction_Dialogue = False
    Ysabel_Introduction_Dialogue = False

    #Successful interaction in part two, for part three
    Jihyeon_Progress_Two = False
    Manisha_Progress_Two = False
    Cheng_Hau_Progress_Two = False
    Pao_Progress_Two = False
    Edwin_Progress_Two = False
    Ysabel_Progress_Two = False
    Huanvy_Progress_Two = False

    #Any interaction in part two
    Jihyeon_Part_Two = False
    Manisha_Part_Two = False
    Cheng_Hau_Part_Two = False
    Pao_Part_Two = False
    Edwin_Part_Two = False
    Ysabel_Part_Two = False
    Huanvy_Part_Two = False

    #Intro to interaction two
    Huanvy_Part_Two_Intro = False
    Edwin_Part_Two_Intro = False
    Manisha_Part_Two_Intro = False
    Jihyeon_Part_Two_Intro = False
    Ysabel_Part_Two_Intro = False
    Pao_Part_Two_Intro = False
    Cheng_Hau_Part_Two_Intro = False


# The game starts here.

label start:
    scene stanford
    with dissolve
    n "This is your first day at Stanford University!"
    n "You're so excited to be on campus finally,
        and you can't wait to meet all the cool people here!"
    scene okaka lounge
    with dissolve
    y "Wow, this dorm is quite lovely! I love the theme!"
    show cheng hau
    with dissolve
    c "Hi there! Welcome to Okada, I’m your RA Cheng Hau, and I use they/them pronouns."
    c "You must be?"
    python:
        name = renpy.input("My name is...")
        pronouns = renpy.input("My pronouns are...")
    y "Hi I'm [name] and I use [pronouns] pronouns. It's nice to meet me, I mean you! Ahhh!!!
        I messed up already."
    show huanvy at right
    with dissolve
    h "Mood."
    show edwin at left
    with dissolve
    d "Y = mx + it be like that sometimes *hehe*"
    c "*cute laugh* Nice to meet you [name]."
    h "I'm Huanvy and I use they/them pronouns. I'm one of the ethnic theme associates."
    d "I'm Edwin and I use he/him prnouns. I'm also an ETA. Welcome to Okada [name]."
    scene black
    with dissolve
    n "The staff are so super duper cool! And all very attractive ;)."
    n "You should head up to your room and unpack."
    scene room
    with dissolve
    y "Ahhh, finally finished unpacking."
    n "It is now night time, and you decide to explore around the dorm."



    #This label first_night has the menu for the options of where to go
    label first_night:
        if Jihyeon_Part_One == True or Manisha_Part_One == True or Cheng_Hau_Part_One == True or Pao_Part_One == True or Edwin_Part_One == True or Ysabel_Part_One == True or Huanvy_Part_One == True:
                scene room
                with dissolve
                y "What should I do now?"
        menu:
            "Where should I go?"
            "2nd Floor":
                jump .Second_Floor_first_night
            "1st Floor":
                jump .First_Floor_first_night
            "Courtyard":
                jump .Courtyard_first_night
            "I should go to bed":
                jump .Bed_first_night
        #This label Second_Floor_first_night has the options for Jihyeon
        #Manisha, or just going back to the first_night menu
        label .Second_Floor_first_night:
            scene second_floor
            with dissolve
            menu:
                "You hear someone singing Girls Generation" if Jihyeon_Part_One == False:
                    jump .Jihyeon_first_night
                "You hear Punjabi music playing" if Manisha_Part_One == False:
                    jump .Manisha_first_night
                "Go back":
                    jump first_night

        #This label Jihyeon_first_night has the Jihyeon interaction
        label .Jihyeon_first_night:
            scene jihyeon_door
            with dissolve
            n "You check out the room that the singing is coming from"
            scene jihyeon_room
            show jihyeon
            with dissolve
            #This is vital to ensuring that a person introduces only 1 time
            if Jihyeon_Introduction_Dialogue == False:
                j "Oh hi I'm the RCC Jihyeon and I use she/her pronouns"
                y "Oh hi I'm [name] and I use [pronouns] pronouns"
                $ Jihyeon_Introduction_Dialogue = True
            j "Do you want to come in?"
            menu:
                "Yes":
                    y "Ok sure"
                    jump .Yes
                #Saying no doesn't lock people out
                "No":
                    y "No thank you."
                    j "Alright. I'll see you later"
                    jump first_night
            label .Yes:
                j "Have a seat. I was just singing some Girls Generation"
                menu:
                    "I love K-pop":
                        jump .I_Love_K_Pop
                    "Oh, K-pop is lame":
                        jump .K_Pop_Is_Lame
            #This is the good line that allows people to progress Jihyeon
            label .I_Love_K_Pop:
                y "I love K-Pop"
                j "Oh my gosh what's your favorite artist?"
                $ fav_k_pop = renpy.input("What's your favorite artist?")
                y "My favorite artist is [fav_k_pop]."
                j "Oh my gosh I love [fav_k_pop] too."
                j "Do you want to watch music videos right now?"
                y "Yes!!!"
                scene black
                with dissolve
                n "You watch music videos for 2 hours, laughing, giggling, and having fun."
                scene jihyeon_room
                show jihyeon
                with dissolve
                j "Hey this was really fun. We should do this again sometime."
                y "Yeah it was."
                #This flag turns True allowing for progress
                $ Jihyeon_Progress_One = True
                $ Jihyeon_Part_One = True
                jump first_night

            #This is one of the bad lines that lock people out of Jihyeon
            label .K_Pop_Is_Lame:
                j "Oh okay. What do you like?"
                $ jihyeon_I_Like = renpy.input("I like")
                y "I like [jihyeon_I_Like]"
                j "Oh yeah, that's cool."
                n "There's an awkward silence"
                j "Hey I thinking I'm going to sleep soon"
                y "Ok"
                $ Jihyeon_Part_One = True
                jump first_night

        #This label Manisha_first_night is the first interaction with Manisha
        label .Manisha_first_night:
            scene manisha_door
            with dissolve
            n "You go to the room that the music is playing from."
            scene manisha_room
            show manisha
            with dissolve
            if Manisha_Introduction_Dialogue == False:
                m "Oh hey I'm Manisha and I use she/her pronouns."
                y "I'm [name] and I use [pronouns] pronouns."
                m "I was just practicing for my bhangra performance."
                $ Manisha_Introduction_Dialogue = True
            m "Do you want to come in?"
            menu:
                "Yes":
                    jump .yes
                "No thanks":
                    y "No thanks."
                    jump first_night
            #Good progression
            label .yes:
                y "Yes."
                m "Hey do you want to see me dance?"
                menu:
                    "Yeah that'd be cool!":
                        jump .thatd_be_cool
                    "No thanks":
                        jump .no_dance
            label .thatd_be_cool:
                y "Yeah that'd be cool!"
                m "Here let me just turn the music back on *turns music on*"
                n "*Manisha dances*"
                y "Wow you're really good at dancing."
                m "Thanks. Hey do you want to learn some steps?"
                y "Sure I'd love to!"
                m "Great *hehe*"
                scene black
                with dissolve
                n "*Manisha shows you some steps and you two dance together*"
                scene manisha_room
                show manisha
                with dissolve
                y "Wow that was really fun."
                m "Yeah that was. You're a good dancer. We should dance again sometime."
                $ Manisha_Progress_One = True
                $ Manisha_Part_One = True
                jump first_night
            #Bad progression
            label .no_dance:
                m "Oh okay. Well I need to practice some more so...."
                y "Yeah alright, I'll leave."
                $ Manisha_Part_One = True
                jump first_night

        label .First_Floor_first_night:
            scene first_floor
            with dissolve
            menu:
                "You feel drawn to some wise aura" if Pao_Part_One == False:
                    jump Pao_first_night
                "You hear the sound of clacking coming from the lounge" if Edwin_Part_One == False:
                    jump Edwin_first_night
                "You smell spam being fried from the kitchenette" if Cheng_Hau_Part_One == False:
                    jump Cheng_Hau_first_night
                "Go back":
                    jump first_night
        label .Pao_first_night:
        label .Edwin_first_night:
        label .Cheng_Hau_first_night:

        label .Courtyard_first_night:
            scene courtyard_1
            with dissolve
            menu:
                "You see someone flyering" if Huanvy_Part_One == False:
                    jump .Huanvy_first_night
                "You feel the vibrations of someone wiggling" if Ysabel_Part_One == False:
                    jump .Ysabel_first_night
                "Go back":
                    jump first_night

        label .Huanvy_first_night:
            show huanvy
            with dissolve
            h "Oh hey [name] I'm flyering for the Equity for ETAs campaign."
            menu:
                "Can I help out?":
                    jump .Huanvy_Can_I_Help_Out
                "Oh that's cool (Keep Walking)":
                    jump .Courtyard_first_night
            label .Huanvy_Can_I_Help_Out:
                h "Oh yeah that'd be great. Here's a stack of flyers"
                y "Oh I see I see this is interesting. Wait Stanford only pays you $4200?"
                h "Yeah Stanford doesn't care about the labor of people of color."
                menu:
                    "I agree":
                        jump .I_agree
                    "That's a leap of logic":
                        jump .leap_logic
            label .I_agree:
                y "I agree."
                h "Yeah Stanford is... questionable. I'll leave it at that."
                y "Yeah. So why are you an ETA if you get paid so little?"
                h "Well even though I and other ETAs don't get paid enough,
                    we still care about what we do as ETAs."
                y "Wow I see."
                h "Yeah. Ethnic theme dorms like Okada wouldn't be the same
                    space if ETAs didn't exist."
                y "Yeah they're really important it seems like."
                h "Alright let's go over to ...there to flyer"
                scene black
                with dissolve
                n "You and Huanvy put up posters for a while."
                scene courtyard_1
                show huanvy
                with dissolve
                h "Wow thank you so much."
                y "Yeah no problem. It was a good time."
                h "Have a good night."
                y "You too."
                $ Huanvy_Progress_One = True
                $ Huanvy_Part_One = True
                jump first_night
            label .leap_logic:
                y "That's a leap of logic."
                h "...Yeah...I guess."
                y "Alright, where should we flyer?"
                h "Actually, I think I can flyer by myself."
                y "Oh, have a good night."
                h "Night."
                $ Huanvy_Part_One = True
                jump first_night

        label .Ysabel_first_night:
            n "You check out the hip-hop music and wiggling."
            scene courtyard_2
            show ysabel
            with dissolve
            if Ysabel_Introduction_Dialogue == False:
                ys "Wassupp I'm Ysabel Ojoylan and I use she/her pronouns"
                y "Hi I'm [name] and I use [pronouns] pronouns."
                ys "*Keeps dancing*"
                $ Ysabel_Introduction_Dialogue = True
            menu:
                "Oh wow you're a good dancer":
                    y "Oh wow you're a good dancer."
                    jump .good_dancer
                "I'm going to keep walking":
                    jump first_night
            label .good_dancer:
                ys "Thanks. I've been dancing for two years.
                        I'm in Kayu, CO, XTRM, and FFS."
                y "Oh that's super cool."
                ys "Hey do you want to learn how to body roll?"
                menu:
                    "Sure":
                        y "Sure."
                        jump .body_roll
                    "No thanks":
                        y "No thanks."
                        jump .no_body_roll
            label .body_roll:
                ys "Awesome."
                y "Alright, what should I do?"
                ys "Alright, so move your head, then chest, then stomach, then hips, then legs.
                    Like this."
                y "Wow that's super complicated."
                ys "It's not that bad. Give it a try."
                y "Ok yeah."
                n "You try a body roll and fail."
                ys "*giggles* alright let's work on it some more."
                scene black
                with dissolve
                n "You work on your body rolls with Ysabel."
                ys "Hey you got it!"
                y "Oh wow."
                scene courtyard_2
                show ysabel
                with dissolve
                ys "Hey you've made some good progress. You should go to
                    a dance workshop with me sometime."
                y "Yeah that was fun, and I think I will."
                $ Ysabel_Progress_One = True
                jump first_night
            label .no_body_roll:
                ys "Oh alright. Well I have to keep practicing."
                y "Alright. I'll see you later I guess."
                jump first_night

        label .Bed_first_night:
            scene room
            with dissolve
            n "You decide to go to bed."
            jump part_two_intro

label part_two_intro:
    scene black
    with dissolve
    n "NSO ended so soon. Then classes started immediately."
    n "You get caught up in classes and activities and applications and oh my."
    n "Time flies so quickly."
    scene fall leaves
    with dissolve
    n "It is Week 8 of Autumn Quarter."
    n "You're deep in the trench of midterms and papers. When will it end?"
    n "You decide you need to get out of your room and go somewhere."
    n "But where?"
    jump part_two

label part_two:
    scene room
    with dissolve
    menu:
        "Where should you go?"
        "East Campus/Around Okada":
            jump .east_okada
        "Central Campus":
            jump .central
        "West Campus":
            jump .west

    #Pao, Cheng Hau, and Manisha
    label .east_okada:
        $ Visit_East_Okada = True
        scene okada outside
        with dissolve
        menu:
            "You see someone coming back with art supplies" if Pao_Progress_One == True:
                jump .Pao_Part_Two
            "You see someone coming back with many bags from IKEA" if Cheng_Hau_Progress_One == True:
                jump .Cheng_Hau_Part_Two
            "You see someone walking out towards some nature" if Manisha_Progress_One == True:
                jump .Manisha_Part_Two
            "Go Back":
                jump part_two

    #Ysabel and Jihyeon
    label .west:
        $ Visit_West = True
        scene west campus
        with dissolve
        menu:
            "You see someone wiggling towards Roble Gym" if Ysabel_Progress_One == True:
                jump .Ysabel_Part_Two
            "You see someone walking into a building emanating despair" if Jihyeon_Progress_One == True:
                jump .Jihyeon_Part_Two
            "Go Back":
                jump part_two

    #Huanvy and Edwin
    label .central:
        $ Visit_Central = True
        scene central campus
        with dissolve
        menu:
            "You see someone with Pidgeotto hair walking down campus drive" if Huanvy_Progress_One == True:
                jump .Huanvy_Part_Two
            "You see someone singing \"thank u, next\" walking towards Jordan Hall":
                jump .Edwin_Part_Two
            "Go back":
                jump part_two

    label .Huanvy_Part_Two:
        if Huanvy_Part_Two_Intro== False:
            scene palm drive
            show huanvy
            with dissolve
            $ Huanvy_Part_Two_Intro = True
            n "You’d recognize that hair anywhere. It’s Huanvy."
            y "Oh hey Huanvy, where are you heading to?"
            h "Oh hey [name], I’m going to a rave by myself, because Erick flaked on me."
            y "Wow I’ve never been to a rave before. Well have fun!"
            n "(You’re secretly hoping that they’ll invite you to go with them."
            h "Hey what are you doing today?"
            y "Oh?"
            h "I have an extra ticket. Do you want to go?"
            menu:
                "Yes":
                    jump .yes
                "No thanks":
                    jump part_two
        h "Oh hey did you change your mind and want to go?"
        menu:
            "I'd like to go":
                jump .yes
            "It's still a no":
                jump part_two

        label .yes:
            $ Huanvy_Part_Two = True
            y "Yes."
            h "Cool, but wait don’t you have a paper or something?"
            y "Yeah… but I’d rather write this memory with you than that paper."
            scene black
            with dissolve
            n "You and Huanvy ride the Caltrain and get to the venue."
            scene rave
            show huanvy
            with dissolve
            y "Wow this is super cool"
            n "The EDM is shaking your body. You see people going wild including many
                    ABGs and AFBs."
            n "*You feel uncomfortable from the sweat in the air and intoxicated people.
                Your only source of comfort is in Huanvy."
            h "Yoooo this is LIT!!!!!"
            y "Y-yeah!"
            h "Hey how are you feeling?"
            menu:
                "th-this is fun…":
                    jump .fun
                "Actually… I feel uncomfortable":
                    jump .uncomfortable
        label .fun:
            y "th-this is fun…"
            h "I’m glad you came."
            y "Yeah I’m glad I did too."
            n "*You spend the rest of the night watching Huanvy go wild as you try to
            navigate the chaos of the rave"
            scene black
            with dissolve
            y "*After the rave ends you and Huanvy ride the Caltrain back.
                You weren’t comfortable at the rave, but it was an experience."
        label .uncomfortable:
            y "Actually… I feel uncomfortable"
            h "Thanks [name] for being honest. Hey let’s go elsewhere. I know a good
            place that’s more quiet."
            y "Ok thank you"
            n "*Huanvy leads you out the venue and calls a ride-sharing service. You two
                go to a park."
            y "Oh this is quite nice."
            h "Yeah I come to Twin Peaks a lot when I’m emo."
            y "Wow there’s so many lights"
            h "Yeah it’s super nice."
            menu:
                "Huanvy looks nice with the lights of the city softly glowing on their face. Your heart is beating faster"
                "I have something to tell you":
                    jump .tell_you_Huanvy
                "Don’t say anything":
                    jump .dont_say
        label .dont_say:
            n "*You and Huanvy enjoy the view, making small talk."
            h "Hey it’s getting pretty late. Are you ready to go back?"
            menu:
                "I have something to tell you":
                    "Wait can we stay a little longer?"
                    jump .tell_you_Huanvy
                "Yeah let’s go back":
                    jump .lets_go_back
            label .tell_you_Huanvy:
                y "I have something to tell you"
                h "Yeah?"
                y "I like you."
                h "Hello???"
                y "Oh sorry, I know that we can’t be anything, but I needed to say that."
                h "Ok. Well I have something to tell you too."
                y "Yeah?"
                h "I like you too, but this can’t be anything."
                y "Yeah..."
                y "Hey, can we hold hands?"
                h "Yeah, I’d like that."
                scene black
                with dissolve
                n "You two hold hands for a while, admiring the view."
                h "Are you ready to go back?"
                y "Yeah"
                $ Huanvy_Part_Two_Progress = True
                jump part_two
        label .lets_go_back:
            y "Yeah let’s go back."
            n "*You and Huanvy take a ride-sharing service.*"
            n "*You and Huanvy are sitting in the back together.*"
            scene black
            with dissolve
            n "*You can’t help but feel that in the foot of distance between you and
            Huanvy that there exists an infinite distance of longing*"
            jump part_two

    label .Edwin_Part_Two:
        if Edwin_Part_Two_Intro == False:
            $ Edwin_Part_Two_Intro = True
            n "When you get closer you see that it’s Edwin"
            y "Hey Edwin!"
            d "Hey [name]! What are you up to?"
            y "Oh nothing much. I saw you and was wondering if you wanted to hang"
            d "Actually I have my Psych office hours right now, but if you’re willing to wait until it ends"
            menu:
                "Yeah I’ll wait":
                    jump .wait
                "Actually I’ll catch you around later":
                    jump part_two
        d "Did you change your mind?"
        menu:
            "Yes":
                jump .wait
            "I'll catch you around later":
                jump part_two

        label .wait:
            $ Edwin_Part_Two = True
            d "Ok great."
            n "*You and Edwin walk to his office hours and he gets set up.*"
            d "It should only be an hour."
            y "Alright cool."
            n "*At first his office hours are slow and you have time to chat. Then the
                crowd of people starts to grow. Edwin is super busy, but he’s in the
                zone and you can’t help but admire that. He helps everyone with such
                understanding- how is he so smart AND kind?"
            n "*An hour passes by."
            d "Hey sorry [name] but one of my co-TFs needs their shift covered. Do you
                think you could wait another hour?"
            menu:
                "I’m gonna leave.":
                    y "I’m gonna leave."
                    d "Alright, sorry [name] once again."
                    jump part_two
                "Yeah I can wait.":
                    n "*You have more immediate things to do, but you also want to
                        be by Edwin."
            n "*Although Edwin is going back to back on shifts, he still manages to keep
                up his energy and kindness. How is this possible?*"
            n "*Another hour passes. He’s finally finished.*"
            d "Okay thank you for waiting. So what do you want to do?"
            y "It’s up to you."
            d "How about we go study at a coffee shop off-campus?"
            y "Sure"
            d "Alright I’ll Slack that we’re going to off-campus to see if anyone else
                wants to come with."
            menu:
                "Alright":
                    jump .alright
                "What if we go by ourselves?":
                    jump .ourselves
        label .alright:
            y "Alright."
            d "Alright just sent it."
            d "It looks like Saw, Josh, and Michael want to go with us."
            n "*You and Edwin head back to Okada and meet up with the others. Then
                You all drive to an off-campus coffee shop."
            n "*You stay for a couple hours all hard at work studying."
            jump part_two

        label .ourselves:
            y "How about we go by ourselves?"
            d "*Edwin smirks at you* I like that idea too actually."
            n "*Edwin gets his car and you all drive to an off-campus coffee shop. It’s
                very packed and the line is long."
            y "Oh this shop is cute."
            d "Yeah it’s my favorite one."
            d "Here let’s go wait in line."
            n "*You two wait in line for a bit. You get to the front and the barista asks
                for your order.*"
            $ coffee_order = renpy.input("What do you want to order?")
            y "I’ll have an [coffee_order]."
            define b = ("Barista")
            b "That’ll be $4.95."
            y "Ok here. *Searches for wallet.*"
            y "Oh sorry it looks like I don’t have my wallet. Can you cancel my order?"
            d "Here I’ll pay for you."
            y "Oh no you don’t have to."
            d "No, but I want to."
            y "Thanks."
            d "Hey let’s sit over here."
            n "*You two sit and start working. You notice that there are many couples in
            here, holding hands and being affectionate.*"
            y "Look at all these couples, how cute. I wish I had that right now."
            n "*You lock eyes with Edwin, and forget to look away*"
            menu:
                "Look away":
                    jump .look_away
                "Keep looking":
                    jump .keep_looking

        label .look_away:
            y "Sorry, I should get back to work."
            d "Y-yeah, me too."
            n "*You two work for a while. Eventually the shop closes and head back to
                Okada. It was a productive day."
            jump part_two

        label .keep_looking:
            d "I never noticed before, but you have beautiful eyes."
            n "*Your heart beats faster, but you can’t look away."
            menu:
                "I have something to tell you":
                    jump .something
                "You have something in your teeth":
                    jump .teeth

        label .something:
            y "I like you, Edwin."
            n "*Edwin puts his hand on yours. You blush immensely*"
            d "I like you too, but this can’t be"
            y "I know…"
            n "*You both get back to work, sitting extremely closely together.
                You can’t focus on your work, but you try your best. Eventually the shop
                closes and you head back to the dorm"
            $ Edwin_Progress_Two = True
            jump part_two

        label .teeth:
            y "You have something in your teeth."
            d "Oh, thanks for telling me."
            n "You both get back to work for a couple hours. The shop closes
                eventually, and then you head back to the dorm."
            jump part_two

    label .Manisha_Part_Two:
        if Manisha_Part_Two_Intro == False:
            n "You get closer and you see that it’s Manisha"
            y "Manisha!"
            m "Hey [name]. What are you up to?"
            y "Oh nothing much. What are you doing?"
            m "I’m going to Jasper Ridge to do field work."
            y "Oh cool."
            m "Hey do you want to come along and help me?"
            menu:
                "Sure":
                    "Sure."
                    jump .sure
                "No thanks":
                    "No thanks."
                    jump part_two
        m "Did you change your mind?"
        menu:
            "Yes":
                y "Yes."
                jump .sure
            "No":
                y "No thanks."
                jump part_two

        label .sure:
            $ Manisha_Part_Two = True
            m "Alright great."
            n "*You and Manisha walk towards Jasper Ridge."
            y "Oh wow it’s so nice to get into some actual nature."
            m "Yeah I love coming out here."
            y "So what are we doing?"
            m "I need to collect samples of water from the different streams to test
            them in the lab."
            m "One person needs to jump into the stream and collect the water, the other person waits at the bank and organizes the samples."
        menu:
            "I can jump into the streams":
                jump .stream
            "I can wait on the side":
                jump .on_side

        label .on_side:
            y "I can wait on the side."
            m "Oh alright."
            n "Manisha jumps in."
            y "Alright here’s the vial *Tries to hand Manisha vial*"
            n "Manisha pulls out vial from pocket"
            m "Actually I already have vials on me."
            y "Ok here hand me the vial when your done collecting."
            n "Manisha pulls herself out the stream and organizes the vial herself"
            m "Oh I got it."
            y "You sure?"
            m "Yeah don’t worry."
            n "Manisha works on collecting all the samples while you just stand
                around. There’s no cell service out in Jasper Ridge so all you
                can do is stand in the silence as Manisha works."
            m "Alright, we're done."
            y "Okay."
            m "Thanks for the help."
            y "Yeah."
            jump part_two

        label .stream:
            y "I can jump into the streams."
            m "Alright great! Here are some rain boots you can change into."
            y "Alright yeah. How do I do this?"
            m "Jump into the stream, and I’ll hand you a vial. Then dip the vial into
                the stream and screw the cap on while the vial is under water."
            y "Alright that doesn’t sound too bad."
            n "*You jump into the stream. Although you’re wearing rain boots, your pants get soaked.*"
            y "Ahh I’m wet."
            m "Oh my gosh are you ok?"
            n "*You aren’t ok*"
            y "Yes I’m ok."
            m "Ok good. Here’s the vial."
            y "Alright I got you. *collects water and hands the vial back to Manisha*"
            m "Alright perfect, one down, 39 more to go."
            menu:
                "What?!?!?":
                    jump .what
                "39 more!!!":
                    jump .more
        label .what:
            y "What?!?!? 39 more?!?!?!?"
            m "Yeah but we can switch off halfway through or something."
            menu:
                "Can we switch now?":
                    jump .switch
                "Oh no I can do the whole thing":
                    y "Oh no I can do the whole thing"
                    jump .more
        label .switch:
            y "Can we switch now? My pants got wet and I’m freezing."
            m "Oh alright yeah I got it."
            n "You two head to the next test location and Manisha jumps into the
                stream."
            y "Alright here’s the vial *Tries to hand Manisha vial*"
            n "Manisha ulls out vial from pocket."
            m "Actually I already have vials on me."
            y "Ok here hand me the vial when your done collecting."
            n "Manisha pulls herself out the stream and organizes the vial herself"
            m "Oh I got it."
            y "You sure?"
            m "Yeah don’t worry."
            n "Manisha works on collecting all the samples while you just stand
                around. There’s no cell service out in Jasper Ridge so all you
                can do is stand in the silence as Manisha works."
            m "Alright, we're done."
            y "Okay."
            m "Thanks for the help."
            y "Yeah."
            jump part_two

        label .more:
            y "Alright let’s continue!"
            m "Thank you so much."
            n "You go to all 39 test locations and jump into the streams. By the
                end you are soaking wet and freezing."
            m "Alright let’s walk back to Okada."
            y "Alright yea--"
            scene black
            with dissolve
            n "You pass out"
            m "Oh my gosh [name]"
            scene white
            with dissolve
            scene manisha_room
            show manisha
            with dissolve
            m "Hey wake up. Wake up."
            y "*drowsily* huh?"
            m "Thank god you’re awake. You passed out. I think you have
                hypothermia."
            y "Oh wow."
            m "You should’ve told me you were freezing cold. I’m so worried about
                you!."
            y "Yeah, it’s just that the first time I jumped into the stream, I got
                wet, and I knew I would get cold, but I didn’t want you to get
                cold too, so I kept on."
            m "You’re so dumb, [name]."
            m "Well, thank you."
            m "I’m making you some soup right now. Do you need anything else?"
            y "No I’m good. Thank you."
            m "Alright the soup should be ready. I’ll go grab you some."
            hide manisha
            with dissolve
            n "Manisha goes to grab the soup."
            show manisha
            with dissolve
            m "Here you go."
            y "Wow this soup is really good."
            m "Thank you."
            y "Hey, these clothes I’m wearing aren’t mine…"
            m "Oh yeah I changed you out of your wet clothes into my brother’s."
            y "Oh so you saw me… naked?"
            m "I mean yeah."
            y "Well this soup is really good."
            m "What else can I do for you?"
            y "I’m good."
            m "No don’t lie to me. Here I know what you need."
            n "Manisha takes some socks and puts them on your feet. Then she
                takes a scarf and wraps it around you gingerly."
            n "As she’s doing this you can’t help but notice how kind and pretty she
                is. Those brown eyes is making your heart beat faster."
            m "There. Now tell me what else you need."
            menu:
                "I need to tell you something":
                    jump .tell_you
                "I need some help getting to my room":
                    jump .room
        label .room:
            y "I need some help getting to my room."
            m "Yeah sure thing."
            scene room
            show manisha
            with dissolve
            n "Manisha helps you down to your room."
            m "Here you are. Good night."
            menu:
                "Wait":
                    y "Wait."
                    m "Yes?"
                    jump .tell_you_Manisha
                "Good night":
                    y "Good night"
                    jump part_two

            label .tell_you_Manisha:
                y "I need to tell you something."
                m "What is it?"
                y "I like you."
                m "[name]...."
                y "I just needed to say that. Since that first night we met and danced
                    together, I’ve been feeling this way."
                m "[name]...."
                y "I know that nothing can happen between us, but I just needed to
                    say that."
                m "[name]... I like you too."
                y "Manisha…."
                m "[name]... but we can’t be together. I’m sorry."
                y "No don’t be sorry. At least we know how we feel about each other."
                m "Yeah."
                y "Well, good night."
                m "Good night."
                $ Manisha_Progress_Two = True
                jump part_two
                n “You go towards them, and you see that it’s Jihyeon”
y “Jihyeon! What are you up to?”
j “Oh hey [name]! I was just going to where people go to die”
y “Oh gosh, thats terrible”
j “I’m kidding, I’m going to Gates to work on my CS assignment. Do you want to join me?”
menu:
“Yes! I’d love to”:
	jump .yes
“NO I’m afraid of dead people”:
	jump .part_two
label .yes
	y “Yes! I’d love to”:
	j “Alright cool. Let’s go!”
	n “You two go down to the basement of Gates. You can feel despair around
		you. But there’s one ray of sunshine. Jihyeon smiles and it lights up the
whole room.”
y “Wow this does feel like death.”
j “*doesn’t respond*”
y “Jihyeon?”
n “Jihyeon is too busy working. Her eyes are glued to her computer screen, and yours are glued to hers.”
y “Well, I should probably start working.”
n “You get deep into work on a pset. But then one problems gets to you. You can’t solve it.”
n “You start to feel the life being drained out of you.”
j “[name], are you ok?”
y “...”
j “[name]? [name]???”
j “Hey let’s get you out of Gates. This environment isn’t doing you any good.”
n “Jihyeon helps carry you and your stuff out. You go to the Forbes Cafe.”
j “[name]?”
y “Yeah?”
j “Ok, it seems like Gates sucked your soul out.”
y “Yeah, I guess so.”
j “Hey I ordered you some laksa. Eat up.”
y “Yeah ok thank you.”
n “You try to lift up the spoon to your mouth, but it falls out. You’re still weak from being drained by Gates.”
	j “Oh my gosh let me help you.”
	menu:
		“If you could”:
			jump .feed_you
		“I can feed myself”
			jump .feed_myself
	label .feed_you
		y “If you could, that’d be amazing. I’m sorry to put you in this odd position
			though….”
		j “Oh no don’t be sorry. I shouldn’t have taken you into Gates.”
		y “Yeah, I probably shouldn’t have gone in. But I wanted to hang out with
			you.”
		j “Aww that’s sweet, [name]. Now here, open your mouth.”
		y “Ahhhhhh”
		j “Here comes the plane! Yum!”
		y “*giggle*”
		j “*giggle*”
		n “You feel your soul coming back into you. Is it because the laksa is
			filling your body, or is it because Jihyeon is feeding your soul?”
		y “Alright that’s the last bite of food.”
		j “Wow thank you. I feel much better.”
		y “Alright let’s get you back to Okada.”
		j “Alright”
		n “You and Jihyeon head back to your room in Okada.”
		j “Alright, will you be ok? I have to go do some work still.”
		n “You look into Jihyeon’s eyes and feel the warmth of the sun. You can’t
			look away.”
		j “Oh no you’re turning into a CS zombie again.”
		menu:
			“I have something to tell you”:
				jump .tell_you_Jihyeon
			“Yeah I need some rest”:
				jump .rest
	label .rest:
		y “Yeah I think I need some rest.”
		j “Well okay. If you need something, I think Ysabel and Scarlett are
somewhere or you can call me. I gotta go.”
y “Yeah ok, thank you. Good bye”
j “Good bye”
		n “You take a nap. In this nap, you have a dream about Jihyeon feeding
			you, and you feeding Jihyeon back. You wake up.”
		menu:
			“Call Jihyeon”:
				jump .tell_you_Jihyeon
			“Go back to sleep”:
				jump .part_two
label .tell_you_Jihyeon:
	y “Jihyeon, I have to tell you something.”
	j “Yes what’s up?”
	y “I…”
	n “You pass out.”
	j “[name]? [name???]
	y “Oh what happened?”
	j “You’re still weak it seems.”
	y “Yeah I guess.”
	j “What did you want to tell me?”
	y “Oh right. I… like you.”
	j “[name]...”
	y “Yeah I know. It’s just that when I’m with you, I feel like a missing part
		of me is whole. You fill me with your kind eyes and your shining
		smile.”
	j “[name]... I like you too.”
	j “But you know we can’t be together.”
	y “Yeah, I know.”
	j “...”
	y “What’s up?”
	j “How about I work in your room? Then I can make sure you don’t pass
		out again.”
	y “Yeah, I’d like that.”
	j “*blushes* ok.”
	n “Jihyeon gets her work out. This time, she’s not as focused on her work
		as she is on you.”
	j “[name] you seem pretty tired. How about you lean on me?”
	y “Yeah that’d be nice.”
	n “Hours pass by and it’s now night.”
	j “Hey [name] I have to go to bed now. It was nice sitting with you.”
	y “It was nice sitting with you too. I feel like what Gates drained out of me,
		you refilled.”
	j “Good night.”
	y “Good night.”
Ysabel
n “You could tell it was Ysabel, but getting closer allowed you to confirm.”
y “Ysabel! What’s up?”
ys “Wazzup [name]! What are you up to?”
y “Oh nothing much. What about you?”
ys “I’m going to a CO workshop. Hey do you want to join?”
menu:
	“Yes”
		jump .yes
	“No thanks”
		y “No thanks”
		jump part_two
label .yes
y “Yes I’d love to!”
ys “Alright cool. We should run it’s getting started soon actually.”
n “You run in and the floor is packed with the 50 other members of CO”
y “Oh hey is that Michael Chang?”
define mc = (“Michael Chang”)
mc “Oh what’s up [name]?”
y “Oh nothing much Ysabel invited me to the workshop.”
mc “Oh cool. Hey it’s pretty packed but there’s some space over there we
	can use.”
menu:
	“Yeah sure”
		jump .michael_chang
	“Actually I should find Ysabel
		jump .find_ysabel
label .michael_chang
	y “Yeah sure.”
	mc “Alright cool.”
	n “You and Michael go to the space and then the workshop begins.”
	y “Wow this is pretty complicated. Michael how are you so good at this?”
	mc “Oh I’m not that good.”
	n “The workshop ends. You’re sweaty but feel accomplished.”
	mc “You want to walk back to Okada together?”
	y “Yeah sure”
	ys “[name]! I’ve been looking all over for you. Where’d you go?”
	y “I saw Michael and I went to dance with him.”
	ys “Oh yeah alright.”
	y “Are you heading back to Okada? Let’s walk together.”
	ys “Actually I have to go to Kayu practice and then Fullout Funk Squad.”
	y “Oh alright.”
	ys “But I’ll catch you later.”
	y “See ya.”
label .find_ysabel:
	y “Actually I should find Ysabel. She invited me to come.”
	mc “Alright I’ll catch you later.”
	n “You go looking for Ysabel. She’s nowhere to be found though.”
	ys “[name]!”
	n “You turn around and see Ysabel.”
	y “Oh Ysabel, I was looking for you.”
	ys “Yeah where did you go? I thought you were following me.”
	y “Oh I saw Michael Chang so I said hi, and then I lost you.”
	ys “Oh alright. I found some space over there, let’s go.”
	y “Alright cool.”
	n “You two make it over and then the workshop starts.”
	y “Wow this is pretty complicated. Ysabel how are you so good at this?”
	ys “Oh I’m just in a perpetual state of wiggling.”
	n “The workshop ends. You feel sweaty but accomplished.”
	y “Wow that was a lot. Are you going to head back to Okada now?”
	ys “Actually I have Kayu practice. Hey do you want to go to that too?”
	menu:
		“Yes”
			jump .kayu
		“No”
			jump .no
label .no:
	y “No thanks, I should probably head back and get some work done.”
	ys “Yeah you should definitely take care of that. Well I’ll catch you around.”
	y “Yeah I’ll see you Ysabel.”
	ys “I’ll see you [name].”
label .kayu
	y “Yeah sure.”
	ys “Awesome! Hurry let’s run to the A3C”
	n “You and Ysabel run over to the A3C. But running was a mistake. You trip
		and fall and twist your ankle.”
	y “OWW!!!”
	ys “Oh my gosh are you ok?”
	y “I think I twisted my ankle.”
	ys Oh my gosh. Let’s get you back to Okada.”
	menu:
		“No I can call a 5sure”:
			jump .fivesure
		“Please”:
			jump .please
label .fivesure
	y “No I can call a 5sure. You should head to Kayu. You’re a co-chair and
		Breaking Ground is soon.”
	ys “Are you sure? You look like you’re in pain.”
	y “I’m sure.”
	ys “Ok. Let me wait with you at least.”
	n “You and Ysabel wait for the 5sure to come. It comes and she sees
		you off.”
	ys “I’ll see you [name].”
	y “I’ll see you Ysabel.”
label .please
	y “Please.”
	ys “Yeah I got you. Here, swing your shoulder over me.”
	y “Alright yeah.”
	n “You’re in so much pain as you limp back to Okada, but the fact that
		you’re half-hugging Ysabel makes it better.”
	ys “Alright here you are.”
	y “Thank you so much.”
	ys “I’m going to ask Scarlett for an ice pack for you.”
	y “Ok thank you.”
	n “Ysabel goes downstairs and gets an icepack.”
	ys “Here you go.”
	y “Thank you so much.”
	ys “Alright. I’m gonna wait here with you for half an hour and see
		how badly your ankle swells.”
	y “Shouldn’t you go back to the A3C?”
	ys “No my co-chair will be able to handle it today. I need to take care of
		you.”
	n “You feel the pain go away as she says that and smiles. How does she dance
		in Kayu, CO, and FFS and also be such a caring RA?”
	ys “Okay let’s check the swelling now. Hmm, it doesn’t look too bad. How bad
		does it hurt?”
	y “Not too bad. But I do feel bad for making you miss Kayu.”
	ys “No don’t worry about it. Everything will work out.”
	y “Yeah. It’s just…”
	ys “Rest, okay? Is there anything else you want me to get you?”
	menu:
		“Actually… I have something to tell you.”
			jump .tell_you_Ysabel
		“I’ll be good.”
			jump .be_good
label .tell_you_Ysabel:
	y “Actually, I have something to tell you.”
	ys “Yeah what is it?”
	y “I like you.”
	ys “Oh my gosh, [name].”
	y “Yeah, that’s why I went to the CO workshop and why I wanted to
		go to Kayu.”
	ys “[name]...”
	y “Yeah I know, but it’s just foolish.”
	ys “[name], I like you too. But I’m also your RA and I have a boyfriend.”
	y “Yeah I know.”
	y “Hey, I think I’ll be able to take care of myself. You should at least
		get some rest yourself.”
	ys “Are you sure?”
	y “Yeah.”
	ys “Alright. Have a good night.”
	n “You can’t help but feel a dull pain in your body, and it isn’t in your ankle.
		It’s in your heart. Why’d someone so wonderful and right come into
your life at the wrong time?


label part_three:
    if Jihyeon_Progress_Two == True:
        n "Over the break you couldn't stop thinking about Jihyeon."
    if Manisha_Progress_Two == True:
        n "Over the break you couldn't stop thinking about Manisha."
    if Cheng_Hau_Progress_Two == True:
        n "Over the break you couldn't stop thinking about Cheng-Hau."
    if Pao_Progress_Two == True:
        n "Over the break you couldn't stop thinking about Pao."
    if Edwin_Progress_Two == True:
        n "Over the break you couldn't stop thinking about Edwin."
    if Ysabel_Progress_Two == True:
        n "Over the break you couldn't stop thinking about Ysabel."
    if Huanvy_Progress_Two == True:
        n "Over the break you couldn't stop thinking about Huanvy."
    n "When you get back to campus, you need to see them."
    n "But who should you see?"
    n "There is only enough time to see one person."
    n "You should save the game now. You will only be able to choose one
        person to spend time with, but you can go back to an earlier save."
    menu:
        "Jihyeon" if Jihyeon_Progress_Two == True:
            jump .jihyeon_part_three
        "Manisha" if Manisha_Progress_Two == True:
            jump .manisha_part_three
        "Cheng-Hau" if Cheng_Hau_Progress_Two == True:
            jump .cheng_hau_part_three
        "Pao" if Pao_Progress_Two == True:
            jump .pao_part_three
        "Edwin" if Edwin_Progress_Two == True:
            jump .edwin_part_three
        "Ysabel" if Ysabel_Progress_Two == True:
            jump .ysabel_part_three
        "Huanvy" if Huanvy_Progress_Two == True:
            jump .huanvy_part_three

    label .edwin_part_three:
        y "I have to find Edwin. Where is he?"
        n "You go searching all throughout campus to find Edwin. His room, the foyer, the
        Teahouse, Jordan Hall, the A3C. But he’s nowhere to be found."
        define v = ("Voice")
        v "Hey"
        y "Huh?"
        v "Hey [name]"
        n "You turn around."
        d "Hey [name]. I’ve been looking for you."
        y "I’ve been looking for you too, Edwin."
        d "Well, how have you been? How was break?"
        y "I’ve been alright. I’ve been…"
        menu:
            "I’ve been…"
            "Thinking about you":
                y "I’ve been thinking about you."
                $ Edwin_Response = "I’ve been thinking about you too."
            "Missing you":
                y "I’ve been missing you."
                $ Edwin_Response = "I’ve been missing you too."
            "Needing you":
                y "I’ve been needing you."
                $ Edwin_Response = "I’ve been needing you too."
            "Trying to forget you":
                y "I’ve been trying to forget you."
                jump .forget_you
        d "[name], [Edwin_Response]"
        y "...yeah."
        d "...yeah."
        y "But what can we do."
        d "Let’s go out. You and me."
        menu:
            "But what will Edith think?":
                y "But what will Edith think?"
            "But you’re staff, and I’m your resident":
                y "But you’re staff, and I’m your resident"
            "But we can’t":
                y "But we can’t"
                jump .we_cant
        d "But who cares? No one has to know."
        y "..."
        d "I like you so much, and I know you like me too. Encounters like this don’t come
            often."
        menu:
            "Then let’s go":
                y "Then let’s go."
            "We can’t, Edwin":
                y "We can’t, Edwin."
                jump .we_cant
        d "Ok I’m glad you want to."
        y "What are we going to do?"
        d "How about we go to the park and then afterwards… well I’ve save that for later."
        y "Alright let’s go."
        n "You and Edwin drive to the park. When you get there, he opens up the trunk
            and pulls out a picnic basket."
        y "What’s this?"
        d "It’s a picnic basket. Though the weather is cold, I thought we could have a
        picnic out here."
        y "Wow."
        d "What?"
        y "It’s just… you’re so cute."
        d "*blushes* You are too."
        y "What do you have?"
        d "Sandwiches, pasta salad, and pie."
        y "Wow delicious."
        d "Let’s go sit by the tree."
        y "All the leaves have fallen. Winter is really coming."
        d "Yeah it is, but at least I have you to keep me warm."
        menu:
            "Can I hug you?":
                y "Can I hug you?"
                $ hug_hand_lay = "hug"
            "Can I hold your hand?":
                y "Can I hold your hand?"
                $ hug_hand_lay = "hold hands with"
            "Can I lay on you?":
                y "Can I lay on you?"
                $ hug_hand_lay = "lay on"
        d "Yeah I’d like that a lot."
        n "You [hug_hand_lay] Edwin."
        y "This is nice."
        d "Yeah it is."
        scene black
        with dissolve
        d "Hey it’s getting dark. We should go back to campus."
        y "Yeah we should."
        scene okada lounge
        with dissolve
        d "Alright we’re back."
        y "So what’s the other thing you want to do?"
        d "Oh right."
        d "...Do you want to ...smash?"
        menu:
            "Yes":
                jump .yes_to_smash
            "Like Melee?":
                jump .like_melee
        label .like_melee:
            y "Like… Melee?"
            d "Yeah of course."
            y "Alright yeah I’m down to smash."
            d "Smashing in the lounge!"
            n "You and Edwin smash in the lounge for several hours."
            scene black
            with dissolve
            n "It gets late into the night and he falls asleep on you. You don’t want to
            wake him up, so you end up falling asleep with him too."
        label .yes_to_smash:
            y "Yes."
            d "Alright. Let’s go to my room."
            y "Alright."
            scene Edwin Room
            with dissolve
            y "Wow, we’re really doing this."
            d "Yeah, we are."
            y "..."
            d "Are you nervous?"
            menu:
                "Yes":
                    y "Yes"
                "Maybe":
                    y "Maybe"
                "No":
                    y "No"
            d "Don’t be. We don’t have to do anything you don’t want to do, and we
                can start slow."
            y "Ok."
            n "You look into Edwin’s eyes and then at his lips."
            y "Can I kiss you?"
            d "Yes."
            n "You two kiss."
            y "Wow, that was nice."
            d "Yeah."
            y "Do you want to kiss some more?"
            d "Can I cuddle with you?"
            y "Sure."
            n "You two cuddle for a while, and then fall asleep. Then morning comes."
            d "Hey, wake up."
            y "Yes."
            d "How are you feeling?"
            menu:
                "I feel good":
                    y "I feel good."
                    d "Yeah that was nice."
                "I love you.":
                    y "I love you."
                    d "I love you too."
            y "But can be together? People will find out."
            d "Who cares if they find out? I have you."
            y "..."
            y "I love you."
            d "I love you too."
            scene black
            n "UwUkada. Fin."
            label .forget_you:
                y "I’ve been trying to forget you."
                d "..."
                scene black
                n "UwUkada. Fin."
                return
            label .we_cant:
                y "We can’t, Edwin"
                d "..."
                scene black
                n "UwUkada. Fin"
                return
    label .Ysabel_Part_Three:
        y "I have to find Ysabel."
        n "You go looking around for Ysabel. Her room, the gym, the a3c, the nursery, Jordan Hall, and even her boyfriend’s dorm."
        n "She’s nowhere to be found, so you go to your room and give up."
        n "You hear a knock on your door. *knock knock*"
        n "You open the door."
        y "Ysabel!"
        ys "[name]."
        y "How are you?"
        ys "I’m ok. How are you?"
        y "I’ve been good. I’ve been…"
        menu:
            "I’ve been…"
            "Thinking about you":
                y "I’ve been thinking about you."
                $ Ysabel_Response = "I’ve been thinking about you too."
            "Missing you":
                y "I’ve been missing you."
                $ Ysabel_Response = "I’ve been missing you too."
            "Needing you":
                y "I’ve been needing you."
                $ Ysabel_Response = "I’ve been needing you too."
            "Trying to forget you":
                y "I’ve been trying to forget you."
                jump .bad_ending_ysabel
        ys "[name], [Ysabel_Response], but…"
        y "Right… your boyfriend…"
        ys "Yeah, and also I’m your RA. It just wouldn’t be right."
        y "It wouldn’t."
        ys "But [name], I’ve never felt this way before about anyone else."
        menu:
            "But your boyfriend":
                y "But your boyfriend."
            "You make my heart beat…":
                y "Ysabel, you make my heart beat a thousand miles a
                minute."
                ys "I feel so strongly about you, but I just can’t."
                jump .bad_ending_ysabel
        ys "Well I have some news."
        y "Yeah?"
        ys "Over the break, I broke up with my boyfriend."
        y "Oh I’m so sorry."
        ys "No don’t be. I broke up with him because I wanted to be with you."
        y "...*a pained smile draws on your face*..."
        ys "...*a pained smile draws on her face*..."
        y "Ysabel."
        ys "[name]."
        y "..."
        ys "Will you go out with me?"
        menu:
            "Yes":
                jump .yes
            "I can’t":
                y "I can't."
                jump .bad_ending_ysabel
        label .bad_ending_ysabel:
            ys "..."
            y "..."
            scene black with dissolve
            n "UwUkada. Fin."
            return
        label .yes:
            y "Yes."
            ys "Great *smiles*"
            y "Where do you want to go?"
            ys "Let’s go to get ramen."
            y "Wow that sounds yummy."
            ys "I know just the place."
            n "You and Ysabel go to a nearby ramen place."
            y "Wow the line is long."
            ys "It’s, because that means there’s more time to stand next to you."
            menu:
                "Can I hold your hand?":
                    y "Can I hold your hand?"
                    $hand_hug = hand
                "Can I hug you?":
                    y "Can I hug you?"
                    $hand_hug = hug
            ys "I’d like that."
            n "You [hand_hug] Ysabel."
            y "That was nice."
            ys "Yeah that was."
            ys "Oh wow we’re so close to the front."
            define w = ("Waiter")
            w "Hello, how many?"
            y "Two, please."
            n "You two are lead by the waiter to a table."
            ys "Oh wow this looks so delicious."
            y "What do you think you’re going to order?"
            ys "Hmm… I think I want some of… you. How’s that sound?"
            menu:
                "Oh wow":
                    y "Oh wow."
                "I want some of you":
                    y "I want some of you."
            ys "*blushes*"
            w "What would you like to order?"
            ys "I’ll have the tonkotsu ramen."
            menu:
                "I’ll have some of her":
                    y "I’ll have some of her."
                    ys "*blushes* stop that *giggles*"
                "I’ll also have tonkotsu ramen":
                    y "I’ll also have some tonkotsu ramen."

            w "Alright… your orders will come out shortly."
            ys "Oooo I can’t wait."
            y "Me neither."
            w "Alright here are your orders."
            ys "Thank you!!!"
            y "Thanks!"
            scene black
            with dissolve
            n "You two enjoy your ramen. After that, you go back to Ysabel’s
                room."
            scene ysabel room
            show ysabel
            with dissolve
            y "I’m so full."
            ys "Same."
            y "It’s nice hanging out with you."
            ys "Yeah. Hey I was thinking. Do you want to slow dance?"
            menu:
                "Yes":
                    y "Yes."
                    jump .slow_dance
                "No":
                    y "No."
                    jump .no_ysabel
        label .no_ysabel:
            ys "Oh, alright."
            n "You two sit and just enjoy each other’s presence for the night."
            scene black
            with dissolve
            n "UwUkada. Fin."
            return
        label .slow_dance:
            ys "Alright. Let me dim these lights and turn some music on."
            n "Ysabel dims the lights and turns some music on, and you two
                start to slow dance."
            y "This is nice."
            ys "Yeah, this is."
            menu:
                "Ysabel looks so nice with the soft lights glowing on her
                face."
                "Can I kiss you?":
                    y "Can I kiss you?"
                    ys "Yeah, I’d like that."
                    n "You two kiss."
                "*Just look into her eyes*":
                    n "You look deeply into her eyes. She looks deeply
                        into yours."
            ys "Hey, I think I want to do something more with you."
            menu:
                "I’d like to do something more too":
                    y "I’d like to do something more too."
                    jump .something_more
                "I don’t think I should do that.":
                    y "I don’t think I should do that."
                    y "I still don’t think we can be anything."
                    ys "You’re right."
                    jump .ysabel_bad_ending
        label .something_more:
            ys "Ok, I want to yike on you… in bed."
            y "I’m into that."
            ys "Are you ready?"
            y "Yeah, are you?"
            ys "Yeah, I am."
            scene black
            with dissolve
            n "You two enjoy each other’s company for the night."
            ys "Hey, I love you."
            y "I love you too."
            n "UwUkada. Fin."
            return
