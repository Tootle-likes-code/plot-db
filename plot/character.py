""" Manages characters. """

from dataclasses import dataclass


@dataclass
class Character:
    """
    A character data class.
    """
    name: str
    description: str
