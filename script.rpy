# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Ant", color="#485212")
define l = Character("Luz", color="#3b276b")
define v = Character("Voice", color="#413e47")

# The game starts here.

init:
    $ relationship_meter = 50 # Starting the meter at 50 (neutral).

init:
    image Ant Neutral = "Ant Neutral.png"
    image Luz Neutral = "Luz Neutral.png"

label relationship_status:
    if relationship_meter > 70:
        "The siblings are becoming familiar, their bond growing stonger than ever."
    elif relationship_meter < 30:
        "The bond feels terribly strained."
    else:
        "The tension between them lingers, unresolved but not unbearable."
    
    return

label start:
    # Screen fades in from black to a night-time forest road, the headlights of the car cutting through the mist. Gentle rain falls, and distant thunder rumbles.

    # Camera shifting to inside the car, showing the siblings. The older sister drives while the younger sibling sits in the passenger seat. Radio plays in the back but faintly.
    scene road_misty with fade
    show screen relationship_meter
    play sound "rain_loop.mp3" loop
    play music "melancholy_theme.mp3" fadein 2.0

    # car engine starting up and moving w/ black screen
    
    "{size=-5}Some wounds linger longer than they should.{/size}"
    "{size=-5}Resentment builds in the spaces between words-spoken, unspoken, and swallowed whole.{/size}"
    "{size=-5}For these two siblings, the weight of things done, said, and quietly repressed had festered into something unshakable. Tonight, that weight had surfaced again, threatening to pull them even further apart-or force them to confront all their misunderstandings.{/size}" 

    scene car_interior with dissolve

    play music "car_start.mp3" fadein 1.0 volume 1.0

    show Luz Neutral at left # move up
    show Ant Neutral at right # move up

    l "So, no greeting, huh? No, \"Hey, how are you?\""
    play music "melancholy_theme.mp3" fadein 2.0
    a "(Looking out the window, avoiding her gaze)\n..."
    l "Well?"
    a "(without looking at her)\nSilence is better than pretending, don't you think?"
    a "Just focus on the road."
    l "(Tightening her grip on the steering wheel) \nPretending? You think that's what I'm doing?"


    call Car_ride_choice
    hide screen relationship_meter
    "The tension between them was palpable, heavier than the mist clinging to the edges of the road. Neither noticed the dark shape darting across the road until it was too late."
    jump chapter_one


label chapter_one:

    play sound "rain_loop.mp3" loop
    scene outside_car with fade
    play music "dying_engine" volume 0.2
    
    "The car jolted forward with a loud sputter. The dashboard lights flickered, the engine coughed, and then–silence. Only the sound of rain and the faint crackle of the radio remained."
    l "(angrily smacking the steering wheel)\nGreat. Perfect timing."
    a "(sarcastically)\nGuess it couldn't take the weight of this conversation either."
    "Luz shot Ant a glare before pulling the car to the side of the road and killing the ignition. Both sit in silence, the rain hammering the roof like a relentless drumbeat."

    # [Shifting to Suspense]
    # (The sister opens the door, letting in the sound of rain and the faint rustle of leaves. The forest beyond the road looms dark and heavy with mist.)

    l "(stepping out)\nStay here. I'll check the engine."
    "Ant watched her from the inside, fidgeting with the hem of their jacket."
    a "(muttering)\nYeah, like that's going to fix anything."
    "Luz popped the hood, rain drenching her as she peered inside. She called out over the storm."
    l "It's dead. We're not going anywhere tonight."
    a "(Stepping out of the car reluctantly)\nWhat now? No signal, no help. This just keeps getting better."
    play sound "whispers.mp3" fadein 1.0 volume 0.2
    "A faint whispering sound drifted through the air, barely audible. Both siblings glanced uneasily toward the dark forest beyond the road."
   
    # As Ant and Luz start walking in separate directions, a strange noise echoes through the forest. Both freeze. Ant looks around nervously, while Luz’s confident facade falters.
   
    a "We need to find someone to help us. I'll bet I can find someone faster than you."
    l "(crossing her arms)\nSplitting up? Sure. I wouldn't want to go with you anyway."
    "Before either could take more than a few steps, the whispering grew louder–a haunting melody of indistinct voices."
    a "(looking around nervously)\nDo you hear that?"
    l "(pretending to be tough)\nIt's just the wind. Probably."

    # The camera lingers on in the forest as the siblings reluctantly step off the road and into the shadows. The screen fades to black, with the sound of their footsteps fading into the mist.)

    scene forest_path with fade
    "Realizing they were stranded and unwilling to face the unsettling sounds alone, the siblings ended up exploring together."

    # As they explore, they find a flashlight in an abandoned toolbox. This triggers a notification and adds the item to the inventory.

    a "(picking up the flashlight)\nGuess this will be useful. Unless you're afraid of the dark, Luz?"
    l "(Ignoring the jab)\nLet's just keep moving. There's got to be something out here."

    # [Transition from Chapter 1 to Chapter 2]

    stop music fadeout 2.0
    play music "eerie_theme.mp3" fadein 2.0 loop
    play sound "forest_ambience.mp3" loop

    scene forest_path2 with fade

    "As the siblings stepped deeper into the forest, the path behind them seemed to vanish into the mist. Every step forward felt heavier, as if the forest itself resisted their presence."
    show shadows_forest with fade
    play sound "crunch_leafs.mp3" loop
    "Shadows danced at the edge of their vision, and the air carried whispers—soft, haunting, and impossibly familiar."
    l "Keep up, Ant. We're not stopping every time you get spooked."
    a "(glaring)\nWho says I'm spooked? You're just marching ahead like you know where you're going. Newsflash, ya don't."
    "Despite their bickering, neither could shake the feeling the forest was alive, watching them, waiting for something."

    #show screen relationship_meter
    jump chapter_two


label chapter_two:
    # Chapter 2: The Forest's Secrets
    # [Setting the scene]
    scene overgrown_path with fade
    play sound "whispering_wind.mp3" loop
    "After what felt like hours of walking, the siblings stumbled upon an abandoned path, overgrown and barely visible. The whispers grew louder, threading through the trees like a melody of despair. Occasionally, they caught glimpses of something—shadows that weren't quite human."
    show Ant Neutral at left
    show Luz Neutral at right
    with dissolve

    a "(whispering)\nDid you see that? There's something out there."
    l "(tightening her grip on the flashlight)\nIt's nothing, just your imagination. Let's keep going."
    play sound "flashlight.mp3"
    show haunted_house with fade
    "But the flashlight flickered, casting fleeting glimpses of a crumbling structure in the distance. A house, half consumed by the forest, stood waiting in the clearing. The air felt charged, heavy with secrets and dread."

    call stay_or_split_choice
    call relationship_status
    # show relationship meter status

    # [Both paths converge]
    
    "Inside the decrepit house, they discovered remnants of the past—an old photograph of their great-grandmother, a tattered journal with half-erased writing, and symbols carved into the walls that seemed to pulse faintly in the dim light. The whispers became voices, clearer now, calling their names."
    scene cabin_room with fade
    play sound "creak.mp3" loop

    show Ant Neutral at right
    show Luz Neutral at left

    l "(reading the journal aloud)\n\'The curse thrives on what we bury. Only through the trials can it be broken.\'"
    a "(uneasily)\nTrials? What trials?"
    play sound "floor_crack.mp3"
    scene black with vpunch
    stop sound

    "As if in response, the house shuddered, and the floor beneath them cracked open. The siblings fell, landing in a cavernous expanse that seemed to shift and change, the forest above now a distant memory."
    scene cabin_room with fade
    jump last_chapter

label last_chapter:
    # Chapter 3: Trials of the Forest
    # [Setting the Scene]

    "The cavern around them pulsed with an unnatural glow, the walls shifting like a living thing. A voice, deep and resonant, echoed in the chamber."
    v "You carry the weight of your bloodline—a legacy of pain, secrets, and division. To leave, you must face the truths you've hidden from yourselves and each other."

    # [Trial Explanation]

    "Before them stood two doors, each marked with a symbol: one resembling a heart, the other a heart, the other a broken chain. The voice continued."
    v "One door reveals the truth of your shared past; the other tests the strength of your bond. Choose wisely, for both paths are needed to break the curse."
    l "(whispering)\nTwo doors. Of course it's not simple."
    a "(quietly trying to steady their voice)\nSo…we have to go through both?"
    l "(nods)\nI don't think we have a choice."

    # [First Trial: Shared Past]
    "The siblings stepped through the door marked with the heart, and the world shifted around them. Entering the door marked with the heart, Luz and Ant were plunged into a series of memories. They found themselves standing in their childhood home, the walls distorted and the air heavy with memories."
    "The moments of pain and misunderstanding that had driven them apart, and the unspoken sacrifices Luz made to shield Ant from the worst of their parents' wrath."
    "Fragments of their past materialized before them: their parents arguing in the kitchen, Luz packing her bags in the dead of night, and Ant sitting alone in their room, tears streaming down their face."
    a "(tearfully)\nYou… you never told me. I thought you just left because you didn't care."
    l "I didn't know how to explain it. I thought leaving would… protect you, somehow…."
    "The memories shifted again, revealing Ant's loneliness and their struggle to hold the family together after Luz's departure. Ant's face twisted with suppressed anger and sorrow, the weight of their role pulling them to the brink."
    "The siblings watched as younger Ant held back tears while fixing a broken chair their parents had blamed them for. Luz's hand instinctively reached toward the memory, guilt washing over her."
    l "(whispering)\nYou shouldn't have to do all of that. I…I should have stayed."
    l "(shaking their head)\nAnd I shouldn't have blamed you for leaving. I was caught up in my ways. I didn't try to reason what you were trying to save yourself from."
    "The memory dissolved into light as the siblings reached for each other, their shared pain finally acknowledged. The door reappeared, and they stepped through together."

    # [Second Trial: The Bond]
    "Through the second door, they found themselves in a labyrinth of shifting shadows. The walls pulsed with mocking voices, distorted echoes of their parents' anger and their own arguments."
    v "To move forward, you must rely on each other. Alone, you will fail."
    l "(urgently)\nAnt, I need you to guide me through this. The shadows are blocking my way!"
    a "(steadying themselves)\nJust listen to my voice. We've got this."
    "The siblings navigated the maze together, Luz, relying on Ant to find paths hidden by the shadows. An Ant leaning on Luz's unwavering determination to push forward. Each step required trust, each wrong move threatening to trap them in the labyrinth forever."
    "As they worked together, the shadows began to recede, the mocking voices fading into silence.The walls of the labyrinth crumbled, revealing an open path ahead."
    v "You have faced what was hidden. Now, the forest's hold weakens. The choice remains yours."

    jump check_ending


#label sprites:


# Relationship meter- I will come back to this to fix up decision, etc.
# Major choices + or - 10, Minor choice + or - 5

label Car_ride_choice:
    menu:
        "Keep to yourself":
            $ relationship_meter += 10
            a "(softening their voice)\nI'm just tired, Luz. This conversation can wait."
            l "(pauses)\n...Fine. We'll talk later."
            "The tension eased, if only slightly, as the rain continued to fall."

        "Speak your mind":
            $ relationship_meter -= 10
            stop music fadeout 2.0
            a "(Turning to face her, voice raising)\nThen, what are you doing? I swear, it's like you want me to forget you left me behind."
            l "(Snapping back)\nI didn't have a choice! You don't know what it was like for me, what I had to go through on a day-to-day basis. I needed to get out, or I would've-"
            a "(Cutting her off)\nNeeded to? Yeah, right. You {i}had{/i} a choice, you just wanted to run away."
            a "You ran, and I was blamed for everything. For you leaving. For the chaos. For the silence."
            play sound "rain_loop.mp3" fadein 1.0 volume 3.0
            "The argument grew sharper, the rain pounding harder outside."

    return

label stay_or_split_choice:
    "The siblings paused at the base of the structure, the air heavy with tension. The distant whispering seemed to grow louder, as though urging them forward."
    l "(looking at Ant)\nWe need to check this out. No more hesitating."
    a "(staring at the house)\nYou're seriously thinking this is a good idea?"
    l "(flatly)\nIt's not about good ideas. We're out of options."
    menu:
        "Stay together":
            $ relationship_meter += 10
            l "(looking at Ant)\nAlright, we're not splitting up. I don't trust this place, and honestly, I don't trust you to handle it alone."
            a "(mocking)\nOh, so now you care?"
            l "(dryly)\nDon't flatter yourself. It's a survival instinct."
            "Despite their bickering, they stuck close, the flashlight illuminating the path as they approached the ominous house. Each creak of the floorboards and each whispered sound in the wind made them draw closer together, their bond subtly strengthening against the eerie backdrop."
            
            "Inside the house, their cooperation paid off. They found an old journal tucked under a pile of debris. Its pages spoke of a curse that thrived on division and buried truths. Together, they pieced together fragments of their family's past, their bond growing stronger as they worked through their shared fear."
            a "(quietly)\nMaybe we're better at this than I thought."
            l "(slightly\nsmiling) Don't get used to it."

        "Split up":
            $ relationship_meter -= 10
            l "Let's cover more ground. You head left; I'll check the right side of the house."
            a "(skeptical)\nSplitting up? Have you not seen a single horror movie in your life?"
            l "(flatly)\nWe don't have time for your commentary, Ant. Just stay where I can hear you."
            "The two went their separate ways, each stepping into the unknown. The whispers seemed to intensify, and the darkness felt thicker. Ant struggled to keep their nerves steady, while Luz kept glancing over her shoulder, trying to shake the unease that had taken root in her chest."

            "In their separate searches, both siblings encountered disturbing sights. Ant found a cracked mirror showing a distorted version of themself, its reflection whispering cruel truths about loneliness and blame. Luz uncovered an old family photograph with a faint shadow of their great-grandmother, her expression grim and knowing."
            a "(starting to panic)\nLuz! I... I don't think we should be alone right now."
            l "(returning, shaken)\nYeah. Let's not do that again."
            "Their reunion was marked by tension and relief, their fears temporarily set aside as they pressed on."
    
    return


# The ending is based on the relationship meter.

label check_ending:
    if relationship_meter >= 70:
        jump good_ending
    elif relationship_meter <=30:
        jump bad_ending
    else:
        jump neutral_ending


label good_ending:
        "{size=+5}Ending 1: Reconciliation (Good Ending){/size}" 
        l "(softly)\nWe… we did it. Together."
        a "(nodding)\nI'm sorry, Luz. For everything. For blaming you."
        l "(sincerely)\nAnd I'm sorry for leaving. I thought I was protecting you, but I only hurt you more."
        "The siblings embraced, their bond stronger than ever. The forest released them, the mist dissipating to reveal the road they had traveled before. The cycle of pain had ended, and the curse was broken."
        call show_meter

        return

label neutral_ending:
        "{size=+5}Ending 2: Uneasy Balance (Neutral Ending){/size}" 
        l "(hesitantly)\nWe made it out...but it doens't feel over, does it?."
        a "(quietly)\nNo. There's still so much we haven't said. So much we haven't faced."
        "The siblings emerged from the forest together, but the mist clung faintly to their footsteps. The trials had forced them to confront their pain, yet the resolution felt incomplete."
        v "The curse wanes, but its roots linger. Healing is a journey, not a moment."
        "They galnced at each other, their expressions caught between relief and uncertainty. The forest had released them, but the bond they shared was only partially mended."
        "As they walked away, the silence was not as heavy as before, but it wasn't entirely lifted. The road ahead stretched long, the echoes of the forest fading, but not entirely forgotten."
        call show_meter

        return

label bad_ending:
        "{size=+5}Ending 3: Division (Bad Ending){/size}" 
        l "(flatly)\nWell, we survived. That's something."
        a "(coldly)\nBarely. And only because we had to."
        "The bond between them remained fractured, the trials only deepening the cracks. The forest released them, but it's whispers lingered, a reminder of the wounds they refused to heal."
        v "The curse is lifted, but its echoes remain. The pain you carry will shape the path ahead."
        "As they walked away from the forest, the silence between them was heavier than ever, the shadow of their journey stretching far behind."
        call show_meter
       
        return

label show_meter:
    "Your final relationship score was [relationship_meter]."

    return


    # This ends the game.

return
