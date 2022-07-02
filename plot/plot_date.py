""" Handles customer date/times for potentially fantasy dates. """

from dataclasses import dataclass
from typing import Optional


@dataclass
class PlotDate:
    """
    A custom date + hour that works for custom calendars.
    """
    year: int
    month: Optional[int] = None
    day: Optional[int] = None
    hour: Optional[int] = None

    def __init__(self, year, month=None, day=None, hour=None):
        if not month and day:
            raise ValueError("Must be given a month as well as a day.")

        if not day and hour:
            raise ValueError("Must be given a day as well as an hour.")

        self.year = year
        self.month = month
        self.day = day
        self.hour = hour

    def __hash__(self):
        return hash((
            self.year,
            self.month,
            self.day,
            self.hour
        ))

    def __str__(self) -> str:
        date = f"{self.year}"
        date += f"{f'-{self.month:02}' if self.month else ''}"
        date += f"{f'-{self.day:02}' if self.day else ''}"
        date += f"{f'T{self.hour:02}' if self.hour else ''}"
        return date
