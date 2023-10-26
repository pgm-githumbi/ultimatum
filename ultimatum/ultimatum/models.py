
from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = "mini-ultimatum"
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 1
    ENDOWMENT_AMT = cu(200)



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    POSITIVE_DECISION = 'positive'
    NEGATIVE_DECISION = 'negative'
    def __init__(self, *args, **kwargs) -> None:
        self.punisher_decision = None
        super().__init__(*args, **kwargs)
        

    def set_payoffs(self):
        for player in self.get_players():
            player1 = self.get_player_by_id(1)
            player2 = self.get_player_by_id(2)
            player3 = self.get_player_by_id(3)
            if player3.punish:
                player.payoff = Currency(0)
            else:
                # Not punish decision: Calculate payouts.
                player1.payoff = C.ENDOWMENT_AMT - player1.offer
                player2.payoff = player1.offer


class Player(BasePlayer):
    offer = models.IntegerField(min=0, max=C.ENDOWMENT_AMT, 
                                label="Enter amount to send to player 2")
    punish = models.BooleanField(
        choices=([True, 'Punish'], [False, 'Don\'t punish'])
    )

    def calculate_payoff(self):
        self.group.set_payoffs()

def punish_blank(player: Player):
    # The punish field should be blank if
    # its player 1 or 2 but not if its 3
    return player.id_in_group in (1, 2)

def payoff_blank(player: Player):
    # Player 3 lacks payoffs
    return player.id_in_group == 3

def results(player: Player):
    player.calculate_payoff()
