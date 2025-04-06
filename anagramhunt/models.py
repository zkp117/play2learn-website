import random
import time
import threading
from django.db import models
from django.conf import settings
from common.utils.text import unique_slug

# timer will end even if input isn't entered (from user)
def enter_input(user_input_container):
    user_input_container.append(input())

# list of anagrams + sets
def anagram_list():
    return {
        5: [["abets", "baste", "betas", "beast","beats"],
            ["acres", "cares", "races", "scare"],
            ["alert", "alter", "later"],
            ["angel", "angle", "glean"],
            ["baker", "brake", "break"],
            ["bared", "beard", "bread", "debar"],
            ["dater", "rated", "trade", "tread"],
            ["below", "bowel", "elbow"],
            ["caret", "cater", "crate", "trace", "react"]],
            
        6: [["arrest", "rarest", "raster", "raters", "starer"],
            ["carets", "caters", "caster", "crates", "reacts", "recast", "traces"],
            ["canter", "nectar", "recant", "trance"],
            ["danger", "gander", "garden", "ranged"],
            ["daters", "trades", "treads", "stared"]],

        7: [["allergy", "gallery", "largely", "regally"],
            ["aspired", "despair", "diapers", "praised"],
            ["claimed", "decimal", "declaim", "medical"],
            ["dearths", "hardest", "hatreds", "threads", "trashed"],
            [ "detains", "instead", "sainted", "stained"]],

        8: [["parroted", "predator", "prorated", "teardrop"],
            ["repaints", "painters", "pantries", "pertains"],
            ["restrain", "retrains", "strainer", "terrains", "trainers"],
            [ "construe", "counters", "recounts", "trounces"]]
            }

# choosing the word length and picking an anagram set + first chosen word
def choose_word_length(anagrams):
    while True:
        try:
            word_length = int(input("Please enter a word length [5, 6, 7, 8]: "))
            if word_length in anagrams:
                chosen_group = random.choice(anagrams[word_length])
                chosen_word = random.choice(chosen_group)
                return word_length, chosen_word, chosen_group
        except ValueError:
            print("That is not a correct word length. Please try again [5, 6, 7, 8]: ")


# playing the game
def anagram_game_play():
    anagrams = anagram_list()
    score = 0

    word_length, chosen_word, chosen_group = choose_word_length(anagrams)
    anagrams_left = set(chosen_group) - {chosen_word}
    already_guessed = set()
    completed_word_sets = set()

    start_time = time.time()
    time_total = 60
    
    print(f"Your chosen word is '{chosen_word}'")
    print(f"Unguessed anagrams for '{chosen_word}': {len(anagrams_left)}")
    print("You have 60 seconds, good luck!")
    
    while True:
        passed_time = time.time() - start_time
        remaining_time = time_total - passed_time

        if remaining_time <= 0:
            print("Time is up! Sorry you didn't get that last word in")
            print(f"Your final score is {score}")
            return
        
        # if user guesses all the anagrams / finishes all anagram sets before 60 seconds is up 
        print(f"Make a guess ({round(remaining_time)}s left): ", end="", flush=True)

        user_input_container = []
        input_thread = threading.Thread(target=enter_input, args=(user_input_container,))
        input_thread.daemon = True
        input_thread.start()

        input_thread.join(timeout=remaining_time)

        if not user_input_container:
            print("Time is up! Sorry, you weren't able to enter a guess in time.")
            print(f"Your final score is {score}")
            return
        
        user_guess = user_input_container[0].strip().lower()

        # when user finishes an anagram set it gets added to the completed set list
        if not anagrams_left:
            completed_word_sets.add(tuple(sorted(chosen_group)))

            unguessed_word_sets = [
                group for group in anagrams[word_length]
                if tuple(sorted(group)) not in completed_word_sets
            ]

            if not unguessed_word_sets:
                print(f"Great job,you finished all of the anagrams for {word_length}!")
                print(f"Your final score is {score}")
                return
            
            # how random anagrams are chosen within word length + collection of anagrams
            chosen_group = random.choice(unguessed_word_sets)
            chosen_word = random.choice(chosen_group)
            anagrams_left = set(chosen_group) - {chosen_word}
            already_guessed.clear()

            print(f"Your new word is '{chosen_word}'.")
            print(f"Unguessed anagrams for '{chosen_word}': {len(anagrams_left)}")
        
        # when the user makes a correct guess for the current anagram set it gets added to the already guessed
        if user_guess in anagrams_left:
            already_guessed.add(user_guess)
            anagrams_left.remove(user_guess)
            score+=1
        
            print(f"{user_guess} is correct!")
            print(f"Unguessed anagrams for '{chosen_word}': {len(anagrams_left)}")

        # if user makes a repeated guess for current anagram set
        elif user_guess in already_guessed:
            print(f"You already guessed {user_guess}.")
            print(f"Unguessed anagrams for '{chosen_word}': {len(anagrams_left)}")

        # if user guesses the current chosen word
        elif user_guess == chosen_word:
            print(f"{user_guess} is the chosen word.")
            print(f"Unguessed anagrams for '{chosen_word}': {len(anagrams_left)}")

        # if user makes an incorrect guess
        else:
            print(f"{user_guess} is incorrect.")
            print(f"Unguessed anagrams for '{chosen_word}': {len(anagrams_left)}")

    # if user doesn't finish the game in time after input is enter    

anagram_game_play()


WORD_LENGTH = [
    ('5', '5 letters'),
    ('6', '6 letters'),
    ('7', '7 letters'),
    ('8', '8 letters'),
    ]
class Anagramhunt(models.Model):
    play = models.CharField(max_length=100)

    def __str__(self):
        return self.play
class WordScore(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    score = models.IntegerField(default = 0)
    word_length = models.CharField(
        max_length = 1,
        choices = WORD_LENGTH,
        default = '5',
    )
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)  

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - Word Score: {self.score} - Length: {self.get_word_length_display()}"