""" Manages locations of a plot. """

from abc import ABC
from dataclasses import dataclass
from typing import Optional


@dataclass
class Place(ABC):
    """ The root of locations. """
    name: str
    description: str


@dataclass
class Location(Place):
    """ The implementation of Place, which is aware of it's parent location. """
    parent_location: Optional[Place] = None
