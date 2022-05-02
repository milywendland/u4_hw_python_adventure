# Create your own adventure with python here

"""
idk why it makes me do this
"""


def game():

    print("""
    WELCOME! WELCOME! Its Time for an Adventure.

    There is a big orange gus cat standing in front of you. He looks up at you and he's screaaaaaming. You think he might be hungry.

    What do you feed him? (1: Kitty Gogurts / 2: Can of Tuna / 3: Kibble / 4: Bowl of Milk)

    """)

    answer_1 = input()

    if answer_1 == '1':
        print("""That's Gus' favorite treat!! He rubs his head against your leg.

        Now he's very bored and he wants to work off those gogurt calories, what kind of toy should gus get? (you're buyin)

        (1: A floor to ceiling cat tree / 2: A floppy fish toy / 3: A cardboard box / 4: A crinkly ball)
        """)

    elif answer_1 == '2':
        print(
            """Gus reluctantly eats the canned tuna.. He wishes it was Kitty Gogurts instead.

            He's pretty bored. He wants something to play with. What kind of toy will you buy him?

            (1: A floor to ceiling cat tree / 2: A floppy fish toy / 3: A cardboard box / 4: A crinkly ball)

            """)

    elif answer_1 == '3':
        print("""Not gonna lie, Gus is kinda bummed. He was hoping for Kitty Gogurts. He still apprecaites your help.

        Since you disappointed him with your snack choice, Gus thinks you should make it up to him with a fun new toy. What do you get him?

        (1: A floor to ceiling cat tree / 2: A floppy fish toy / 3: A cardboard box / 4: A crinkly ball)

        """)

    elif answer_1 == '4':
        restart = input("do you want to start over? (1. Yes / 2. No)")
        if restart == '1':
            game()
        else:
            print("bye!")

    else:
        print("that wasnt an option -_-")
        game()

    answer_2 = input()

    if answer_2 == '1':
        print("""Gus climbs up the kitty cat tree and parches at the top. He is very pleased with his new throne.

        Your new orange god feels a little bit sleepy. It would please him to stay a while.. What do you say?

        (1. Yes / 2. No)
        """)

    elif answer_2 == '2':
        print(
            "The floppy fish toy scares the absolute heck out of Gus. He hides under the bed and you never see him again...")
        restart = input("do you want to start over? (1. Yes / 2. No)")
        if restart == '1':
            game()
        else:
            print("bye!")

    elif answer_2 == '3':
        print("""Gus believes you are a genius. He was questioning your loyalty, but now he is certain that you will make a perfect minion.

            Wait.. what? He meant... uhh.. you'd make a perfect companion. haha... ANYWAY! Gus was thinking, maybe.. he could stay a while. What do you say?

            (1. Yes / 2. No)

            """)

    elif answer_2 == '4':
        print("""Gus loves the crinkly ball! But only if you play fetch with him for aproximately 2 hours.
          
          The orange demon, I mean Gus, was wondering if maybe he could stay for a while.. What do you think?

          (1. Yes / 2. No)

          """)

    else:
        print("That wasn't an option. This displeases the orange boy.")

    answer_3 = input()

    if answer_3 == '1':
        print("""You chose wisely.. Gus will be sure to spare your life when he takes over the world. He only has one more question.. Where the heck is he gonna rest his head at night? and during the day? and generally kinda just all the time.. he sleeps a lot.
          
          What kind of bed will you get for THE one and only Gus?

          (1. He already has a cat tree, he doesn't need a bed.. / 2. A poofy donut bed / 3. A little cat house with a bed inside it / 4. He will sleep on your neck at night)
          
          """)

    elif answer_3 == '2':
        print("You don't quite remember what happened.. but you woke up in the hospital. It seems that you were mauled by an animal")
        restart = input("do you want to start over? (1. Yes / 2. No)")
        if restart == '1':
            game()
        else:
            print("bye!")

    else:
        print("Gus is sick of your foolish games")
        restart = input("do you want to start over? (1. Yes / 2. No)")
        if restart == '1':
            game()
        else:
            print("bye!")

    answer_4 = input()

    if answer_4 == '1':
        print("""AHA AHAHAHAHA! That is quite a funny joke... You seem to think your new god will sleep on his cat tree? His play toy? No no no no no... He needs a proper bed, silly!!""")
        # restart = input("do you want to start over? (1. Yes / 2. No)")
        # if restart == '1':
        #     game()
        # else:
        #     print("bye!")

    elif answer_4 == '2':
        print("Gus approves of the poofy donut bed for a month or two.. but then he gets bored with it and ends up sleeping in various places around the house. He refuses to leave.. Congrats! You now have a Gus.")
        new_game = input("Do you want to play again? (1. Yes/ 2. No)")
        if new_game == '1':
            game()
        else:
            print("K BYE!")

    elif answer_4 == '3':
        print("Gus ignores his house for 6 months.. then one day he climbs inside and takes a nap.. oh, by the way.. you have a Gus now.. Way to go!")
        new_game = input("Do you want to play again? (1. Yes/ 2. No)")
        if new_game == '1':
            game()
        else:
            print("K BYE!")

    elif answer_4 == '4':
        print("So true bestie.. he really will.. Also now you have a Gus! Very exciting.. Good luck!")
        new_game = input("Do you want to play again? (1. Yes/ 2. No)")
        if new_game == '1':
            game()
        else:
            print("K BYE!")

    else:
        print(
            "Gus takes out a life insurance policy on you and kills you six months later.")


game()
