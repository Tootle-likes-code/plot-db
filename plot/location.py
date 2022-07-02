""" Manages locations of a plot. """

from abc import ABC
from dataclasses import dataclass
from typing import Optional


@dataclass
class Place(ABC):
    """ The root of locations. """
    name: str
    description: str

    def __hash__(self):
        return hash((
            self.name,
            self.description
        ))


@dataclass
class Location(Place):
    """ The implementation of Place, which is aware of it's parent location. """
    parent_location: Optional[Place] = None

    def __hash__(self):
        return hash((
            self.name, self.description, self.parent_location
        ))
