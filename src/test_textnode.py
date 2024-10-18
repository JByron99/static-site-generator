import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    
    # Node tests
    
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

    # Converting to HTML

    def test_text_to_html_plain(self):
        html_node = text_node_to_html_node(TextNode("Plain text", "text"))
        target_html = "Plain text"
        self.assertEqual(html_node.to_html(), target_html)

    def test_text_to_html_bold(self):
        html_node = text_node_to_html_node(TextNode("Bold text", "bold"))
        target_html = "<b>Bold text</b>"
        self.assertEqual(html_node.to_html(), target_html)

    def test_text_to_html_italic(self):
        html_node = text_node_to_html_node(TextNode("Italic text", "italic"))
        target_html = "<i>Italic text</i>"
        self.assertEqual(html_node.to_html(), target_html)
    
    def test_text_to_html_code(self):
        html_node = text_node_to_html_node(TextNode("Code text", "code"))
        target_html = "<code>Code text</code>"
        self.assertEqual(html_node.to_html(), target_html)
    
    def test_text_to_html_link(self):
        html_node = text_node_to_html_node(TextNode("Linked text", "link", "boot.dev"))
        target_html = "<a href=\"boot.dev\">Linked text</a>"
        self.assertEqual(html_node.to_html(), target_html)
    
    def test_text_to_html_image(self):
        html_node = text_node_to_html_node(TextNode("A picture of corn.", "image", "./corn_on_the_cob.png"))
        target_html = "<img src=\"./corn_on_the_cob.png\" alt=\"A picture of corn.\"></img>"
        self.assertEqual(html_node.to_html(), target_html)


if __name__ == "__main__":
    unittest.main()
