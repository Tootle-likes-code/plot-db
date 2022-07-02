""" Represents events within a plot. """

from dataclasses import dataclass, field

from plot.character import Character
from plot.location import Location
from plot.plot_date import PlotDate


@dataclass
class Event:
    """ A thing that happened at a time and a place, likely with characters. """
    name: str
    description: str
    location: Location
    plot_date: PlotDate
    involved_characters: set[Character] = field(default_factory=set)

    def __hash__(self):
        return hash((
            self.name,
            self.description,
            self.location,
            self.plot_date
        ))


@dataclass
class LinkedEvent(Event):
    """
    A thing that happened at a time and a place, likely with characters, with links to events
    that influenced this event and those that came abouts because of it.
    """
    triggering_events: set[Event] = field(default_factory=set)
    following_events: set[Event] = field(default_factory=set)

    @staticmethod
    def convert_event(event: Event, triggering_events: set[Event] = None,
                      following_events: set[Event] = None):
        """
        Converts an Event into a LinkedEvent
        :param event: The Event you wish to convert.
        :param triggering_events: Any events that you want this LinkedEvent to have been the
        result of. If left blank, initialises to set.
        :param following_events: Any events that were caused directly because of this event.
        If left blank, initialises to an empty set.
        :return: The new LinkedEvent.
        """
        if not triggering_events:
            triggering_events = set([])

        if not following_events:
            following_events = set([])

        return LinkedEvent(event.name, event.description, event.location, event.plot_date,
                           event.involved_characters, triggering_events, following_events)
