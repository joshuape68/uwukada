# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narrator")
define y = Character("You")
define c = Character("Cheng-Hau")
define j = Character("Jihyeon")
define m = Character("Manisha")
define p = Character("Pao")
define h = Character("Huanvy")
define d = Character("Edwin")
define ys = Character("Ysabel")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg main quad

    # These display lines of dialogue.

    n "This is your first day at Stanford University!"
    n "You're so excited to be on campus finally,
        and you can't wait to meet all the cool people here"

    scene bg okada outside
    y "Wow, this dorm is quite lovely! I love the theme!"
    scene bg okada lounge
    show c
    c "Hi there! Welcome to Okada, I’m your RA Cheng Hau, and I use they/them pronouns."
    c "You must be?"
    python:
        name = renpy.input("My name is...")
        pronouns = renpy.input("My pronouns are...")
    y "Hi I'm [name] and I use [pronouns]. It's nice to meet me, I mean you! Ahhh"
    y "I messed up already"
    show h rightish
    h "Mood."
    show d leftish
    d "Y = mx + it be like that sometimes *hehe*"
    c "*cute laugh* Nice to meet you [name]"
    h "I'm Huanvy and I use they/them pronouns. I'm one of the ethnic theme associates"
    d "I'm Edwin and I use he/him prnouns. I'm also an ETA. Welcome to Okada [name]"
    hide c
    hide h
    hide d
    n "The staff are so super duper cool! And all very attractive ;)."
    n "You should head up to your room and unpack"
    show bg black
    n "It is now night time, and you decide to explore around the dorm."

    #These are flags for if a person has successfully interacted with a
    #a character. These will be used for the next set of interactions to
    #see if they can progress in the interaction tree
    python:
        Jihyeon_Progress_One = False
        Manisha_Progress_One = False
        Cheng_Hau_Progress_One = False
        Pao_Progress_One = False
        Edwin_Progress_One = False
        Ysabel_Progress_One = False
        Huanvy_Progress_One = False
        #These are for introductions
        Jihyeon_Introduction_Dialogue = False

    #This label first_night has the menu for the options of where to go
    label first_night:
        menu first_night_menu:
            "Where should I go?"
            "2nd Floor":
                jump .Second_Floor_first_night
            "1st Floor":
                jump .First_Floor_first_night
            "Courtyard":
                jump .Courtyard_first_night
        #This label Second_Floor_first_night has the options for Jihyeon
        #Manisha, or just going back to the first_night menu
        label .Second_Floor_first_night:
                menu:
                    "You hear someone singing Girls Generation":
                        jump .Jihyeon_first_night
                    "You hear Punjabi music playing":
                        jump .Manisha_first_night
                    "Go back":
                        jump first_night

        #This label Jihyeon_first_night has the Jihyeon interaction
        label .Jihyeon_first_night:
            show j
            #This is vital to ensuring that a person introduces only 1 time
            if Jihyeon_Introduction_Dialogue == False:
                n "You check out the room that the singing is coming from"
                j "Oh hi I'm the RCC Jihyeon and I use she/her prnouns"
                y "Oh hi I'm [name] and I use [pronouns]"
                $ Jihyeon_Introduction_Dialogue = True
            j "Do you want to come in?"
            menu:
                "Yes":
                    y "Ok sure"
                    jump .Yes
                #Saying no doesn't lock people out
                "No":
                    jump first_night
            j "Have a seat. I was just singing some Girls Generation"
            label .Yes:
                menu:
                    "I love K-pop":
                        jump Jihyeon_first_night.I_Love_K_Pop
                    "Oh, K-pop is lame":
                        jump Jihyeon_first_night.K_Pop_Is_Lame
            #This is the good line that allows people to progress Jihyeon
            label .I_Love_K_Pop:
                y "I love K-Pop"
                j "Oh my gosh what's your favorite artist?"
                $ fav_k_pop = renpy.input("What's your favorite artist?")
                y "My favorite artist is [fav_k_pop]"
                j "Oh my gosh I love [fav_k_pop] too"
                j "Do you want to watch music videos right now?"
                y "Yes!!!"
                hide j
                scene bg black
                n "You watch music videos for 2 hours, laughing, giggling, and having fun"
                scene j
                show j
                j "Hey this was really fun. We should do this again sometime"
                #This flag turns True allowing for progress
                $ Jihyeon_Progress_One = True
            #This is one of the bad lines that lock people out of Jihyeon
            label .K_Pop_Is_Lame:
                j "Oh okay. What do you like?"
                $ jihyeon_I_Like = renpy.input("I like")
                y "I like [jihyeon_I_Like]"
                j "Oh yeah, that's cool."
                n "There's an awkward silence"
                j "Hey I thinking I'm going to sleep soon"
                y "Ok"

        #This labe Manisha_first_night is the first interaction with Manisha
        label .Manisha_first_night:
            $ Manisha_Introduction_Dialogue = False
            if Manisha_Introduction_Dialogue = False:
                n "You go to the room that the music is playing from"
                m "Oh hey I'm Manisha and I use she/her pronouns"
                y "I'm [name] and I use [pronouns]"
                m "I was just practicing for my bhangra performance"
                $ Manisha_Introduction_Dialogue = True
            m "Do you want to come in?"
            menu:
                "Yes":
                    jump .yes
                "No thanks":
                    jump .no
            label .yes:
                m "Hey do you want to see me dance?"
                y "Sure I'd love to"
                m "Here let me just turn the music back on *turns music on*"
                n "*Manisha dances*"
                y "Wow you're really good at dancing"
                m "Thanks. Hey do you want to learn some steps?"

            label .no:
        label .First_Floor_first_night:
            menu:
                "You feel drawn to some wise aura":
                    jump Pao_first_night
                "You hear the sound of clacking coming from the lounge":
                    jump Edwin_first_night
                "You smell spam being fried from the kitchenette":
                    jump Cheng_Hau_first_night
        label .Pao_first_night:
        label .Edwin_first_night:
        label .Cheng_Hau_first_night:
        label .Courtyard_first_night:
            menu:
                "You see someone flyering":
                    jump Huanvy_first_night
                "You feel the vibrations of someone wiggling":
                    jump Ysabel_first_night
        label .Huanvy_first_night:

        label .Ysabel_first_night:

    #These are flags for if a person has successfully interacted with a
    #character. If so, then the the third interaction is unlocked
    python:
        Jihyeon_Progress_Two = False
        Manisha_Progress_Two = False
        Cheng_Hau_Progress_Two = False
        Pao_Progress_Two = False
        Edwin_Progress_Two = False
        Ysabel_Progress_Two = False
        Huanvy_Progress_Two = False
    # This ends the game.

    return
