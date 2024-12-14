import unittest

from utils import extract_title

class TestUtils(unittest.TestCase):
    def test_extract_title(self):
        md = """
# Title 

## Sub-title

This is **bolded** paragraph
text in a p
tag here

# Title fake

This is another paragraph with *italic* text and `code` here

"""

        title = extract_title(md)
        self.assertEqual(
            title,
            "Title"
        )

    def test_extract_title_no_title(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""
        with self.assertRaises(Exception) as context:
            extract_title(md)
            self.assertTrue("There is no h1 header !" in context.exception)

if __name__ == "__main__":
    unittest.main()