from abc import ABC
from dataclasses import dataclass
from typing import Optional


@dataclass
class Place(ABC):
    name: str
    description: str


@dataclass
class Location(Place):
    parent_location: Optional[Place]
