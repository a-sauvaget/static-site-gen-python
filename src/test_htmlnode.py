import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "h1",
            "H1 Title",
            None,
            {"id": "title", "class": "isBold"}
        )
        self.assertEqual(
            node.props_to_html(),
            (' id="title" class="isBold"')
        )

    def test_values(self):
        node = HTMLNode(
            "p",
            "Un superbe paragraphe."
        )

        self.assertEqual(
            node.tag,
            "p"
        )

        self.assertEqual(
            node.value,
            "Un superbe paragraphe."
        )

        self.assertEqual(
            node.children,
            None
        )

        self.assertEqual(
            node.props,
            None
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "Quel beau temps !",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, Quel beau temps !, children: None, {'class': 'primary'})",
        )

if __name__ == "__main__":
    unittest.main()