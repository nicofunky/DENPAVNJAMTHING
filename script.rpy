#Start of document. Hi!

define nn = Character(color="#d3e8ea", kind=nvl,what_textalign=0.0)                                                                             #Basic text with no styling
define nc =Character(color="#ffcccc", kind=nvl, what_xalign=0.5, what_yalign=0.5, what_textalign=0.5)                                           #Basic text positioned on center of screen
#Chunni Mio
define Chuni = Character("Mio", who_color='#75F2BF',what_color='#75F2BF',kind=nvl,what_textalign=0.0)                                           #Chunni's voice
define ChuniNar = Character(who_color='#75F2BF',what_color='#75F2BF',kind=nvl,what_textalign=0.0)                                               #Chunni's POV
define ChuniNarCnt = Character(who_color='#75F2BF',what_color='#75F2BF',kind=nvl,what_xalign=0.5, what_yalign=0.5, what_textalign=0.5)          #Chunni's POV center text

#Tomboy Mio
define TB = Character("Unknown", who_color='#DC143C',what_color='#DC143C',kind=nvl,what_textalign=0.0)                                          #Tomboy's Voice (as unknown)
define TBKn = Character("Mio?", who_color='#DC143C',what_color='#DC143C',kind=nvl,what_textalign=0.0)                                           #Tomboy's Voice (as Mio)
define TBNar = Character(who_color='#DC143C',what_color='#DC143C',kind=nvl,what_textalign=0.0)                                                  #Tomboy's POV
define TBNarCnt = Character(who_color='#DC143C',what_color='#DC143C',kind=nvl,what_xalign=0.5, what_yalign=0.5, what_textalign=0.5)             #Tomboy's Pov center Text

#Mio
define Mio = Character("Mio", who_color='#a9837e', what_color='#a9837e', kind=nvl, what_textalign=0.0)                                          #Mio's voice, at the end
define MioNar = Character(who_color='#a9837e', what_color='#a9837e', kind=nvl, what_textalign=0.0)
define MioNarCnt = Character(who_color='#a9837e', what_color='#a9837e', kind=nvl, what_xalign=0.5, what_yalign=0.5, what_textalign=0.5)          #Mio's POV center text

#Exa
define ExaUn = Character("Unknown", who_color='#a9a9a9',what_color='#a9a9a9',kind=nvl,what_textalign=0.0)                                       #Exa's Voice (as Unknown)
define Exa = Character("Exa", who_color='#a9a9a9',what_color='#a9a9a9',kind=nvl,what_textalign=0.0)                                             #Exa's Voice
define ExaCont = Character(who_color='#a9a9a9',what_color='#a9a9a9',kind=nvl,what_textalign=0.0)   
define ExaContCnt = Character(who_color='#a9a9a9',what_color='#a9a9a9',kind=nvl,what_xalign=0.5, what_yalign=0.5, what_textalign=0.5)             #Exa's Voice (used for continuing so that her name doesn't clog the screen.

#Others
define Bully =Character("Bully", who_color='#DC143C',what_color='#DC143C',kind=nvl,what_textalign=0.0)                                          #Bully's Voice
define School1 = Character("Voice 1",color="#d3e8ea", kind=nvl,what_textalign=0.0)                                                              #Unnamed "Voice"'s Voice
define School2 = Character("Voice 2",color="#d3e8ea", kind=nvl,what_textalign=0.0)
define School3 = Character("Voice 3",color="#d3e8ea", kind=nvl,what_textalign=0.0)

#Fade
define end_fade = Fade(3.0, 2.5, 3.0, color="#000000")

# The game starts here.

label start:

    #show chunni1   Show should be used for characters, not scenes
    scene stars1
    nvl show dissolve
    play music "Music/Respite.ogg" fadein 5.5 volume 0.5

    #Chapter 1-1
    nn "Stars."
    nn "Stars continue to rain down their light from above, regardless of how we feel.{p}They’re indifferent to our existence.{p}They’re unbothered by the continuous gaze of mankind.{p}They don’t mind all the myths and legends we build up around them.{p}They accept any visitors or passerbys, regardless of their status."
    nn "They continue to shine, regardless of it all, until they die."
    nvl clear
    ChuniNar "It is a kind of cruel fate, don’t you think? These shining stars didn’t have a choice, a say, any input in the matter of their existence or purpose.{p}...{p}Do the stars think of a higher power? Do they look up to something above them, just like we do? Do the stargazed have their own sky?"
    ChuniNar "..."
    ChuniNar "It makes me sick."
    nvl clear
    ChuniNar "The stars, the beyond, the above.{p}All of it is unreachable.{p}Regardless of it all, I’m forced to hope in an entity that might get me near them or hope in the human will to overcome obstacles.{p}Both options rely on someone else. No solution to my problem exists."
    ChuniNar "And so, I am forced."
    nvl clear
    ChuniNar "I’m forced to stay ground-bound, a mere spectator to the starry stage above.{p}They’ll continue to be out of range, like all the other desirables in my life. Like everything else I tried to grasp, it will all just pass through my fingers."
    ChuniNar "I can grasp nothing.{p}I can hold nothing.{p}I can be nothing."
    nvl clear
    scene stars2
    ChuniNar "Nothing.{p}Nothing.{p}Nothing. Nothing. Nothing.{p}No eyes on me.{p}No nothing.{p}Nothing.{p}Nothing.{p}Nothing."
    nvl clear
    scene chunni1
    with dissolve
    ChuniNar "A new message in the thread snaps me back to look at my computer. I don’t know where my mind was, but the ping pulled me back in.{p}The alien thread has been dead lately as others are preoccupied with their daily activities.{p}Only true losers like myself have the time to talk about our delusions during these hours."

    #Chapter 1-2
    stop music
    nvl clear
    scene chunni1
    with fade

    pause 1.0

    nvl clear
    Chuni "I am alone.{p}I\'m alone.{p}{cps=10}I am alone.{/cps}{p}I am {cps=5}alone.{/cps}"
    ChuniNar "I speak as if there was someone here.{p}I cut myself off from the world by staying in this room.{p}There is no access to the outside here.{p}I am by myself in this room.{p}No {i}{cps=10}eyes {/cps}{/i}can cast their gaze on me while I am in this room."
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
    ChuniNar "No Window remains illuminated.{p}The only lights shining are the street lamps and the stars.{p}Not even the gas stations have their lights on, and no cars remain parked."
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

    scene classroom3
    with blinds
    nvl clear

    ChuniNarCnt "..."
    nvl clear
    ChuniNar "A classroom filled to the brim with people.{p}Unfortunately, our school was understaffed, so this kind of cramming was a normality within this building.{p}This came with its own benefits and downsides."
    ChuniNar "The benefit is that it allowed someone as myself to blend in with the class.{p}I never stood out, never wanted to.{p}I only wanted to remain in my delusions, by myself, unbothered by anyone else.{p}Delusions of traveling the stars, of fighting monsters, of aiding people, the lot you'd usually image up in a scene of boredom."
    nvl clear
    ChuniNar "A downside is that a certain few can lead the pack."
    ChuniNar "This happened during one of the many lunch times.{p}It's a simple enough story that you hear plenty of times."
    ChuniNar "A kid was being bullied for his food."
    nvl clear
    Bully "It's that time again,{w=0.5} isn't it?"
    ChuniNar "The bully said to the kid.{p}Of course the kid couldn't fight back.{p}Of course no one stepped in."
    ChuniNar "You've heard this before.{p}Like I said, it's a common enough trope."
    nvl clear
    ChuniNar "The whole class pretended to act as if this was some normalised and okay behaviour."
    ChuniNar "That is when I felt it for the first time.{p}I could hear a ping,{w=0.2} a screw dropping somewhere.{p}A disgust I never knew before began to radiate from within to the point of being overwhelmed by it."
    nvl clear
    ChuniNar "I has to ask myself, why now?{p}What set it off?{p}Why only now{w=0.5} and not before?"
    ChuniNar "I was too focused to answer my own questions.{p}In my vision only the bullied and the bully existed.{p}With a trembling body, I stood up and raised my bandaged covered arm.{p}I dragged my other hand to support the arm, as it seemed that my body was resisting this newly found will."
    nvl clear
    ChuniNar "No one paid me any attention as I assumed this unusual pose.{p}Not even the bully threw a glance my way, not that I needed his acknowledgement."
    ChuniNar "I took a deep breath, and closed my eyes."
    ChuniNar "Insticts told me to focus.{p}Focus forward.{p}Focus on the target."
    nvl clear
    scene classroom1
    ChuniNar "What is the target?{p}The bully."
    ChuniNar "What is the goal?{p}To stop this scene."
    ChuniNar "What do you feel?{p}I feel...{w=1.0} like this is an eyesore."
    ChuniNar "All of the feeling, all of it, I focused it onto my outstretched hand, and I felt my delusions being expelled into reality."
    nvl clear
    ChuniNarCnt "..."
    nvl clear
    ChuniNar "A silence."
    ChuniNar "An unusual silence for the time of day enveloped the classroom.{p}This caused me to open my eyes.{p}Before me was a scene of a class, all with their eyes on me."
    ChuniNar "All their piercing gazes were locked on me, on my odd pose, on my actions.{p}They all stared at me because the source of the commotion was gone."
    nvl clear
    scene classroom2
    ChuniNar "Vanished."
    ChuniNar "As if he never was there in the first place.{p}Even the bullied remained bewildered at the sudden disappearance."
    ChuniNar "All the eyes remained locked on me.{p}I felt it all.{p}All of the emotion radiated through me."
    nvl clear
    School1 "Why?"
    School2 "Why did you do that?{p}Who are you?"
    School1 "How?"
    School3 "Why him?"
    School2 "Why?"
    School3 "How dare you?"
    nvl clear
    ChuniNar "It was nauseating.{p}A static took over my sight and hearing.{p}Nothing made sense anymore."
    ChuniNar "Really?{p}He disappeared?{p}Just like that?"
    ChuniNar "Is this... was this really my doing?"
    nvl clear
    ChuniNar "I felt sick...{w=2.0}Sick."
    ChuniNar "I felt my head spin around the room. Possibly as an attempt to confirm the reality I now lived in.{p}All of the eyes in the room remained locked on me.{p}That person was gone now."
    nvl clear
    ChuniNarCnt "..."
    nvl clear
    ChuniNar "That...{w=1.0} is what happened.{p}A missing person's report was then filed a few days later.{p}Everypne refused to interact with me{w=1.0}, yet they continued their gaze.{p}They continued to stare at me{w=1.0}, the walking wonder, the scary sight, the mystery that I was."
    nvl clear
    School1 "How did she do that?"
    School2 "Did she really do it?"
    School1 "Are you sure we didn't imagine the whole deal?"
    School3 "Haha!{w=1.0} I hope she pull another trick like that!"
    scene city2
    with blinds
    nvl clear
    ChuniNarCnt "..."
    nvl clear
    ChuniNar "I Remember."
    ChuniNar "I Remember."
    ChuniNar "The need to disappear."
    ChuniNar "The will to be nothing."
    ChuniNar "The plea to vanish."
    nvl clear
    ChuniNar "I{w=0.5} remember."
    ChuniNar "It remembers."
    ChuniNar "The shadow before me takes a form largely unknown to me.{p}It no longer remains human."
    ExaUn "\"I'm here now.\""
    ChuniNar "It speaks."
    nvl clear
    ExaUn "\"Don't worry. I'll pay you back for the favor you did me."
    ChuniNar "It approaches."
    ExaCont "\"I'll unpeel those eyes off you myself.\"{p}\"That is you wish after all.\""
    ChuniNar "My Wish...{p}My Wish?"
    ChuniNar "What is my wish?{p}To disappear?"
    nvl clear
    ChuniNarCnt "..."
    nvl clear
    ChuniNar "Kind of?{p}I need to disappear from these {cps=5}{i}eyes.{/cps}{/i}{p}I need to vanish from their sight.{p}I need to be alone.{p}I don't exist."
    ChuniNar "I shouldn't exist.{p}I should have never met anyone.{p}{cps=10}I am nothing.{p}Nothing to anyone.{/cps}"
    nvl clear
    ChuniNarCnt "..."
    nvl clear
    ChuniNar "I heard a pin drop somewhere.{p}A new memory began to flood in, overlaying itself on the static.{p}There was someone else in that classroom."
    ChuniNar "Someone whose gaze wasn't one of hostility.{p}Someone who would later on become a close friend."
    nvl clear
    ChuniNar "I remember."
    ChuniNar "I remember that someone.{p}Despite the end we faced, despite the aftermath, despite it all damnit...{p}There was one friend there.{p}A friend that help me face the stares.{p}A freind that stood by my delusions."
    ChuniNar "I remember...{w=1.0} Her name was..."
    nvl clear
    Chuni "\"Exa?\""
    ChuniNar "The figure in front began to distort, forming itself into a tornado.{p}Wind began spiraling from within, causing the surrorunding lights to rapidly flicker once more, envoloping my sight in more static."
    ChuniNar "Something else was forming out the shadow.{p}A more tangible figure.{p}Something more familiar."
    nvl clear
    ChuniNar "The shadow was blown apart,{w=1.0} revealing the newly formed entity from within.{p}On the gorund I lay and look up to see what the smoke reveals."
    ChuniNar "It first revealed{w=0.5} a confident smile, then a pretty face, a familiar one.{p}The golden twin tails began to piece through the faint smoke curtain, until it was fully dispelled by her boastful voice."
    nvl clear
    Exa "\"Hahaha!{w=1.0} Yes!\""
    ChuniNar "She did a fist pump once she saw the situation."
    ExaCont "\"Tell me, dear one!\""
    ChuniNar "She reached out her hand, her bandaged covered right hand."
    ExaCont "\"Are you my master?\""
    nvl clear
    ChuniNarCnt "..."
    nvl clear
    Chuni "\"Ah. Ahahaha.\""
    ChuniNar "I felt the corners of my mouth rise."
    Exa "\"Hahaha.\""
    ChuniNar "And I-"

    #Chapter 2-1
    stop music
    scene tomboy2
    with wiperight
    nvl clear

    TBNar "-was not amused."
    TBNar "Exa stood on top of the shed, allowing the wind to flutter her twintails and skirt. The woman below continues to stare at the utter bizarre sight that was in front of her."
    nvl clear
    Exa "\"Hello?{w=1.0} You look like you just saw a ghost.\""
    TBNar "Exa threw out that witty comment,{w=0.5} thinking she was smart,{w=0.5} but she actually hit the nail on the head perfectly."
    TB "\"Get down!\""
    TBNar "The woman commanded."
    nvl clear
    Exa "\"...{w=0.5}Roger that.\""
    TBNar "Exa said with a hint of hesitation.{p}She performed a totally unnecessary front flip off the shed and landed on the ground with no problems.{p}The woman did not get to see this impressibe feat due to her back being already turned on Exa, dismissing her appearance as some sort of grand delusion she must have conjured up."
    nvl clear
    Exa "\"Hey!{w=0.5} You summoned me here for something,{w=0.5} correct?\""
    TBNar "Exa attempted to make conversation with the woman in her signature{w=0.25} cheerful voice, one which rubbed the woman the wrong way.{p}Her hand twitched, but no respone came.{p}She continued to walk towards her house unimpeded."
    nvl clear
    Exa "\"No...{w=0.5} Hey!{w=0.5} You're just walking off?!\""
    TBNar "Exa ran in front of the woman.{p}It's an honest attempt at getting the woman to stop in her tracks{w=0.5}, an attempt that gets met with hostility."
    TBNar "The woman pulls out a sawed off shotgun and points it at Exa."
    nvl clear
    TB "\"Why are you here?\" the woman demanded."
    Exa "\"Well, you summoned-\""
    TBNar "\"Stop playing.\""
    TBNar "The woman moves closer, shotgun still up.{p}She does not have the finger on the trigger. Despite being so close to a source of death, Exa seems more thrown off by the woman's emotional response than the possibility of being shot at.{p}She takes a breath before trying to reply to the person she once knew."
    nvl clear
    Exa "\"Okay{w=0.5} okay.{w=0.5} The truth is,{w=0.5} The Organisation sent me here.\""
    TBNar "Exa lifted her hands up and hung her head in defeat."
    TB "\"...{w=0.5}this again?{w=0.5} You are still going on about that?\""
    TBNar "The woman says, displeased with this answer.{p}The idea that this mature looking Exa is still believing in her delusions is,{w=0.5} frankly,{w=0.5} an absurd concept to even consider.{p}Exa looks on, horrified. She tries again to find that person in her memories."
    nvl clear
    Exa "\"It's much more important matter than you think Mio.{w=0.5} They rarely get involved like this,{w=0.5} you should know-\""
    TBKn "\"I came to these woods to be alone.\""
    TBNar "Mio moves in further, shotgun still pointed, finger still off the trigger.{p}Exa refuses to move.{p}The gun begins to visibly shake, unknown if it is out of anger or hesitation."
    nvl clear
    TBNar "The wind fills in for the silence left by the two.{p}Exa looks down at the gun{w=0.5}, then back up at the Mio.{p}Her disbelief is changed to a defeated smile, one that the woman interprets as pity{w=0.5}, which only accelerates the shakiness of the shotgun."
    nvl clear
    TBKn "\"No one is here{w=0.25} Exa. No one besides me.\""
    Exa "I know.{w=0.25} That is why-"
    TBNar "\"I made sure it would be that way.{w=0.25} No one besides me is to set foot here.\"{p}Her voice began to shake."
    nvl clear
    TBKn "\"No one else shall set sight on it, nor on me.{w=0.25} I made sure of it.{w=0.25} And yet.{w=0.1} And yet...!\""
    TBNar "Mio moves forward, pressing the shotgun agianst Exa, who still refuses to move.{p}This causes Mio to stubble forwards a little.{p}This is real.{p}This physical feedback confirms Exa is here in the flesh, meaning a loaded shotgun is now pressed up against the guts of Exa.{p}Mio panics and dashes backward,{w=0.25} creating a lot of distance between the two."
    nvl clear
    TBKn "\"You {i}DARE{/i} to show yourself...{w=0.25} now?{w=0.25} Of all times...{w=0.25} Now?!\""
    TBNar "Birds flew out from the trees in the distance after her shouts.{p}It acted like ambience between the two's silence.{p}Exa continued to stand there, looking at a person she can no longer recognise."
    TBNar "With a sigh and a bite of her lip, Exa spoke up first."
    nvl clear
    Exa "\"I understand.\""
    TBKn "\"Never show your face here again.\""
    ExaCont "\"Okay.\""
    TBNar "\"Go back.\""
    ExaCont "\"Okay.\""
    TBNar "\"Go back to whatever you were doing abroad.\""
    ExaCont "\"I understand.\""
    nvl clear
    TBNar "Mio continued to hold her shotgun up as Exa turned around and made her way into the woods.{p}Wiht her back now turned, Mio could have shot her to make her truly disappear from this realm.{p}And yet, despite her being one step away from ending it, depsite her intentions, the shotgun was not fired.{p}Exa simply disappeared into the forest."
    nvl clear
    TBKn "\"Damnit...\""
    TBNar "\"Damnit!!!\" she said while pointing her gun towards Exa's direction"
    TBNar "A loaded sigh left Mio.{p}\"When did I become {i}THIS WEAK{/i}?!\"{p}Her frustrations fell on no one's ears.{p}They only served to reinforce her reality,{w=0.2} well,{w=0.2} her perception of it,{w=0.5} of herself."
    nvl clear
    TBKn "\"She left me for that long and this is how I treat her?{w=0.2} I should have sent her off the second I saw her!\""
    TBNar "She hated that Exa arrived.{p}She hated that she still felt any empathy towards her.{p}She hated that she was seen."
    TBNar "She hated that it was her that broke through."
    nvl clear
    TBNarCnt "..."
    nvl clear
    TBNar "Mio looked off into the distance, the radio tower covering part of the sunset.{p}Another day was coming to a close.{p}However, with this encounter, Mio could sense something else was going to come to a close."
    TBNar "She knew that she was going to be invaded.{p}Be it that \'Organisation\' or something completely unexpected, {w=0.2}the safe haven is now compromised."
    nvl clear
    TBKn "\"How am I going to see my little sister now?\""
    TBNar "An uncharacteristic comment split out her lips.{p}This did not go unnoticed."
    TBNar "\"...{w=0.2}litte sister?\"{p}Only now is the reality of this absurd thought sinking in.{p}She looks off to the distance, once again at that radio tower."


    #Chapter 2-2
    stop music
    scene crossing  #Temp name
    with wipeleft
    nvl clear
    play music "Music/SlowRainfallLoop.ogg" fadein 1.0

    ChuniNar "Exa continues to sit across from me, with her back facing the radio tower off in the distance.{p}The train continues to throttle along, filling in for the lack of conversation."
    ChuniNar "This isn't an uncomforable kind of silence.{p}Just staring seems to be enough for the both of us at the moment.{p}Exa got to vent her frustrations over meeting her other friend, I got to hear her speak for the first time in a long while."
    ChuniNar "That's about all we needed right now."
    nvl clear
    ChuniNarCnt "..."
    nvl clear
    ChuniNar "Questions begin to flow around my mind, threatening to ruin this moment of ours.{p}I will need to address them soon enough since they won't stop itching in the back of my consciousness.{p}This moment feels too nice."
    ChuniNar "It's too perfect."
    ChuniNar "This cannot be real, and if it is, there has to be at least a catch.{p}After all, I went out to find an alien{w=1.0}, and instead I found Exa."
    nvl clear
    ChuniNar "This is highly unusual."
    ChuniNar "All of those Shadow figures, I still cannot discern if they were real or my panicked view of the world around me.{p}I almost tried to reach out to Exa out of instinct."
    ChuniNar "Almost."
    ChuniNar "I managed to keep my body in check before I moved a muscle.{p}This moment is too fragile.{p}It's too perfect.{p}I don't want to break it."
    nvl clear
    ChuniNarCnt "..."
    nvl clear
    ChuniNar "And yet, I want to speak up."
    ChuniNar "I look up and see that same smile I remember so fondly staring back.{p}She too is enjoying the mere presence of us being within the same room.{p}I try to say anything, but the words fail to manifest at a conceptual level.{p}Everything is just so bizarre.{p}There's almost too many questions to ask,{w=1.0} too much to talk about."
    nvl clear
    Exa "\"I should have said this first{w=1.0}, but words cannot express how happy I am to see you again, Mio.\""
    ChuniNar "This statement crashed my brain.{p}It ceased operations for a second before a quick reboot springed my body into action."
    Chuni "\"Exa...{w=1.0} it really has been too long.\""
    ChuniNar "I managed to voice some of my true feelings."
    nvl clear
    ExaCont "\"I'm sorry it took this long.{w=1.0} I really, really am.\""
    ChuniNar "She even nodded her head down significantly as she spoke,{w=1.0} trying whatever way she could think of to sound as sincere as possible."
    ExaCont "\"Mio.{w=1.0} I really am sorry.\""
    ChuniNar "I could hear her voice begin to tremble."
    ChuniNar "\"It's Okay.\"{p}I replied on instinct."
    nvl clear
    Exa "\"No.{w=1.0} No it isn't okay.{w=0.5} I can make all the excuses I want,{w=0.5} it won't change what happened.\""
    ChuniNar "I saw her start to shake."
    ExaCont "\"Bottom line is,{w=0.5} I failed you.{w=0.5} I really did, and I am sorry for that Mio.\""
    nvl clear
    Chuni "\"You are repeating yourself now, Exa.\""
    ChuniNar "I attempted to reply as softly as I could while my legs finally find the will to move towards her."
    ChuniNar "\"It's okay.{w=0.5} I'm here now{cps=5}...{/cps} right?\"{p}I managed to say as I plop down beside her, managing to get a firm grasp of her as I brought her close.{p}I even made sure to press extra hard against her to make sure she knew that this moment was real."
    nvl clear
    Exa "\"Right{cps=5}...{/cps} you are{cps=5}...{/cps} you sure are Mio.\""
    ChuniNar "A few sniffles managed to make themseleves known as she embraced me back with what felt like all the force she could muster."
    nvl clear
    ChuniNarCnt "..."
    nvl clear
    ChuniNar "More train ambiance filled in the gaps left between the now shared sniffles.{p}It seemed we're in the same camp{w=0.5}, as much as my feelings hate to admit it.{p}If this is not real, then this is a very convincing lie I'm living."
    ChuniNar "Even while I hold onto Exa tightly{w=0.5}, the thoughts continue to creep in.{p}This is not real.{p}This isn't the Exa you know.{p}This moment is your own delusion.{p}And yet, the simple warmth of Exa continues to push back against this wave of self doubt."
    nvl clear
    ChuniNarCnt "..."
    nvl clear
    ChuniNar "I can allow myself to be hopeful once in a while, right?"
    ChuniNar "I can allow myself to enjoy this moment, right?"
    ChuniNar "{i}Right{/i}"
    ChuniNar "Even if it is a delusion,{w=0.5} even if it is real, {w=0.5}whatever it is...{p}It is here,{w=0.5} right now,{w=0.5} in this moment."
    ChuniNar "The Train continues on, as do we, in each other's arms."
    nvl clear
    ChuniNarCnt "..."
    nvl clear
    ChuniNar "Eventually,{w=0.5} inevitably,{w=0.5} the moment must come to a close.{p}The train stops,{w=0.5} and we are forced to disembark at our desitination."
    Exa "\"We're here.\""
    Chuni "\"And where exactly is here?\""
    ChuniNar "We exit out of the train together, and face a forest entrance right off the train platform.{p}Exa moves in front of me and begins to drag me forawrds."
    nvl clear
    Exa "\"This is the path you'll have to walk down.\""
    Chuni "\"Why?\""
    ChuniNar "She never did explain why we're here in the first place."
    ExaCont "\"This is the path you'll need to take if you want to see...{w=0.5} my friend{w=0.5}, the one I told you about.\""
    nvl clear
    Chuni "\"And why would I want to see them?\""
    Exa "\"It's not a want, it's a need. You need to see each other.\""
    ChuniNar "She says this with a straight face, and a tone so straight you could almost mistake it for desperation."
    ExaCont "\"The path will be a difficult one.{w=0.5} However, this time, I will be there with you. {w=0.5}This time, you won't face it alone.\""

    #Chapter 3-1
    stop music
    scene forest2
    with pixellate
    nvl clear
    ChuniNar "Exa continued to guide me through the forest, holding my hand firmly.{p}The forest path itself was lit up by the occasional lamppost, which was a greatly appreciated feature since the sky has been blocked off by the trees.{p}I couldn't defer my vision to the sky anymore{w=1.0}, meaning I could only face forward now.{p}Forward{w=1.5}, with Exa in hand."
    nvl clear
    ChuniNarCnt "..."
    nvl clear
    ChuniNar "The air feels heavy.{p}Something is definitely off with this path."
    Exa "\"Are you keeping up?\""
    ChuniNar "She asks out of concern."
    Chuni "\"Yeah{w=1.0}, yeah I am.\""
    ExaCont "\"Good.{w=1.0} It's about to begin.\""
    ChuniNar "\"...What is?\""
    nvl clear
    ChuniNar "There was a lamppost,{w=1.0} I saw it.{p}It was flickering rapidly.{p}The shadows began to take shape once more."
    ChuniNar "This time, they seemed uninterested in my existence.{p}Instead they assumed the form of actors and began playing out a familiar scene."
    ChuniNar "It was the classroom scene.{p}It played out exactly as I remembered it.{p}I even felt a tint of the feelings I felt back then."
    nvl clear
    ChuniNar "Exa's grip tightens."
    Chuni "\"You can see this too?\""
    Exa "\"I can.\""
    ChuniNar "Once the performance is finished, the shadows disintegrate, and Exa continues pulling me forward."
    nvl clear
    ChuniNar "We stop at another lamppost,{w=1.0} one that begins flickering.{p}This time, the shadows emerged into another performance that was familiar to me.{p}A copy of Exa standing at the train station was shown."
    ChuniNar "Her grip tightens once again."
    ChuniNar "In the play, Exa mouths off some words that remain inaudible, and yet their meaning still reaches my ears, along with those feelings I felt back then."
    nvl clear
    Exa "\"I will be back, Mio.{w=1.0} I will be there when you'll need me.\""
    ChuniNar "She says those words I trusted so much in.{p}She knows those words never became a reality.{p}That's why her hand is shaking.{w=1.0} That's why I can feel the guilt radiate from her, both from the performance and herself.{p}I'm sure she's also feeling my pain of abandonment."
    Exa "\"I'm sorry.\""
    ChuniNar "Is all she could muster."
    nvl clear
    Chuni "\"Don't be, it wasn't your fault.\""
    ChuniNar "We both know it wasn't her choice to make.{p}Exa takes a deep breath."
    Exa "\"Right.{w=1.0} Let's continue on.\""
    ChuniNar "She continues pulling me along the path."
    nvl clear
    ChuniNar "Another flickering light.{p}Another memory.{p}This time, it is not of my own.{p}Unfamiliar people play out an unfamiliar scene, yet the emotions still wash over me all the same."
    ChuniNar  "Due to an error beyond her control, she was blamed for the company’s closure and lost her job, the one she tried so hard to get and maintain.{p}No one believed in her pleas.{p}No one understood her attempts.{p}She was kicked out of what remained with nothing."
    nvl clear
    ChuniNar "Another flickering light.{p}Another memory, one not of my own."
    ChuniNar "Her partner slams a chunk of papers in front of her.{p}The regret and embarrassment of it all began to radiate from within me.{p}Despite her protests and attempts at mending the situation, this was the outcome she was forced to accept."
    nvl clear
    ChuniNar "Another flickering light.{p}Another memory."
    ChuniNar "This time, the light pulsed to the beat of the heart monitors.{p}This machine was hooked up to two specific people, one of the last ones she had the will to care for.{p}She tried her best, and yet her care wasn’t enough.{p}The monitors flattened out, as did the light."
    nvl clear
    ChuniNar "Another light.{p}No one remained by her side.{p}The very last people she thought would be at her side spilled away from her in all directions.{p}Her brothers, sisters, relatives, all walked away."
    ChuniNar "She was left alone, by everyone, by everything.{p}And so, she stood there."
    ChuniNar "All of the anger, all of the sorrow, all of it.{p}She made her way forward."
    nvl clear
    ChuniNarCnt "As did I, as did we. Exa snapped me out of my trance."
    nvl clear
    Exa "\"Mio!{w=1.5} Mio please!!!{w=1.0} You're still alive, right!\""
    ChuniNar "Tears were streaming down her face."
    ExaCont "\"You're still with me, right?{w=1.0} Right?!\""
    nvl clear
    Chuni "\"Yes,{w=1.0} yes.{w=2.0} I'm{cps=3}...{/cps}{w=0.5} I'm still here Exa.\""
    ChuniNar "I try to tighten the grasp on her hand, only for my muscles to fail me.{p}That was the first domino."
    scene forest1
    ChuniNar "Everything else began to fail as all of the feelings pured over me at once.{p}Everything felt off.{p}The world was upside down.{p}My {i}skin{/i} was inside out.{p}The air felt on fire.{p}My guts turned to inflated mush."
    nvl clear
    ChuniNarCnt "Someone chose to be alive, after experiencing all that?"
    nvl clear
    ChuniNar "Exa carried my limping self to what seemed to be a pool of water, surrounded by four lampposts, one in each corner of the pool"
    Exa "\"This is the last one.{w=1.0} I know it has been tough, but this time I am here.\""
    ChuniNar "She makes me look into her eyes."
    ExaCont "\"This time,{w=1.0} I will be there with you, until the very end.\""
    nvl clear
    ChuniNar "That's all she says.{p}She continues to support me as we stare out into the pool."
    ChuniNar "I take note of the stone monument placed before us.{p}It had an engrave paragraph of text that looked unrecognisable to my eyes."
    ChuniNar "We come a little closer, close enough to see our reflections in the water."
    nvl clear
    ChuniNar "In the reflection I do not see myself, nor Exa.{p}Instead I see a figure, one that feels eerily familiar."
    ChuniNar "The four lampposts begin to flicker.{p}The stone text comes to life.{p}The final show begins."
    nvl clear
    scene black
    with pixellate
    nn "{i}After suffering a job loss, romantic failure beyond repair, death of her parents, disappointment and rejection of her brothers and sisters, failures to keep up with life at all, there was no one else that would take her in.{/i}"
    nn "{i}She had to roam the streets on the outskirts, near this very forest.{p}After trying to seek help again and again, with all of her options withdrawn, she reached for the stars in a final ditch attempt at some salvation.{/i}"
    nvl clear
    nn "{i}She closed her eyes and tried to grasp at anything that might save her.{p}Once she felt her feelings get across to the stars, she opened her eyes and looked back down on the earth.{/i}"
    nn "{i}That’s when she came across an axe.{/i}"
    nvl clear
    nn "{i}An axe, of all things, was the first thing that she saw after she prayed to the heavens, to the aliens that she believed in as a child, the ones that supposedly gave her those powers.{p}She took this sight as her answer.{/i}"
    nn "{i}Using the remaining belief in that power she once had, she took matters into her own hands and sought an ending she believed in.{p}She swung at her own head.{/i}"
    nvl clear
    nc "{i}And with a dull sounding thud-{/i}"

    scene chunni1
    with pixellate
    nvl clear
    ChuniNar "-I awoke in my room.{p}Exa was no longer by my side."
    ChuniNar "Why...?{p}Why am I back here?{p}How am I back here?{p}Before the confusion took over, I ran for the door to try step outside again."
    nvl clear
    ChuniNarCnt "..."
    nvl clear
    ChuniNar "It's locked.{p}I can't leave.{p}The panic takes over."
    ChuniNar "Why?{p}Why??{p}Why?!"
    nvl clear
    ChuniNarCnt "..."
    nvl clear
    ChuniNar "A key...{w=1.0} Right, a key.{p}There has to be a key somewhere here, right?{p}{i}Right?!{/i}Even if I have to flip this whole room upside down,{w=1.0} I have to find it!"
    nvl clear


    #Chapter 3-2
label shiok:
    with pixellate
    nvl clear
    TBNar "The sudden noise of items being thrown around startled her. This noise serves as the most unnerving confirmation possible."
    nvl clear
    TBNar "There is someone else inside this house.{p}"
    TBNar "It came from the locked room, the one that is never supposed to be opened."
    nvl clear
    TBNar "She took arms and went up to the door and put {i}Her{/i} ear up towards it."
    nvl clear
    ChuniNar "“Come on… come on! Where is it?!”"
    nvl clear
    TBNar "...could be heard just beyond this one boundary.{p}"
    TBNar "She knew what this voice was. {w=1.0}She knew that the barrier has broken down."
    TBNar "She was now at an impasse."
    TBNar "Either she walks away, or she opens the door."
    nvl clear
    ChuniNar "“Damn it… where is Exa!?”"
    nvl clear
    TBNar "More shouts from beyond the door."
    TBNar "She put her hand on the door handle.{w=0.5} It is still locked firmly."
    TBNar "She lifts her hand up off the handle."
    nvl clear
    ChuniNar "“{cps=14}Please!{w=0.1} Please!{/cps} {w=1.0} It has to be here somewhere!”"
    TBNar "It’s a kind of desperation she went through herself."
    nvl clear
    TBNar "Ah. Her empathy is flaring up again, that emotion she tried but failed to kill off."
    ChuniNar "Ah!{w=0.4} That’s right!"
    TBNar "A shout came from the other side... {w=0.5}Then silence."
    nvl clear
    TBNar "She knew this feeling. {w=0.5}The person on the other side was starting up those powers."
    TBNar "Instinctually, she flung the door open."
    TBNar "What was inside was the remains of {i}Her{/i} past, holding her hand up at the door."
    nvl clear
    TBNar "The two locked in on each other. {w=0.4}{i}Her{/i} arm twitches as if she wanted to close the door on instinct but {i}Her{/i} shock stopped {i}Her{/i} arm from working correctly."
    ChuniNar "“It’s you.”"
    TBNar "The younger self states the obvious."
    TBNar "The older self tried to slam the door shut but the younger self was too quick."
    TBNar "The young girl breaks the stalemate and dashes towards the door."
    nvl clear
    TBNar "It takes a second for the older one to come to her senses and tries to slam the door shut,{w=0.4} only for the young girl to make it in time and successfully prevent the door from closing with her foot."
    TBNar "{nw}{w=0.3}It’s official now.{p}"
    TBNar "The sealed self has escaped containment."
    nvl clear
    TBNar "The woman was forced to back off and draw her gun on the younger one’s entrance. {p}{p}However, instead of reacting with panic, the young girl simply erects a barrier with her bandage written arm."
    TBNarCnt "Shooting it renders the shot ineffective."
    nvl clear
    TBNar "Knowing she’s now at a disadvantage, the older self exited out of the building and out into the open."
    TBNar "The young girl wordlessly followed her out."
    nvl clear
    TBNar "The two now stood, {w=0.5}surrounded by sunset tinted trees."
    TBNar "The older one knew that this was her last stand. {w=0.5}She could not escape into the forest."
    TBNar "The trees marked where her domain ended."
    TBNar "If she were to step outside, she knows that she’ll return to the real world."
    TBNar "She would rather {shader=jitter}{b}die{/b}{/shader} than face reality ever again."
    nvl clear
    TBNar "And so, she raised her right arm up, {w=0.5}still holding that sawed off shotgun, {w=0.4}closed her eyes, {w=0.6}and focused her mind."
    TBNar "It felt... {w=0.5}nostalgic{w=0.4}, that’s how long it was since the older one used this kind of power."
    TBNar "She remembered the activation phase with ease."
    nvl clear
    TBNar "What is the target?"
    ChuniNar "{fast}...The younger me."
    TBNar "What is the goal?"
    ChuniNar "{fast}...To stop this scene."
    TBNar "What do you feel?"
    ChuniNar "{fast}...I fee{cps=5}l...{/cps}{w=1.0} like I need to disappear."
    nvl clear
    ExaCont "“Are you sure about that?”"
    TBNar "A boastful voice appeared right before the older self, seemingly out of nowhere."
    TBNar "It was Exa. {w=0.6}She forcefully stopped the command."
    ChuniNar "“It just had to be you again...”"
    TBNar "With this, {w=0.3}the older self summoned her axe,{w=0.3} and began to swing wildly at Exa. {w=0.7} She dodged all of the swings with ease."
    nvl clear
    ExaCont "“Again, Mio,{w=0.5} I’m sorry I wasn’t there for you."
    extend "I’m here to make it up to you.”"
    MioNar "“You can make it up to me by leaving!!! {w=0.5}I don’t need you now!”"
    ExaCont "“You do need me, {w=0.5}you just need to open yourself-”"
    nvl clear
    MioNarCnt "{shader=jitter}{b}“Not happening!”{/b}{/shader}"
    TBNar "A surprise shot was fired at Exa, but the younger one blocks it again. {w=0.4}Exa continues to speak while closing the distance."
    nvl clear
    ExaCont "“I saw it all, Mio. {w=0.5}I saw your struggles, {w=0.5}and I know I broke my promise to you. {w=0.5}But then you gave me this chance,{w=0.4} this very space to help you.”"
    ExaCont "“A space that's only accessible by people like us, regardless of physical boundaries.{w=0.5} It's almost as if you were inviting me in.”"
    nvl clear
    MioNar "“Shut up! No I wasn't!”"
    ExaCont "“Still stubborn till the very end ey? {w=0.4}Right, Mio. {w=0.6}You're up!”"
    TBNar "The two who bore the name shot their eyes at Exa."
    ExaCont "“Right, there's two of you now... {w=1}Young Mio!”"
    nvl clear
    TBNar "She beckonned her over."
    ExaCont "“Only you can now sav{cps=8}e...{/cps}{w=0.6} yourself.{w=1.0} I've done all I can. {w=0.5}The rest is up to you.”"
    MioNar "{i}“...right.”{/i}"
    TBNar "Exa raised her hand, as if she were asking for a high five.{w=0.5} Young Mio met that expectation and tagged herself in."
    nvl clear
    TBNar "The two once again stared at each other, {w=0.4}with young Mio staring down due to Old Mio currently laying on the ground."
    MioNar "{i}“I saw those memories too.”{/i}"
    MioNar "“Did you now? {w=0.4}So you must know how I feel.”"
    MioNar "{i}“I do. {w=0.8}I really do. {w=0.8} After all...”{/i}"
    MioNarCnt "“{i}I'm {b}you{/b}.”{/i}"
    nvl clear
    MioNar "“More like we are me.”"
    MioNar "{i}“Something to that extent.”{/i}"
    MioNar "“So you must know that I'm not leaving.”"
    TBNar "Old Mio still digs her heels in."
    nvl clear
    MioNar "{i}“Even with everything gone, you still want to stay here?”{/i}"
    MioNar "“Correct. {w=0.5}I get to live by my own terms here.”"
    MioNar "{i}“So...{w=0.5} you've fully converted to being an earthling.”{/i}"
    MioNar "“...huh?”"
    nvl clear
    MioNar "{i}“You've accepted being human.{w=0.5} You abandoned your pledge to {b}The Organisation{/b}.”{/i}"
    MioNar "“This organisation business again...{w=0.5} of course you'd still be into it.”"
    TBNar "Young Mio shoots her right hand up into the sky,{w=0.3} and began forming a ball of light in the palm of her hand. "
    MioNar "{i}“It seems that the harshness of reality made you forget.”{/i}"
    MioNar "“Forge{cps=8}t...{/cps}{w=0.4} what?”"
    nvl clear
    MioNar "{i}“I'll show you. {w=1.0}Look up.”{/i}"
    TBNar "The sun set just beyond the horizon, allowing the stars of the night to begin peeking beyond the yellow curtains."
    TBNar "Mio's ball of light began resonating with the stars above.{w=0.5} They all began to flicker as they transmit a memory this Old Mio forgot."
    nvl clear
    ExaCont "“Mio,{w=1.0} do you believe in miracles?”"
    MioNar "“Exa,{w=0.6} please, {w=1.0}with our powers,{w=0.6} any miracle can happen at any time.”"
    ExaCont "“I want you to believe in that power Mio.”"
    TBNar "Exa grabbed her hands and pressed them together."
    nvl clear
    MioNar "“Eh? {w=0.8}Where is this coming from?”"
    TBNar "Exa symboled to stay quiet and continued."
    nvl clear
    ExaCont "“If there ever comes a time for it...{w=0.8} I want you to believe in the biggest miracle you can.”"
    MioNar "“The biggest?”"
    ExaCont "“The biggest...”"
    ExaCont "“...whatever is in your heart...”"
    ExaCont "“...whatever truth you desire the most...”"
    ExaCont "“I want you to wish for it with all your might.”"
    nvl clear
    TBNar "Exa paused for dramatic effect."
    ExaCont "“Of course,{w=0.6} you know this is not how our powers work. {w=0.6}Only after someone has devoted themselves to their path fully,{w=0.6} and seen the end of it,{w=0.6} only then can a miracle be granted.”"
    TBNar "Mio remained confused,{w=0.5} even after attempting to process this vague information."
    nvl clear
    MioNar "{i}“Doesn't the end of a path imply a successful journey?”{/i}"
    ExaCont "“It could also mean a dead end. {w=0.5}With our powers,{w=0.6} we can defy fate and mold our happy endings into reality.”"
    TBNar "Mio begins gathering a ball of energy around her hands."
    ExaCont "“But only after we put in the sufficient amount of work.{w=0.6} Something in exchange for something.{w=0.5} The greater the effort,{w=0.2} the greater the reward.”"
    nvl clear
    MioNar "{i}“So I still need to work?”{/i}"
    ExaCont "“Of course.{w=0.4} That is how we stay human,{w=0.15} despite our magical powers.{w=0.5} No freebies.”"
    MioNar "{i}“...okay.{w=0.5} I understand.{w=0.6} I think.” {/i}"
    TBNar "Exa shut off Mio's ball of energy, and began to stretch."
    nvl clear
    ExaCont "“Good good, got the message across. {w=0.6}Seriously,{w=0.5} never doing that serious business again!{w=0.5} {b}Unless!{/b} {w=0.6}It is serious business!”"
    TBNar "That's where the transmission ends."
    MioNar "“It's all so obvious in retrospect.”{nw}"
    TBNar "...admits Old Mio."
    nvl clear
    ExaCont "“Mio, {w=0.8}do you believe in miracles?”{nw}"
    TBNar "Asks Exa as she stretched out her hand to the Old Mio.{w} Young Mio follows suit."
    MioNar "“... absolutely.”"
    TBNar "She accepts both the hands, which pull her up. {w=0.5}Now everyone is linked."
    nvl clear
label current: #This is for testing only.
    ExaCont "“Well then,{w=0.8} here it is.{w=1.0} Your own {shader=jitter}miracle{/shader}.”"
    TBNar "And the whole world faded to black...{w=1.0}"
    scene black
    with end_fade
    nvl clear
    ExaCont "“Found you.”{nw}"
    TBNar "..she whispered to Mio, and smiles warmly."
    TBNar "Stars twinkle behind Exa."
    nvl clear
    MioNar "“...took you long enough.”{nw}"
    TBNar "...replied Mio in a raspy voice."
    ExaContCnt "{cps=14}“Welcome back...”{/cps}"
    scene black
    with end_fade

    # This ends the game.

    return
