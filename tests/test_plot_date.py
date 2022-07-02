import unittest

from plot.plot_date import PlotDate


class PlotDateTests(unittest.TestCase):
    pass


class ConstructorTests(PlotDateTests):
    def test_constructor_missing_month_raises_ValueError(self):
        # Arrange
        expected_result = "Must be given a month as well as a day."

        # Act
        with self.assertRaises(ValueError) as error:
            PlotDate(year=2000, day=1, hour=1)

        # Assert
        exception = error.exception
        self.assertEqual(expected_result, exception.args[0])

    def test_constructor_missing_day_raises_ValueError(self):
        # Arrange
        expected_result = "Must be given a day as well as an hour."

        # Act
        with self.assertRaises(ValueError) as error:
            PlotDate(year=2000, month=1, hour=1)

        # Assert
        exception = error.exception
        self.assertEqual(expected_result, exception.args[0])

    def test_constructor_has_only_hour_raises_Value_Error(self):
        # Arrange
        expected_result = "Must be given a day as well as an hour."

        # Act
        with self.assertRaises(ValueError) as error:
            PlotDate(year=2000, hour=1)

        # Assert
        exception = error.exception
        self.assertEqual(expected_result, exception.args[0])


class StrTests(PlotDateTests):
    def test_full_date_returns_correct_format(self):
        # Arrange
        expected_result = "2000-01-01T01"
        test_date = PlotDate(year=2000, month=1, day=1, hour=1)

        # Act
        result = str(test_date)

        # Assert
        self.assertEqual(expected_result, result)

    def test_no_month_returns_correct_format(self):
        # Arrange
        expected_result = "2000"
        test_date = PlotDate(year=2000)

        # Act
        result = str(test_date)

        # Assert
        self.assertEqual(expected_result, result)

    def test_no_day_returns_correct_format(self):
        # Arrange
        expected_result = "2000-100"
        test_date = PlotDate(year=2000, month=100)

        # Act
        result = str(test_date)

        # Assert
        self.assertEqual(expected_result, result)

    def test_no_hour_returns_correct_format(self):
        # Arrange
        expected_result = "2000-01-01"
        test_date = PlotDate(year=2000, month=1, day=1)

        # Act
        result = str(test_date)

        # Assert
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
