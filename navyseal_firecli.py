#!/usr/bin/env python3

import fire, re

class Ships():
    def sail(self):
        ship_name = 'Your Ship'
        print(f'{ship_name} is setting sail')

    def list(self):
        ships = ['Cassandra', 'Roberto', 'Anna a pina' ]
        print(f"Fleet: {','.join(ships)}")

    LIGHT_MESSAGES = {
		'English': "There are %(number_of_lights)s lights.",
		'Pirate':  "Arr! Thar be %(number_of_lights)s lights."
    }

    def lights_message(language, number_of_lights):
        """Return a language-appropriate string reporting the light count."""
        return LIGHT_MESSAGES[language] % locals()

    def is_pirate(message):
        """Return True if the given message sounds piratical."""
        return re.search(r"(?i)(arr|avast|yohoho)!", message) is not None

def sailors():
    print('Greetings Great Pirate')

class Cli():

    def __init__(self):
        self.sailors = sailors
        self.ships = Ships()

if __name__ == '__main__':
    fire.Fire(Cli)

