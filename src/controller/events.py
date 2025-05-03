import enum
from typing import Dict, List, Any, Callable

from src.utils.logging import get_logger


class GameEvent(enum.Enum):
    TILE_CHANGED = "tile_changed"
    # Add more events as needed


class EventManager:
    def __init__(self):
        self.listeners: Dict[GameEvent, List[Callable]] = {
            event: [] for event in GameEvent
        }
        self.logger = get_logger("MVC-Events")

    def subscribe(self, event_type: GameEvent, listener: Callable):
        """Add a listener function for a specific event type"""
        if event_type in self.listeners:
            self.listeners[event_type].append(listener)
            self.logger.debug(f"Subscribed {listener.__name__} to {event_type.name}")

    def unsubscribe(self, event_type: GameEvent, listener: Callable):
        """Remove a listener from a specific event type"""
        if event_type in self.listeners and listener in self.listeners[event_type]:
            self.listeners[event_type].remove(listener)
            self.logger.debug(
                f"Unsubscribed {listener.__name__} from {event_type.name}"
            )

    def dispatch(self, event_type: GameEvent, data: Any = None):
        """Send event to all registered listeners"""
        if event_type in self.listeners:
            for listener in self.listeners[event_type]:
                listener(data)
                # self.logger.debug(f"Dispatched {event_type.name} to {listener.__name__} with data: {data}")
