import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_base_case(self):
        node = HTMLNode()
        self.assertEqual(None == node.tag == node.value, node.value == node.children == node.props)

    def test_base_props_to_html(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_one_props_to_html(self):
        node = HTMLNode(props={"color":"red"})
        self.assertEqual(node.props_to_html(), "color=\"red\"")

    def test_many_props_to_html(self):
        three_props = {
                "color":"red",
                "font-size":"15px",
                "font-type":"ariel"
                }
        node = HTMLNode(props=three_props)

        target_string = "color=\"red\" font-size=\"15px\" font-type=\"ariel\""

        self.assertEqual(node.props_to_html(), target_string)
        self.assertNotEqual(node.props_to_html(), target_string + " ")

class TestLeafNode(unittest.TestCase):
    def test_invalid_leaf(self):
        try:
            node = LeafNode()
        except ValueError:
            self.assertTrue(True)
            return
        self.assertTrue(False)

    def test_plain_text_leaf(self):
        plain_leaf = LeafNode(value="Plain.")
        target_html = "Plain."
        self.assertEqual(plain_leaf.to_html(), target_html)

    def test_p_leaf(self):
        p_leaf = LeafNode("p", "This is a paragraph of text.")
        target_html = "<p>This is a paragraph of text.</p>"
        self.assertEqual(p_leaf.to_html(), target_html)

    def test_a_leaf(self):
        a_leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        target_html = "<a href=\"https://www.google.com\">Click me!</a>"
        self.assertEqual(a_leaf.to_html(), target_html)

