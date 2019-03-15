"""Test module
file: test_highlighter.py
date: 12.12.2012
author smith@example.com
license: MIT"""

import unittest
from highlighter import create_app


class HighlightTest(unittest.TestCase):
    """Test class for flask app."""

    def setUp(self):
        """This method is called each time the test routine run"""
        self.app = create_app().test_client()
        self.text = "Python!"
        self.search_text = "th"

        self.hi_text = '<mark>' + self.search_text + '</mark>'
        self.highlighted = str.encode(self.hi_text)

    def tearDown(self):
        """This method is called after the test routine is finished
        to clear out the data created in setUp method."""

    def test_markup_text(self):
        """Test markup process"""

        response = self.app.post('/', data={'search': self.search_text,
                                            'text': self.text})
        print("Result: ")
        print(response.data)

        self.assertIn(self.highlighted, response.data)
