import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a different text node", "bold")
        self.assertNotEqual(node, node2)

    def test_type_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is a text node", "link", "https://google.com")
        node2 = TextNode("This is a text node", "link", "https://boot.dev")
        self.assertNotEqual(node, node2)

    def test_node_prints_properly(self):
        node = TextNode("This is a text node", "bold")
        target_string = "TextNode(This is a text node, bold, None)"
        self.assertEqual(node.__repr__(), target_string)

if __name__ == "__main__":
    unittest.main()
