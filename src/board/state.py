from src.controller.events import EventManager, GameEvent
from src.utils.logging import get_logger
from enum import Enum


class GamePhase(Enum):
    SETUP = 0
    PLAY = 1
    END = 2


class GameState:

    def __init__(self, events_manager: EventManager):

        self.logger = get_logger("GameState")
        self.events_manager = events_manager
        self.current_game_phase = GamePhase.SETUP

        # Subscribe to events

        self.events_manager.subscribe(GameEvent.PHASE_CHANGED, self.set_game_phase)

    def set_game_phase(self, phase: GamePhase):
        self.current_game_phase = phase
        self.logger.debug(f"Game phase set to {phase.name}")
