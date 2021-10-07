"""
Tests for the `translate` function.
"""

import pathlib
import pytest

from scripts.translate import translate


class TestTranslate:
    """ Translate function tests. """
    def test_translate_missing_longitude(self):
        """ Test CSV file with missing `Longitude` column. """
        with pytest.raises(AssertionError):
            translate(
                './resources/missing-longitude.csv',
                './resources/missing-longitude.geojson'
            )

    def test_translate_missing_latitude(self):
        """ Test CSV file with missing `Latitude` column. """
        with pytest.raises(AssertionError):
            translate(
                './resources/missing-latitude.csv',
                './resources/missing-latitude.geojson'
            )

    def test_translate_success(self):
        """ Test CSV file with both `Longitude` and `Latitude` columns. """
        output_filename = './resources/stadiums.geojson'

        translate('./resources/stadiums.csv', output_filename)

        assert pathlib.Path(output_filename).resolve().is_file()
