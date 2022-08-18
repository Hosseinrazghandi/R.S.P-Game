from rule import RULES

class Game:

    counter_p1 = 0
    counter_p2 = 0

    person1 = None
    person1 = None
    
    def __init__(self, p1, p2):
        Game.person1 = p1
        Game.person2 = p2


    @classmethod
    def winner_choice(self):
        match = {Game.person1, Game.person2}

        if len(match) == 1:
            return None

        return RULES[tuple(sorted(match))]

    
    @classmethod
    def winner_person(self):
        if Game.person1 == Game.winner_choice():
            return Game.person1

        elif Game.person2 == Game.winner_choice():
            return Game.person2

        else:
            return None

    
    @classmethod
    def counter_winner(self):
        if Game.person1 == Game.winner_person():
            Game.counter_p1 += 1
        
        elif Game.person2 == Game.winner_person():
            Game.counter_p2 += 1

        return f"You: {Game.counter_p1}\nSystem: {Game.counter_p2}"






