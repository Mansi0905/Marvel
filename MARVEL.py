import random as r

def format_movie_title(title, guessed_letters):
    # Replace unguessed letters with '_', keep special characters
    return ''.join([char if char in guessed_letters or not char.isalpha() else '_' for char in title])

def display_title(title, guessed_letters, incorrect_guesses):
    # Replace unguessed letters with '_', incorrect guesses with '_'
    return ''.join([char if char in guessed_letters or not char.isalpha() else '_' for char in title])

# Dictionary with Marvel movie names as keys and hints as values
marvel = {
    "iron man": "The film that launched the Marvel Cinematic Universe, featuring Tony Stark.",
    "the incredible hulk": "The story of Bruce Banner and his transformation into the Hulk.",
    "iron man 2": "Tony Stark deals with new threats and his identity as Iron Man.",
    "thor": "The film about the Norse god Thor and his exile to Earth.",
    "captain america: the first avenger": "The origin story of Steve Rogers and his transformation into Captain America.",
    "the avengers": "The team-up of Earth's mightiest heroes to save the world.",
    "iron man 3": "Tony Stark faces a new enemy, the Mandarin, and struggles with his identity.",
    "thor: the dark world": "Thor battles the Dark Elves to save the Nine Realms.",
    "captain america: the winter soldier": "Captain America uncovers a conspiracy within SHIELD.",
    "guardians of the galaxy": "A group of misfit heroes come together to protect a powerful orb.",
    "avengers: age of ultron": "The Avengers face off against the sentient AI, Ultron.",
    "ant-man": "A thief gains the ability to shrink and must stop a dangerous technology from falling into the wrong hands.",
    "captain america: civil war": "The Avengers are divided over the Sokovia Accords, leading to a clash between Captain America and Iron Man.",
    "doctor strange": "A neurosurgeon discovers the mystical arts and battles dark forces.",
    "guardians of the galaxy vol. 2": "The Guardians continue their cosmic adventures and deal with family issues.",
    "spider-man: homecoming": "Peter Parker tries to balance high school life with his role as Spider-Man.",
    "thor: ragnarok": "Thor must stop the apocalypse and face his sister Hela.",
    "black panther": "T'Challa returns to Wakanda to take his place as king and protector.",
    "avengers: infinity war": "The Avengers and their allies face Thanos in a battle to save the universe.",
    "ant-man and the wasp": "Scott Lang teams up with Hope van Dyne to uncover secrets about the quantum realm.",
    "captain marvel": "The origin story of Carol Danvers and her rise as Captain Marvel.",
    "avengers: endgame": "The Avengers attempt to undo the damage caused by Thanos in a final showdown.",
    "spider-man: far from home": "Peter Parker goes on a school trip and faces the mysterious Mysterio.",
    "black widow": "Natasha Romanoff confronts her past and battles the Red Room.",
    "shang-chi and the legend of the ten rings": "Shang-Chi faces his father's secretive Ten Rings organization.",
    "eternals": "An ancient group of immortals come out of hiding to protect humanity from the Deviants.",
    "spider-man: no way home": "Peter Parker deals with the multiverse and seeks help from Doctor Strange.",
    "doctor strange in the multiverse of madness": "Doctor Strange explores the multiverse and faces a new threat.",
    "thor: love and thunder": "Thor teams up with Jane Foster, who has become the Mighty Thor, to face a new villain.",
    "black panther: wakanda forever": "Wakanda mourns the loss of T'Challa and faces new challenges.",
    "ant-man and the wasp: quantumania": "Scott Lang and Hope van Dyne explore the Quantum Realm further.",
    "guardians of the galaxy vol. 3": "The Guardians face new challenges and delve into their pasts.",
    "captain america: new world order": "Sam Wilson takes on the mantle of Captain America in a new world order.",
    "blade": "The vampire hunter Blade makes his debut in the Marvel Cinematic Universe.",
    "fantastic four": "The Fantastic Four are rebooted in the Marvel Cinematic Universe."
}
x="Yes"
while x =="Yes":
    print("~~~~~~"*8)
    print('''!                                                                                                      !
!      ||\\    /||       /\\        ||====\\         \\          /   ||======    ||                !                          
!      || \\  / ||      /  \\       ||     |          \\        /    ||          ||                !
!      ||  \\/  ||     /    \\      ||====/            \\      /     ||====      ||                !
!      ||       ||    /----- \\     ||    \\            \\    /      ||          ||                !
!      ||       ||   /        \\    ||     \\            \\  /       ||          ||                !      
!      ||       ||  /          \\   ||      \\            \\/        ||======    ||======          !
!                                                                                                                  !''')
    print("~~~~~~"*8)
    print("\n")
    # Select a random movie from the dictionary
    L = list(marvel.keys())
    S = r.choice(L)
    hint = marvel[S]
    GS=0
    mar="MARVEL-STUDIOS"
    m=list(mar)
    # Initialize guessed letters and incorrect guesses
    guessed_letters = set()
    incorrect_guesses = set()
    max_incorrect_guesses = 7

    # Game loop
    while True:
        # Display the movie title with current guesses
        formatted_title = display_title(S, guessed_letters, incorrect_guesses)
        print("MOVIE : " + formatted_title)
        
        '''# Check for hint condition
        if '-' in formatted_title:
            print("Hint: " + hint)'''
        
        # Prompt user for input
        G = input("ENTER A CHARACTER: ").lower()
        
        if len(G) != 1 or not G.isalpha():
            a="Please enter a single alphabetical character."
            a=a.upper()
            print(a)
            print("\n")
            continue
        
        if G in S:
            guessed_letters.add(G)
        else:
            incorrect_guesses.add(G)
            
            if m[GS]=='-':
                print("HINT : ",hint)
                m[GS]='$'
                GS+=1
            else:
                m[GS]='$'
                GS+=1
            # Replace incorrect letters with `_` in the display
            formatted_title = display_title(S, guessed_letters, incorrect_guesses)
            print(' '.join(m))
        
        # Check if all letters are guessed
        if all(char in guessed_letters or not char.isalpha() for char in S):
            c="Congratulations! You've guessed the movie: "
            c=c.upper()
            print(c + S)
            break
        
        # Check if maximum incorrect guesses reached
        '''if len(incorrect_guesses) >= max_incorrect_guesses:
            print("Too many incorrect guesses. The movie was: " + S)
            break'''

        '''# Print remaining guesses
        remaining_guesses = max_incorrect_guesses - len(incorrect_guesses)
        print("Remaining guesses:", remaining_guesses)'''
        if all(char == '$' or char == '-' for char in m):
            print("GAME OVER! THE MOVIE WAS: " + S)
            break

    x=input("CONTINUE : ")
    x=x.title()
