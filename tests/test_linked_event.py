import unittest

from plot.event import LinkedEvent, Event
from plot.location import Location
from plot.plot_date import PlotDate


class LinkedEventTests(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_location = Location("Test Location", "Test Location Description")
        self.mock_plot_date = PlotDate(2000, 1, 1, 0)


class ConvertEventTests(LinkedEventTests):
    def test_converts_event(self):
        # Arrange
        expected_result = LinkedEvent("Test", "Test Description", self.mock_location, self.mock_plot_date)
        event = Event("Test", "Test Description", self.mock_location, self.mock_plot_date)

        # Act
        result = LinkedEvent.convert_event(event)

        # Assert
        self.assertEqual(expected_result, result)

    def test_converts_event_with_triggering_events(self):
        # Arrange
        triggering_events = {
            Event("First Event", "First Event Description", self.mock_location, self.mock_plot_date),
            Event("Second Event", "Second Event Description", self.mock_location, self.mock_plot_date),
            Event("Third Event", "Third Event Description", self.mock_location, self.mock_plot_date),
        }
        expected_result = \
            LinkedEvent(
                "Test",
                "Test Description",
                self.mock_location,
                self.mock_plot_date,
                triggering_events=triggering_events
            )
        event = Event("Test", "Test Description", self.mock_location, self.mock_plot_date)

        # Act
        result = LinkedEvent.convert_event(event, triggering_events)

        # Assert
        self.assertEqual(expected_result, result)

    def test_converts_event_with_following_events(self):
        # Arrange
        following_events = {
            Event("First Event", "First Event Description", self.mock_location, self.mock_plot_date),
            Event("Second Event", "Second Event Description", self.mock_location, self.mock_plot_date),
            Event("Third Event", "Third Event Description", self.mock_location, self.mock_plot_date),
        }
        expected_result = \
            LinkedEvent(
                "Test",
                "Test Description",
                self.mock_location,
                self.mock_plot_date,
                following_events=following_events
            )
        event = Event("Test", "Test Description", self.mock_location, self.mock_plot_date)

        # Act
        result = LinkedEvent.convert_event(event, following_events=following_events)

        # Assert
        self.assertEqual(expected_result, result)
