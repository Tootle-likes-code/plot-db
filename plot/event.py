from dataclasses import dataclass, field

from plot.character import Character
from plot.location import Location
from plot.plot_date import PlotDate


@dataclass
class Event:
    name: str
    description: str
    location: Location
    plot_date: PlotDate
    involved_characters: set(Character) = field(default_factory=list)


@dataclass
class LinkedEvent(Event):
    triggering_events: set(Event) = field(default_factory=list)
    following_events: set(Event) = field(default_factory=list)

    @staticmethod
    def convert_event(event: Event):
        return LinkedEvent(event.name, event.description, event.location, event.plot_date)
