# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Jing")
define m = Character(_("Me"), color="#c8c8ff")

# This is a variable that is True if you've compared a VN to a book, and False
# otherwise.
default ramen = False

image ramen:
    "bg ramen.jpg"
    pause 0.5    

#animation
transform moveFromLeftToRight:
    align (1.0, 0.0)
    linear 3 xalign 0.0
    linear 2 xalign 1.0
    repeat

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg club #never have 2 of these bg tag showing at once
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show jing happy
    with dissolve
    # These display lines of dialogue.

    e "Hi! How are you feeling? I'm super hungry and I'm craving Ramen.." #吃了吗？

    # choices
    menu:

        "Me too..."

        "Wanna go for Ramen?":

            jump ramen

        "I hate Ramen!":

            jump breakup            

        "Ask her out later.":

            jump later

label ramen:

    show jing happy

    m "Wanna go for Ramen?"

    e "Yes! I never say no to Ramen!"

    #animation
    #show ramen at moveFromLeftToRight
    #pause 

    scene bg ramen
    with fade        
    pause 1.0   

    scene black
    with dissolve

    "Together, we live happily ever after with lots of Ramen."

    "{b}Good Ending{/b}."

    return

#right away
label breakup:

    show jing happy

    m "I hate Ramen!!!"

    m "I will never go out with anyone who likes Ramen. Are you OK with that?"

    e "Unless you are a bowl of Ramen, the answer is yes, I can live without you."

    scene bg ramen
    with fade     
    pause 1.0       

    scene black
    with dissolve

    "We broke up shortly after that."

    "{b}Bad Ending{/b}."

    return    

# later
label later:

    "I decide to ask her later."

    scene black
    with dissolve

    "But I'm an indecisive person."

    "I couldn't ask her that day and I end up never being able to ask her."

    "{b}Bad Ending{/b}."

    return


    # This ends the game.

   # return
