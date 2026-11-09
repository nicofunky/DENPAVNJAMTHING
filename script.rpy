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
define ExaUn = Character("Unknown", who_color='#a9a9a9',what_color='#a9a9a9',kind=nvl,what_textalign=0.0)
define Exa = Character("Exa", who_color='#a9a9a9',what_color='#a9a9a9',kind=nvl,what_textalign=0.0)
define Bully =Character("Bully", who_color='#DC143C',what_color='#DC143C',kind=nvl,what_textalign=0.0)


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
    scene city2
    with fade

    pause 1.0

    ChuniNar "Finally{w=0.5}, after all the courage{w=0.5}, I managed to set foot on the outside.{p}That place that I had cut off for so long, it now lays before me, bare, empty, lifeless.{p} All of the traffic, all of the life of the city that annoyed my ears whenever I left the window open, all of it now was dormant."
    ChuniNar "Only I seemed to exist within this landscape in this moment of time."
    nvl clear
    ChuniNar "Well, this is convenient for me.{p}This means a lot less eyes will be on me.{p}That is always a benefit.{p}I make sure I have the right location on the map and I embark on my journey."
    ChuniNar "The destination?{p}A train station on the outskirts of the city."
    nvl clear
    ChuniNar "The eeriness of the landscape did not go unnoticed.{p}I understand that it is nighttime, but to have absolutely no traffic of any kind in a city of this size?{p}Utterly unheard of."
    ChuniNar "The wind blows by, {w=0.5}unbothered by the lack of resistance usually present.{p}Nothing echos through the streets.{p}My own footsteps don't even make a dent in the soundscape of the silent city, them being audible to my ears alone."
    nvl clear
    ChuniNar "No Window remains illuminated.{p}The only lights shining are the streat lamps and the stars.{p}Not even the gas stations have their lights on, and no cars remain parked."
    ChuniNarCnt "..."
    nvl clear
    ChuniNar "Wait."
    ChuniNar "There are no cars.{p}None parked, driving, or anything.{p}Where is everyone?"
    ChuniNar "It is like the whole city is devoid of life."
    nvl clear
    ChuniNarCnt "..."
    nvl clear
    ChuniNar "This is..."
    ChuniNar "Very...{w=0.5} unusual..."
    nvl clear
    ChuniNar "Hairs begin to stand.{p}I feel {cps=3}eyes {/cps}looking at me.{p}I looked around, turning.{p}The source of the eyes wasn't there.{p}Of course, there is nothing here."
    ChuniNar "I see no one here, around, nor anywhere.{p}Could the sight have come from one of the buildings?"
    nvl clear
    ChuniNar "Instinctually I dashed into a nearby alleyway.{p}Confirming with the map, this is a shortcut I can take.{p}And so, I make my way down the alleyway that was sswallowed in shadow."
    nvl clear
    ChuniNar "Past the alleyway, I made it into a residential area.{p}Buildings way less taller than the apartments, now revealed more of the sky, in turn showcasing more stars.{p}This reveal made me pause in my tracks for a second, {w=0.5} unfortunately."
    ChuniNar "A mear distraction.{p}I continued on."
    ChuniNar "Well, I would have, if I didn't notice an...{w=0.5} oddity."
    nvl clear
    ChuniNar "The Shadows."
    ChuniNar "The shadows here seemed to leak from the light posts.{p}They spilled heavily into every direction, contradicting their natural form."
    ChuniNar "This..."
    nvl clear
    Chuni "\"...isn't normal.\""
    ChuniNar "{cps=75}No shit it isn't.{p}Of course it isn't!{/cps}{p}I sensed one of the shadows looking at me.{p}It was the same sensation as {cps=15} before.{/cps}{p}More hairs stand.{p}My senses cannot be wrong.{w=0.25} {i}Can they?{/i}"
    nvl clear
    ChuniNar "The further I move forward, the more shadows spill out, almost combining with each other.{p}I continued to make my way forward, avoiding stepping on the shadows."
    nvl clear
    ChuniNar "I came to a junction.{p}A four way junction."
    ChuniNar "An impasse."
    ChuniNar "The shadows from the four corners bled into each other, merging right at the middle."
    ChuniNar "Then, the shadow took form."
    nvl clear
    ChuniNar "It began to rise, molding itself into a human figure.{p}The lights began to flicker rapidly, as if they're..."
    ChuniNar "transmitting data right into my eyes?{p}It doesn't fully work.{p}I still see a shadowy figure before me, a rought approximation of the human form.{p}However, now this... thing... is wearing clothes, ones I am vary familiar with."
    ChuniNar "It's the School uniform."
    nvl clear
    ChuniNar "The shadow makes a wave motion towards me."
    ExaUn "\"Hey!{w=0.5} It's that time again, isn't it?\""
    ChuniNar "That voice.{p}That motion.{p}It's exactly the same as before, as I remember."
    ChuniNar "The flickering accelerates, forcing me to recall a scene of static."

    scene crossing
    with blinds
    nvl clear

    ChuniNarCnt "..."
    nvl clear
    ChuniNar "A classroom filled to the brim with people.{p}Unfortunately, our school was understaffed, so this kind of cramming was a normality within this building.{p}This came with its own benefits and downsides."
    ChuniNar "The benefit is that it allowed someone as myself to blend in with the class.{p}I never stood out, never wanted to.{p}I only wanted to remain in my delusions, by myself, unbothered by anyone else.{p}Delusions of traveling the stars, of fighting monsters, of aiding people, the lot you'd usually image in a scene of boredom."
    nvl clear
    ChuniNar "A downside is that a certain few can lead the pack."
    ChuniNar "This happened during one of the many lunch times.{p}It's a simple enough story that you hear plenty of times."
    ChuniNar "A kid was being bullied for his food."
    nvl clear
    Bully "It's that time again, isn't it?"
    ChuniNar "The bully said to the kid.{p}Of course the kid couldn't fight back.{p}Of course no one stepped in."


    #Chapter 2-1



    #Chapter 2-2


    #Chapter 3-1


    #Chapter 3-2




    # This ends the game.

    return
