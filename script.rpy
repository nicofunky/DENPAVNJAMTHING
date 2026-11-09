# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define nn = Character(color="#d3e8ea", kind=nvl,what_textalign=0.0)
define nc =Character(color="#ffcccc", kind=nvl, what_xalign=0.5, what_yalign=0.5, what_textalign=0.5)
#Tomboy Mio
define Chuni = Character("Mio", who_color='#75F2BF',what_color='#75F2BF',kind=nvl,what_textalign=0.0)
define ChuniNar = Character(who_color='#75F2BF',what_color='#75F2BF',kind=nvl,what_textalign=0.0)
define ChuniNarCnt = Character(who_color='#75F2BF',what_color='#75F2BF',kind=nvl,what_xalign=0.5, what_yalign=0.5, what_textalign=0.5)
#Tomboy Mio
define TB = Character("Unknown", who_color='#DC143C',what_color='#DC143C',kind=nvl,what_textalign=0.0)
define TBNar = Character(who_color='#DC143C',what_color='#DC143C',kind=nvl,what_textalign=0.0)
define TBNarCnt = Character(who_color='#DC143C',what_color='#DC143C',kind=nvl,what_xalign=0.5, what_yalign=0.5, what_textalign=0.5)


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #show chunni1   Show should be used for characters, not scenes
    scene chunni1
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
    scene chunni1
    with fade

    pause 1.0

    nvl clear
    Chuni "I am alone.{p}I\'m alone.{p}{cps=10}I am alone.{/cps}{p}I am {cps=5}alone.{/cps}"
    ChuniNar "I speak as if there was someone here.{p}I cut myself off from the world by staying in this room.{p}There is no access to the outside here.{p}I am by myself in this room.{p}No {cps=10}eyes{/cps} can cast their gaze on me while I am in this room."
    nvl clear
    ChuniNarCnt "This is True."
    nvl clear
    ChuniNar "I look around for the umpteenth time to confirm this statement of fact.{p}The blinds are closed.{p}The windows are shut.{p}The door is locked. The walls have no holes.{p}Everything is as it should be."
    ChuniNar "There is no one here.{p}There are no eyes on me."
    ChuniNarCnt "I am alone.{p}I am alone.{p}I am alone."
    nvl clear
    ChuniNarCnt "..."
    nvl clear
    ChuniNar "I can confirm this as a fact now.{p}{cps=10}I am safe.{/cps}"
    Chuni "\"I am safe!\""
    ChuniNar "The words echo through the room as I jump out of my chair, taking a victorious stance."       #Has to be nar after Chuni proper to not have Mio name be put many times while Chunni is still thinking or talking.
    ChuniNar "\"Heh.{w=0.5} It is only natural.\""
    ChuniNar "A flick of my hair was added for some additional coolness factor."
    nvl clear
    Chuni "{cps=5}\"Haaaaaaaaah.\"{/cps}"
    ChuniNar "A sigh of relief escaped me as I fell back into my chair.{p}Naturally,{w=1.0} my line of sight fell towards the radio that sat off in the distance.{p}It seemed that I would have to crack this code manually, less I risk another attack."
    nvl clear

    nvl clear
    scene tomboy1
    with fade

    pause 1.0

    TBNar "A woman sits by her fireplace,{w=0.25} relaxing after another hard days work.{p}The whole house now looked sparkiling, as if it was never occupied in the first place.{p}Such a high standard of maintenance was unheard off, so this accomplishment brought with a great deal of pride."
    TBNar "All of the shelves contained the cutlerly specifically made to her liking.{p}After all, she made them herself.{p}You have a lot of time to do things once you are out here by yourself."
    nvl clear
    TBNar "Paintings of various sizes cover the walls, paintings of no particular meaning.{p}They're just sights she thought looked interesting inside of this forest area."
    TBNar "She looked across the room and realised that there were no memories of a life before she arrived here.{p}This would normally {cps=10}unsettle{/cps} someone if they were to notice this detail,{w=0.5} But to her,{w=0.5} this served as yet another accomplishment."
    nvl clear
    TB "\"Look how cut off I am.\""
    TBNar "She stated to herself, once again reconfirming her reality with her voice.{p}The sight of it all, she almost got off to her own competence.{p}She continued to allow the wave of self praise to wash over her.{p}Oh look, it's all the wooden furniture she varnished by hand.{p}Oh, how competent she is."
    nvl clear
    TBNar "She let out a laugh that echoes throughout the room, then took another sip of her tea."
    TBNar "This is it.{p}This is the outcome she wanted."
    nvl clear
    TBNarCnt "..."
    nvl clear
    TBNar "An intrusive thought came to mind.{p}That one family member came to mind."
    TBNar "That little sister."
    TBNar "She tired to recall what she looked like,{w=0.5} with no success.{p}She tried to look for any visual reference of her,{w=0.5} only to realise that she had no physical mementos anywhere."
    nvl clear
    TBNar "All the places that would contain memorabilia relating to her family or history, in those places, are pieces that reflect her current self...{p}Her present self."
    TBNar "This...{p}is an odd point that forces itself to be acknowledged by her.{p}This is not normal."
    nvl clear
    TBNarCnt "..."
    nvl clear
    TBNar "She acknowledges this state of reality and continues slipping on her tea.{p}Only there was no more tea.{p}She looked at her cup."
    nvl clear
    TBNarCnt "..."
    nvl clear
    TBNar "She drank it all.{p}The horror.{p}This forced her to get up from her sofa, make her way past the sealed room, and arrive at the kitchen door.{p}She took a hold of the handle, only to pause."
    TBNar "She wanted to open it. She wanted to enter.{p}But something in the back of her head was saying{p}'Stop. Don't.'{p}It was intrusive, unwanted, forced.{p}Despite this, she closed her eyes and pictured what was beyond the door."

    #Chapter 1-3
    nvl clear
    scene chunni1
    with fade

    pause 1.0

    ChuniNar "Finally{w=0.5}, after all the courage{w=0.5}, I managed to set foot on the outside.{p}That place that I had cut off for so long, it now lays before me, bare, empty, lifeless.{p} All of the traffic, all of the life of the city that annoyed my ears whenever I left the window open, all of it now was dormant."
    ChuniNar "Only I seemed to exist within this landscape in this moment of time."
    nvl clear
    ChuniNar "Well, this is convenient for me.{p}This means a lot less eyes will be on me.{p}That is always a benefit.{p}I make sure I have the right location on the map and I embark on my journey."
    ChuniNar "The destination?{p}A train station on the outskirts of the city."


    #Chapter 2-1



    #Chapter 2-2


    #Chapter 3-1


    #Chapter 3-2




    # This ends the game.

    return
