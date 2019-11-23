import game.agents.BaseAgent

class PacifistAgent(BaseAgent):
    
    def __init__(self, player_name):
        super().__init__(player_name)

    def place_initial_troops(self, initial_state, num_troops):
        """ Place Initial Troops on board. Executed once at begining of game.

            Arguments:\\
                * current_state: The current Map State of the game.\\
                * num_troops: The number of troops to reinforce with.\\
            Returns:\\
                * result_state: The resulting Map State of the game.
        """
        # TODO: Should call here random_initial_reinforcement()
        raise(NotImplementedError)

    def take_turn(self, current_state):
        """ Take Turn in game. Executed each turn on agents.

            Arguments:\\
                * current_state: The current Map State of the game.\\
            Returns:\\
                * result_state: The resulting Map State of the game.
        """
        goal_state = pacifist_strategy(current_state)
        # TODO: Should act upon goal_state to return action to be done in game.
        # TODO: return next_state
        raise(NotImplementedError)


    def pacifist_strategy(self, current_state):
        """ Employs Pacifist Strategy: pplaces all of its bonus armies to the territory with the fewest armies,
            then conquers only the one territory with fewest armies (if it can).

            Arguments:\\
                * current_state: The current Map State of the game.\\
            Returns:\\
                * result_state: The resulting Map State of the game.
        """
        #TODO: Build Aggressive Solution and return result.
        raise(NotImplementedError)