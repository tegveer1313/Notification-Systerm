import time
from plyer import notification
import random
from random_words import RandomWords
from PyDictionary import PyDictionary

if __name__ == "__main__":
    while True:
        dictionary = PyDictionary()

        rw = RandomWords()

        word = rw.random_word()
        definitions = dictionary.meaning(word)
        part_of_speech = random.choice( list (definitions.keys() ) )
        definition = random.choice( definitions[part_of_speech] )
        print(f'{word}: {definition} ({part_of_speech})')
        kab = (f'{word}: {definition} ({part_of_speech})')

        notification.notify(
            title = "New word and its meaning",
            message = kab,
            app_icon = "C:\\Users\\pragati computers\\Downloads\\dictionary.ico",
            timeout=20
        )
        time.sleep(10)
#Set time above according to you, Make sure that the time is in minutes and this is the time interwell between second notification. 