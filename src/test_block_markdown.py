import unittest

from block_markdown import markdown_to_blocks

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks_trim(self):
        blocks = markdown_to_blocks(
            "         # This is a heading      \n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.    "
        )
        self.assertListEqual(
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            ],
            blocks,
        )

    def test_markdown_to_blocks_with_empty_block(self):
        blocks = markdown_to_blocks(
            "         # This is a heading      \n\n\n\n\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.    \n\n\n\n  * This is the first list item in a list block * This is a list item * This is another list item"
        )
        self.assertListEqual(
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block * This is a list item * This is another list item"
            ],
            blocks,
        )

if __name__ == "__main__":
    unittest.main()