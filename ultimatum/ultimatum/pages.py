

from otree.api import *
from . import models as local_models


class IntroductionPage(Page):
    
    def is_displayed(player: local_models.Player):
        # Shown to every player in first round
        #return player.round_number == 1 # Shown only for first round
        return True
    
    def before_next_page(self):
        print(f'\nIn introduction page\n')
    
    body_text = """Player one makes an offer to player 2. Player 3 approves the offer
                (or not) before player 2 sees the offer. Player 2 will then accept or 
                reject the offer provided the punisher(p3) approved the offer.
                """

class P1OfferPage(Page):
    """Player one asked to give offer to player 2"""
    form_model = 'player'
    form_fields = ['offer']
    def is_displayed(self):
        # Only displayed for player 1
        return self.player.id_in_group == 1
    
    def vars_for_template(self):
        return {
            'endowment_amount' : local_models.C.ENDOWMENT_AMT,
        }
        

class WaitForP1(Page):
    timeout_seconds = 5
    def before_next_page(self):
        print(f'in before_next_page in WaitForP1')

    def after_all_players_arrive(self):
        print(f'p1 has made the offer: {self.group.get_player_by_id(1).offer}')

PUNISHER_DECISION = None
PUNISH_DECISION = 'punish'
NOT_PUNISH = 'not_punish'

class PunisherDecisionPage(Page):
    """Player 3 decides whether the offer is acceptable and
    punishes if unacceptable."""
    def is_displayed(self):
        return self.player.id_in_group == 3  # Display only for Player 3.

    def vars_for_template(self):
        player1 = self.group.get_player_by_id(1)
        return {
            'offer_made': player1.offer,
        }

    def before_next_page(self):
        decision = self.player.punish == True
        global PUNISHER_DECISION, PUNISH_DECISION, NOT_PUNISH
        if decision is True:
            PUNISHER_DECISION = PUNISH_DECISION
        else:
            PUNISHER_DECISION = NOT_PUNISH
            
        print(f"punisher_decision set to: {decision}")

    form_model = 'player'
    form_fields = ['punish']

class WaitForPunishDecision(WaitPage):
    
    timeout_seconds = 5
    def after_all_players_arrive(self):
        pass

class P2OfferAcceptPage(Page):
    def is_displayed(self):
        # Display only to p2
        return self.player.id_in_group == 2
    
    def vars_for_template(self):
        global PUNISH_DECISION, NOT_PUNISH, PUNISHER_DECISION
        player1 = self.group.get_player_by_id(1)
        punish_decision = PUNISHER_DECISION
        return {
            'offer_made': player1.offer,
            'punisher_decision' : punish_decision,
            'punish' : PUNISH_DECISION,
            'not_punish' : NOT_PUNISH,
        }
    
    def before_next_page(self):
        p1:'local_models.Player' = self.group.get_player_by_id(1)
        p2:'local_models.Player' = self.group.get_player_by_id(2)
        p1.calculate_payoff()
        p2.calculate_payoff()
        
    
    


class WaitForP2Decision(WaitPage):
    def after_all_players_arrive(self):
        
        print(f'p2 has made the decision')

class Results(Page):
    def vars_for_template(self):
        player1 = self.group.get_player_by_id(1)
        player2 = self.group.get_player_by_id(2)
        player3 = self.group.get_player_by_id(3)
        return {
            'endowment' : local_models.C.ENDOWMENT_AMT,
            'offer': player1.offer,
            'punish': player3.punish,
            'player' : self.player,
            'player1' : player1,
            'player2' : player2,
            'player3' : player3,
            
        }
    


page_sequence = [#IntroductionPage,
                 P1OfferPage,
                 WaitForP1,
                 PunisherDecisionPage, 
                 WaitForPunishDecision,
                 P2OfferAcceptPage,
                 WaitForP2Decision,
                 Results
                 ]
