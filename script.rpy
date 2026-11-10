#Start of document. Hi!

define nn = Character(color="#d3e8ea", kind=nvl,what_textalign=0.0)                                                                             #Basic text with no styling
define nc =Character(color="#ffcccc", kind=nvl, what_xalign=0.5, what_yalign=0.5, what_textalign=0.5)                                            #Basic text positioned on center of screen
#Chunni Mio
define Chuni = Character("Mio", who_color='#75F2BF',what_color='#75F2BF',kind=nvl,what_textalign=0.0)                                           #Chunni's voice
define ChuniNar = Character(who_color='#75F2BF',what_color='#75F2BF',kind=nvl,what_textalign=0.0)                                               #Chunni's POV
define ChuniNarCnt = Character(who_color='#75F2BF',what_color='#75F2BF',kind=nvl,what_xalign=0.5, what_yalign=0.5, what_textalign=0.5)          #Chunni's POV center text

#Tomboy Mio
define TB = Character("Unknown", who_color='#DC143C',what_color='#DC143C',kind=nvl,what_textalign=0.0)                                          #Tomboy's Voice (as unknown)
define TBKn = Character("Mio?", who_color='#DC143C',what_color='#DC143C',kind=nvl,what_textalign=0.0)                                           #Tomboy's Voice (as Mio)
define TBNar = Character(who_color='#DC143C',what_color='#DC143C',kind=nvl,what_textalign=0.0)                                                  #Tomboy's POV
define TBNarCnt = Character(who_color='#DC143C',what_color='#DC143C',kind=nvl,what_xalign=0.5, what_yalign=0.5, what_textalign=0.5)             #Tomboy's Pov center Text

#Exa
define ExaUn = Character("Unknown", who_color='#a9a9a9',what_color='#a9a9a9',kind=nvl,what_textalign=0.0)                                       #Exa's Voice (as Unknown)
define Exa = Character("Exa", who_color='#a9a9a9',what_color='#a9a9a9',kind=nvl,what_textalign=0.0)                                             #Exa's Voice
define ExaCont = Character(who_color='#a9a9a9',what_color='#a9a9a9',kind=nvl,what_textalign=0.0)                                                #Exa's Voice (used for continuing so that her name doesn't clog the screen.

#Others
define Bully =Character("Bully", who_color='#DC143C',what_color='#DC143C',kind=nvl,what_textalign=0.0)                                          #Bully's Voice
define School1 = Character("Voice 1",color="#d3e8ea", kind=nvl,what_textalign=0.0)                                                              #Unnamed "Voice"'s Voice
define School2 = Character("Voice 2",color="#d3e8ea", kind=nvl,what_textalign=0.0)
define School3 = Character("Voice 3",color="#d3e8ea", kind=nvl,what_textalign=0.0)

# The game starts here.

label start:

    #show chunni1   Show should be used for characters, not scenes
    scene chunni1
    nvl show dissolve

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
    ChuniNar "Nothing.{p}Nothing.{p}Nothing. Nothing. Nothing.{p}No eyes on me.{p}No nothing.{p}Nothing.{p}Nothing.{p}Nothing."
    nvl clear
    ChuniNar "A new message in the thread snaps me back to look at my computer. I don’t know where my mind was, but the ping pulled me back in.{p}The alien thread has been dead lately as others are preoccupied with their daily activities.{p}Only true losers like myself have the time to talk about our delusions during these hours."

    #Chapter 1-2
    stop music
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


    #Chapter 3-2




    # This ends the game.

    return
