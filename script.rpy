# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define nn = Character(color="#d3e8ea", kind=nvl,what_textalign=0.0)
define nc =Character(color="#ffcccc", kind=nvl, what_xalign=0.5, what_yalign=0.5, what_textalign=0.5)
define Chuni = Character("Mio", who_color='#75F2BF',what_color='#75F2BF',kind=nvl,what_textalign=0.0)
define ChuniNar = Character(who_color='#75F2BF',what_color='#75F2BF',kind=nvl,what_textalign=0.0)
define ChuniNarCe = Character(who_color='#75F2BF',what_color='#75F2BF',kind=nvl,what_textalign=0.5)
define TB = Character("Unknown", who_color='#DC143C',what_color='#DC143C',kind=nvl,what_textalign=0.0)      #Tomboy Mio
define TBNar = Character(who_color='#DC143C',what_color='#DC143C',kind=nvl,what_textalign=0.5)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show chunni1

    nvl show dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.
    #Chapter 1-1

    nn "Stars."
    nn "Stars continue to rain down their light from above, regardless of how we feel.{p}They’re indifferent to our existence.{p}They’re unbothered by the continuous gaze of mankind.{p}They don’t mind all the myths and legends we build up around them.{p}They accept any visitors or passerbys, regardless of their status."
    nn "They continue to shine, regardless of it all, until they die."
    nvl clear
    nc "{cps=0}penis penis balls{/cps}"
    nvl clear
    nn "penis balls"
    nn "more text."
    nc "more test text."
    nvl clear
    nn "penis."

    #Chapter 1-2
    nvl clear
    Chuni "I am alone.{p}I\'m alone.{p}{cps=10}I am alone.{/cps}{p}I am {cps=5}alone.{/cps}"
    ChuniNar "I speak as if there was someone here.{p}I cut myself off from the world by staying in this room.{p}There is no access to the outside here.{p}I am by myself in this room.{p}No {cps=10}eyes{/cps} can cast their gaze on me while I am in this room."
    nvl clear
    ChuniNarCe "This is True."
    nvl clear
    ChuniNar "I look around for the umpteenth time to confirm this statement of fact.{p}The blinds are closed.{p}The windows are shut.{p}The door is locked. The walls have no holes.{p}Everything is as it should be."
    ChuniNar "There is no one here.{p}There are no eyes on me."
    ChuniNarCe "I am alone.{p}I am alone.{p}I am alone."
    nvl clear
    ChuniNarCe "..."
    ChuniNar "I can confirm this as a fact now.{p}{cps=10}I am safe.{/cps}"
    nvl clear
    Chuni "\"I am safe!\""
    ChuniNar "The words echo through the room as I jump out of my chair, taking a victorious stance."       #Has to be nar after Chuni proper to not have Mio name be put many times while Chunni is still thinking or talking.
    ChuniNar "\"Heh.{w=0.5} It is only natural.\""
    ChuniNar "A flick of my hair was added for some additional coolness factor."
    nvl clear
    Chuni "{cps=5}\"Haaaaaaaaah.\"{/cps}"
    ChuniNar "A sigh of relief escaped me as I fell back into my chair.{p}Naturally,{w=1.0} my line of sight fell towards the radio that sat off in the distance.{p}It seemed that I would have to crack this code manually, less I risk another attack."

    #Put Transiition here

    TBNar "A woman sits by her fireplace,{w=0.25} relaxing after another hard days work.{p}The whole house now looked sparkiling, as if it was never occupied in the first place."

    #Chapter 1-3



    #Chapter 2-1



    #Chapter 2-2


    #Chapter 3-1


    #Chapter 3-2




    # This ends the game.

    return
