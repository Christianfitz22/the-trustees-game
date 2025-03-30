init:
    # Screen configuration.
    $ config.screen_width = 1920
    $ config.screen_height = 1080
    $ config.window_title = "Oath"

    # Background images
    image bg_black = "bg_black.png"
    image bg_princess_room_day = "SoJ2025BedroomDayDestaturated.png"
    image bg_princess_room_night = "SoJ2025BedroomNightDesaturated.png"
    image bg_garden = "SoJ2025GardenDayDesaturated.png"
    image bg_throne_room = "SoJ2025ThroneRoomBrightDesaturated.png"
    image bg_throne_room_night = "SoJ2025ThroneRoomNightDesaturated.png"

    # CG Images
    image cg_garden = "SliceOfJamCGGarden.png"  # Fixed typo here
    image cg_gay = "CG.png"
    image cg_knight_duel = "knightfighting.png"
    image cg_princess_on_throne = "SliceOfJamCGThroneRefuse.png"
    image cg_princess_on_throne_v2 = "SliceOfJamCGThroneKill.png"

    # Assassin sprites
    image assassin_neutral = "assassin_neutral.png"
    image assassin_fearful = "assassin_fearful.png"

    # Princess sprites 
    image princess_neutral = "princess_neutral.png"
    image princess_cheerful = "princess_happy.png"
    image princess_disapproving = "princess_disapproving.png"
    image princess_knife = "princess_knife.png"
    image princess_bloodied = "princess_bloodied.png"

    # Hawthorn
    image hawthorn_netural = "knight_neutral.png"

    # Character definitions
    define p = Character("Princess Primrose")
    define h = Character("Hawthorn")
    define l = Character("Letter")
    define a = Character("Assassin")

label start:
    $ no_count = 0
    $ no_task1 = False

    scene bg_black
    show hawthorn_netural at center
    "You are Hawthorn, a knight in the employ of Princess Primrose. With your skills, and a little bit of luck, you’ve been appointed as her personal knight."
    "Princess Primrose is considered a beloved Princess by the people, but you’ve never spoken to her before. It might be a little nerve wracking, but she’s the only heir to this Kingdom. Better not mess this up!"
    hide hawthorn_netural
    jump task1

# --------------------------
# Task 1
# --------------------------
label task1:
    scene bg_black
    centered "Day 1"
    scene bg_princess_room_day
    "A neatly written letter is left in the Princess’ room when you arrive. It’s addressed to you."
    menu:
            "Read Letter":
                jump task1_read_letter

label task1_read_letter:
    l "Dearest Hawthorn,"
    l "I hope that the day has been treating you well. I wish we could have a proper introduction, but I’ve been busy these last few days."
    l "Today, however, is the first time I have a task for you! The roses have finally begun to bloom. The gardeners have done a fine job taking care of them."
    l "I should like to see them. Come escort me in the garden! It will be a nice change of pace."
    l "Yours, Princess Primrose."
    l "It’s signed off with the Princess’ personal seal."
    menu:
            "Go to the Garden":
                jump task1_garden
            "Ignore her command":
                $ no_task1 = True
                jump task1_ignore

label task1_garden:
    scene bg_black
    "You rush to the garden as per her orders. Better not be late!"
    scene bg_garden
    show princess_neutral at center
    p "You're here! That was fast."
    hide princess_neutral
    h "It's an honor to serve you, Princess."
    show princess_cheerful at center
    p "I'm glad to hear it. Come, now. The gardener has put his heart and soul into this garden. Look at all the variety!"
    hide princess_cheerful
    show cg_garden with dissolve
    "The Princess walks with grace, pointing out the various flowers with a childlike excitement."
    p "See these? I hear they are a nightmare to take care of. Yet here they bloom so well! They will wilt in a week after blooming, and the fruits they produce aren’t edible—consider yourself lucky to see them."
    p "And, oh! Look at these roses! It's my dream to have a garden with every variety available."
    scene bg_garden
    show princess_cheerful at center
    p "Thank you for spending your time with me. I hope you had as good a time as I did!"
    hide princess_cheerful
    show princess_neutral at center
    p "I have to get back to my duties now… Oh well. All good things must end."
    hide princess_neutral
    "She sends you off with a smile."
    jump task2_intro

label task1_ignore:
    scene bg_black
    "You decide to ignore her command. The Princess’ garden is perfectly safe, anyway. You can spend your time doing something more important."
    "Time flies by, and soon you’re informed by a stern attendant that the Princess has requested your presence."
    "Since it’s a direct command, you suppose you can’t ignore her this time."
    scene bg_princess_room_night
    show princess_disapproving at center
    p "Where in the world were you? Did you not read the letter?"
    p "I cannot believe that my escort knight would be so flippant! What if I had been in danger?"
    p "It was not even that difficult of a task! Butler! I require a new escort knight at once."
    p "I can’t believe this."
    p "…? Why are you still here? Go on, now. You’re dismissed!"
    jump ending1

# --------------------------
# Task 2
# --------------------------
label task2_intro:
    scene bg_black
    centered "Day 2"
    "You wake up to the call of your Captain, telling you to report to the Princess’ room at once."
    "Tossing on your uniform, you rush to the Princess’ bedroom."
    scene bg_princess_room_day
    show princess_neutral at center
    p "Oh, Hawthorn, you're here…"
    hide princess_neutral
    p "I've drafted up a few new policies for the populace, but it looks like they weren't received well."
    p "Thankfully, it seems we can control the situation since it wasn’t actually enacted yet…"
    show princess_disapproving at center
    p "It's a necessary change! The backlash is all because of a misunderstanding."
    hide princess_disapproving
    show princess_neutral at center
    p "…Might you stay with me while I deal with the situation?"
    hide princess_neutral
    menu:
            "Stay With Her":
                jump task2_stay
            "Ignore Her Request":
                $ no_count += 1
                jump task2_ignore

label task2_stay:
    scene bg_black
    "You stay with the Princess as she works through revisions of her policy. Time passes as she chats with you."
    "Even though you're not much help with legalese, she seems much more at ease by the time the sun sets."
    "You suppose this is part of the job."
    scene bg_princess_room_night
    show princess_neutral at center
    p "I was far more productive than I thought I would be!"
    hide princess_neutral
    show princess_cheerful at center
    p "Surely, the populace will be pleased with my decisions now."
    hide princess_cheerful
    show princess_neutral at center
    p "Or at least, I hope so…"
    hide princess_neutral
    show princess_cheerful at center
    p "Either way, your presence was a great comfort to me. Even if the peasantry does not approve of my choices, I feel as though I am not alone."
    p "Thank you."
    hide princess_cheerful
    jump task3_intro

label task2_ignore:
    show princess_disapproving at center
    p "Are you really leaving me alone in my time of need?"
    hide princess_disapproving
    p "I just need you as support! I haven’t asked you for much…"
    p "Goodness! You are just like the peasantry."
    show princess_neutral at center
    p "I shouldn’t have expected better of you, or them."
    hide princess_neutral
    show princess_disapproving at center
    p "Oh, well, and I was just starting to like you..."
    hide princess_disapproving
    scene bg_black
    "You leave the Princess, as she huffs and dismisses you with a wave of her hand. There’s not much else you can do."
    "You return to your quarters, having no other orders for the day."
    jump task3_intro

# --------------------------
# Task 3
# --------------------------
label task3_intro:
    scene bg_black
    "Even though you’ve gotten more accustomed to being called on at random by the Princess, today there is no one in her bedroom when you arrive."
    "Not that it is strange, after all. She could just be at court, speaking with friends, or any number of activities."
    "But, just like your first day on the job, there is a letter addressed to you on her desk."
    scene bg_princess_room_day
    l "Dearest Hawthorn,"
    l "My apologies for being unable to greet you this morning! The court is in a fuss at the moment with the arrival of a beast to the East."
    l "Now isn’t that something! I thought that our borders were safe, but it seems not."
    l "This could pose a big problem to those on the outskirts, so I would like to send you and some other knights to head out and slay it."
    l "Yours, Princess Primrose."
    menu: 
        "Head Out With the Squadron":
            jump task3_head_out
        "Stay At Home":
            jump task3_stay_home

label task3_head_out:
    scene bg_black
    "This is what you’ve been training for! Heading out with the squadron, you feel as though you are making a difference." 
    "The fight is difficult, but not impossible. With your squadron at your side, you are able to pierce the heart of the beast after a struggle."
    "In order to prove your victory to the Princess, you take the pelt of the beast as your prize."
    scene bg_princess_room_night
    show princess_neutral at center
    p "Welcome back, my knight! Are you unharmed?"
    "You present Princess Primrose with your prize and proof."
    hide princess_neutral
    show princess_cheerful at center
    p "Goodness! What a beautiful pelt. I am sure my seamstress will make a fine piece of clothing with this… "
    p "Thank you, Hawthorn!"
    hide princess_cheerful
    show princess_neutral at center
    p "The border villagers thank you for your service. You must be tired."
    p "Make sure to rest well, and get treated for any injuries you sustained."
    "She sends you a warm smile, before you bow to her and leave." 
    hide princess_neutral
    show princess_cheerful at center
    "You see her hold up the pelt, pleased at your offering." 

label task3_stay_home
    scene bg_black
    "That sounds dangerous, you decide, and so you stay at home. The Princess is too busy to check if you went, you think, so there’s no danger in skipping!"
    "From what you hear, it was a good call. Many of the knights who headed out came back injured, though the beast was successfully slain." 
    "Unfortunately, because of how difficult the fight was, there’s no proof."

    scene bg_princess_room_night
    show princess_neutral at center
    p "How did the fight go?"
    h "..."
    hide princess_neutral
    show princess_cheerful at center
    p "Just kidding! I read the report. Your name is strangely missing."
    hide princess_cheerful
    show princess_disapproving at center
    p "ithout your help, there were a great many casualties."
    p "You have your responsibilities, you know. You were supposed to help the fight against the beast."
    p "Being my escort knight isn’t just fun and games."

# --------------------------
# Task 4
# --------------------------
label task4_intro:
    scene bg_black
    centered "Day 4"
    "There is never truly peace in the palace, but lately the chaos has been more intense."
    "Being the escort knight of Princess Primrose, you soon learn that she and a noble have been feuding. While she claims he’s undermined her authority, he denies it."
    "It’s inevitable that you will be drawn into the conflict."
    scene bg_princess_room_day
    l "Dearest Hawthorn,"
    l "There is someone who has been getting on my nerves recently! I trust that someone as loyal as you already knows why."
    l "Nevertheless, I cannot let this stand. I am the Crown Princess, and I must be treated as such."
    l "We have agreed on a duel to settle this honorably. As my escort knight, I have nominated you to represent me. I should hope you will not disappoint."
    l "Yours, Princess Primrose."
    menu:
            "Accept the Nomination":
                jump task4_accept
            "Refuse the Nomination":
                $ no_count += 1
                jump task4_refuse

label task4_accept:
    scene bg_black
    "This is your duty—what an escort knight is for. With high expectations, you head to the duel grounds."
    show cg_knight_duel with dissolve
    "You and your opponent clash fiercely. You are better trained, better geared, and in higher spirits."
    "As you fight, you spot an opening. You raise your sword and..."
    scene bg_black
    "The knight you dueled is mortally wounded. Your strike was true—he’s left for dead."
    "Their blood is on your hands."
    scene bg_princess_room_night
    show princess_neutral at center
    p "Congratulations, Hawthorn! You have won the duel in my honor."
    hide princess_neutral
    show princess_cheerful at center
    p "I can't ask for a better escort knight."
    hide princess_cheerful
    h "…"
    p "Your opponent's death has cost more than victory—it means my rival has lost face before the entire court."
    p "You have my thanks, my knight."
    jump task5_intro

label task4_refuse:
    scene bg_black
    "You can’t accept this. It’s a waste of your talents—and too dangerous. You instruct a servant to relay your refusal, then return to training."
    "Later, you learn the Princess’ other nominee has won the duel, but her disappointment remains palpable."
    scene bg_princess_room_night
    show princess_disapproving at center
    p "Where were you, Hawthorn? You are my escort knight—meant to represent me!"
    hide princess_disapproving
    jump task5_intro

# --------------------------
# Task 5
# --------------------------
label task5_intro:
    scene bg_black
    centered "Day 5"
    "Unrest has become the norm. Nights are rough as you see the Princess tired from her duties—and you, too, feel the strain."
    "Yet your troubled sleep brings vivid dreams. In one, you see Princess Primrose seated on a throne."
    "You approach the throne, kneeling a few paces before her."
    "She stands, ordering you to lift your head and face her."
    "As you follow her command, she covers her soft laugh as you see her beautiful face smile down upon you. Just as she opens her mouth to speak, a glint catches the corner of your eye —"
    "BANG BANG BANG!"
    "Your eyes snap open."
    "Messenger (no sprite): Knight Hawthorn! You have an urgent summons from the Princess!"
    "Instinctively, you toss the bed sheets aside and start putting on your gear, replaying what little you remember of your dream over and over in your mind."
    scene bg_princess_room_day
    show  princess_sad at center
    p "This is not how it’s supposed to go…"
    hide  princess_sad
    show princess_neutral at center
    p "Hawthorn! At last, you’ve finally arrived!"
    p "I’m sorry to call you so early in the morning, but there’s been some trouble in the Kingdom."
    hide princess_neutral
    show princess_sad at center
    p "Even though I worked so hard on the revisions, it seems my policies are still not popular with the people."
    p "My informants tell me that the peasantry have decided to rise up and stage a rebellion against the Crown."
    p "I tried so hard…"
    hide princess_sad
    show princess_disapproving at center
    p "Even if they are unhappy with the results, they are causing chaos and destruction."
    p "They must be stopped as soon as possible, or else they might reach the capital."
    hide princess_disapproving
    show princess_neutral at center
    p "Hawthorn, I would like you to head out and lead the force against them."
    p "For the good of the Kingdom."
    hide princess_neutral
    menu:
            "Quell the rebellion":
                jump task5_quell
            "Ignore the rebellion":
                jump task5_ignore

label task5_quell:
    scene bg_black
    "How dare they! A rebellion was treason by definition, and it’s your job to bring such evildoers to justice."
    "You are Princess Primrose’s escort knight! You must stop all those who want to do her harm. And… well, you keep thinking back on your dream."
    "Leading the charge, you find the headquarters of those who dared to rise up against the Crown and bring them justice."
    "They do not go down without a fight, and you are not able to ensure that all the civilians remain unharmed during the battle."
    "…"
    "When you return to the palace, you are shaken, but successful."
    scene bg_princess_room_night
    show princess_cheerful at center
    p "Hawthorn! I’ve heard the good news. You’ve successfully dealt with all the insurgents."
    
    p "Congratulations! A celebration must be in order."
    hide princess_cheerful
    h "Princess, I…"
    show  princess_sad at center
    p "Hawthorn, is everything alright? You look a little sad."
    h "I wasn’t able to protect the people while I fought the rebellion."
    h "People died."
    hide  princess_sad
    show princess_neutral at center
    p "..."
    hide princess_neutral
    show princess_cheerful at center
    p "Is that it? Oh, Hawthorn, you worry too much!"
    p "You did your best, and the most important thing is that you were successful."
    hide princess_cheerful
    show princess_disapproving at center
    p "It’s the fault of the rebellion that people died."
    hide princess_disapproving
    show princess_neutral at center
    p "So don’t worry about it at all."
    hide princess_neutral
    show princess_cheerful at center
    p "The insurgents got what they deserved."
    hide princess_cheerful
    jump task6_intro

label task5_ignore:
    scene bg_black
    "It’s not your business. The rebellion is probably not much of an issue, and if they’re mad at the Princess’ policy, all she needs to do is revise them again!"
    "You decide to head back to your quarters and focus on patrolling the palace instead. Keeping the Princess safe is more important."
    scene bg_princess_room_night
    show princess_disapproving at center
    p "The rebellion is growing as we speak. Why didn’t you head out when I told you to?"
    hide princess_disapproving
    p "Now there’s no way we can easily deal with a mob this size!"
    p "Argh! This is why you should have listened to me."
    p "…"
    show princess_disapproving at center
    p "Go away. I don’t want to see you right now."
    hide princess_disapproving
    jump task6_intro

# --------------------------
# Task 6
# --------------------------
label task6_intro:
    scene bg_black
    centered "Day 6"
    "The weight of recent events grows heavier. Unrest simmers in the streets, patrols tighten around the palace, and whispered conversations among the nobles turn grave."
    "Even sleep feels like a luxury now. With your armor and sword at the ready, you roam the palace, ever vigilant."
    "Then one night, a shadowy figure in a cloak slips silently through the corridors toward the Princess’ bedroom. You rush forward."
    scene bg_princess_room_night
    show assassin_neutral at right
    show princess_disapproving at left
    "You catch the intruder just as he stands over the sleeping Princess with a dagger in hand."
    "You shout, startling the Princess awake and catching the assassin off guard. Before he can strike again, you intercept her dagger with your sword."
    "A duel ensues, the clashing of metal filling the room as the Princess watches with a detached air."
    show assassin_fearful at right
    "At last, your training and faith prove strong enough—you triumph over the intruder."
    "The assassin lies disarmed and injured in a corner as the Princess slowly approaches."
    show princess_bloodied at center
    p "Hawthorn… you saved me."
    hide princess_bloodied
    a "If only you hadn’t… you keep letting that monarch live and the crimes against this kingdom's people will never end."
    show princess_disapproving at center
    p "How could you spit such treasonous words? Everything I do, I do for this kingdom."
    hide princess_disapproving
    a "She lies, knight. She commands death for her own pride. She betrays the good of her people to consolidate her power. There is no line she will not cross."
    show princess_disapproving at center
    p "That's enough, villain."
    hide princess_disapproving
    p "Even your words make you an enemy. But to kill me in my sleep? You truly are the worst type of scum."
    p "Hawthorn, kill her."
    show princess_neutral at center
    p "Please."
    hide princess_neutral
    menu:            
        "Execute the Assassin":
            jump task6_execute
        "Arrest the Assassin":
            $ no_count += 1
            jump task6_arrest

label task6_execute:
    scene bg_black
    "No need to tell you twice. Letting an assassin roam around late at night is just asking for trouble. Attempted or not, the fact remains that she had planned to kill someone."
    "She shouldn’t have if she wasn’t ready to face death herself."
    scene bg_princess_room_night
    show assassin_fearful at center
    a "You can’t be serious-!"
    "You quickly dispatch the Assassin."
    h "The danger is gone, Your Highness."
    show princess_neutral at center
    p "Thank you, Hawthorn. I’ll be able to rest well with you guarding me."
    hide princess_neutral
    h "… What should we do about the assassin?"
    show princess_cheerful at center
    p "Don’t worry. I’ll send for a maid to clean up the mess. You should get some rest."
    "You look at the assassin’s body. Calling it a mess seems dismissive. Besides, another thought nags at you…"
    h "Isn’t this against the law? I was supposed to bring her to court."
    show princess_cheerful at center
    p "Don’t worry about that, Hawthorn! This was the best choice. Who knows if she would have tried again if you left her alone."
    "You suppose she is right."
    show princess_neutral at center
    p "You did the right thing."
    hide princess_neutral
    jump task7_intro

label task6_arrest:
    scene bg_black
    "No, that’s not right. Even if the assassin tried to kill the Princess, you are meant to follow the law."
    "You instead simply keep your sword pointed at the assassin."
    h "Guards! Arrest this criminal."
    "Another pair of guards rush in, taking the assassin away. You know that she will likely be tried in the morning, but that isn’t your business."
    scene bg_princess_room_night
    show princess_disapproving at center
    p "That was unnecessary."
    p "It would have been quicker to kill her right here and now."
    p "She would have been executed for treason, anyway, and the trial will just waste everyone’s time."
    h "But the law…"
    show princess_neutral at center
    p "You would be following the law. Just a little… faster."
    show princess_disapproving at center
    p "It would have been better if I didn’t have to worry about her escaping and attacking me again."
    show princess_neutral at center
    p "Continue your patrol."
    show princess_bloodied at center
    p "I hope I can get some sleep tonight…"
    hide princess_bloodied
    jump task7_intro

# --------------------------
# Task 7
# --------------------------
label task7_intro:
    scene bg_black
    centered "Day 7"
    "Once again, you find the Princess’ room empty. It’s become routine—but you always check for a letter addressed to you."
    scene bg_princess_room_day
    l "Dearest Hawthorn,"
    l "Come meet me in the Throne Room. I have an important task for you."
    l "Yours, Princess Primrose."
    "Concerned, you rush to the Throne Room."
    scene bg_throne_room
    show princess_neutral at center
    p "Hawthorn, you are loyal to me, right?"
    hide princess_neutral
    p "This is the most important task I have for you so far."
    p "There is much I need to do. And for that, I need the throne."
    p "Kill the king, my knight."
    menu:
            "Kill the King":
                jump task7_kill_king
            "Refuse":
                $ no_count += 1
                jump task7_refuse

label task7_kill_king:
    scene bg_black
    "There is no need to hesitate. You rush to the throne, draw your sword, and in one swift motion, the King's head is severed cleanly."

    "He is no more. It almost feels too easy."
    scene bg_throne_room
    show princess_neutral at center
    p "What is it, Hawthorn?"
    hide princess_neutral
    h "Please wait a moment, Your Highness."
    "You drag the King’s body away, then drape your cape over the throne to hide the bloodstains."
    show princess_cheerful at center
    p "Oh, my. Thank you!"
    hide princess_cheerful
    show cg_princess_on_throne with dissolve
    "She sits on the throne—it appears as though it has always belonged to her. This is her rightful place."
    "You kneel."
    "If you have refused any of her commands, go to Ending 0. Otherwise, go to Ending 3."
    jump ending3

label task7_refuse:
    scene bg_black
    "Kill the King? Impossible. Though loyal to the Princess, your loyalty to the Kingdom stands firm."
    "Regicide goes against everything you stand for. You make your disapproval known with your stance."
    scene bg_throne_room
    show princess_disapproving at center
    p "…"
    hide princess_disapproving
    show princess_knife at center
    p "I suppose I have to do everything myself."
    hide princess_knife
    show princess_bloodied at center
    p "Long live the King, and all that. Hawthorn! Clean this up."
    hide princess_bloodied
    "You hesitate—after all that has happened, it feels like a coup."
    "Reluctantly, you set the King’s body aside. Blood stains the floor."
    show princess_bloodied at center
    p "Move aside."
    hide princess_bloodied
    show cg_princess_on_throne_v2 with dissolve
    p "Hawthorn, I thought you would be more loyal than this."
    jump determine_ending

label determine_ending:
    if no_count == 0:
        jump ending3
    elif no_count <= 2:
        jump ending0
    else:
        jump ending2

# --------------------------
# Endings
# --------------------------
label ending0:
    scene bg_throne_room
    show princess_disapproving at center
    p "Hawthorn. I have given you many chances, and here is your final one."
    p "I want to know... will you be loyal to me?"
    hide princess_disapproving
    menu:
            "Kneel":
                jump ending3
            "Face her":
                "You cannot accept her as your Queen. You must take some action…"
                "However, you need to prepare yourself first. So you bow."
                "Hopefully it’s enough to convince her."
                jump ending2

label ending1:
    scene bg_black
    "And thus ends your short term as the Princess’ escort knight. Dismissed from your job, you also lose your place as a member of the royal knights."
    "After all, what kind of knight ignores a simple order from their superior? You’re lucky you weren’t banished out of the Kingdom."
    "Still… you can’t afford to stay in the Capital without a job, and so you move to the outskirts. It’s basically exile at this point. Whatever happens with Princess Primrose is high above your paygrade."
    "You live in shame and squalor for the rest of your life."
    return

label ending2:
    scene bg_black
    "You’ve come to the decision that you cannot continue to serve Princess Primrose. For whatever reason, her commands simply don’t sit well with you."
    "Even though you know this is treason, you approach the throne room, hand on the hilt on your sword."
    scene bg_throne_room_night
    show princess_neutral at center
    p "Hawthorn! What are you doing here at this time of night?"
    hide princess_neutral
    "She looks at you in surprise."
    show princess_neutral at center
    p "Is something the matter?"
    hide princess_neutral
    "You steel your nerves, taking one good last look at her."
    scene bg_black
    "..."
    show cg_princess_stabbing with dissolve
    p "Hawthorn… surely you weren’t trying to hurt me, were you?"
    h "…"
    "You can't muster a word, blood loss clouding your vision."
    hide cg_princess_stabbing
    scene bg_throne_room_night
    show princess_bloodied at center
    p "Good night, my knight."
    hide princess_bloodied
    return

label ending3:
    scene bg_black
    "The King is dead, and so Princess Primrose is now the rightful ruler of the Kingdom."
    "You are glad to have been able to serve her all this time… but you worry—does she need you anymore?"
    "As a Queen, she will have leagues of loyal knights. You are just one of them."
    
    scene bg_throne_room
    show princess_cheerful at center
    p "Hawthorn, my loyal knight. I couldn’t have done this without you. You may stand."
    p "What sort of reward would you like? Riches, a title?"
    
    menu:
            "Nothing.":
                pass
            "You.":
                pass

    "Finally, you stand, walking closer to the Princess as she sits on her throne. She smiles, and it is like the sun."
    "You hesitate."
    p "I see. Well, come closer, then. You will have the highest honor in the Kingdom, after me."
    
    show cg_gay with dissolve
    p "My lover."
    
    window hide
    pause 3
    return
