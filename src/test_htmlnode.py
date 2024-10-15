import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_base_case(self):
        node = HTMLNode()
        self.assertEqual(None == node.tag == node.value, node.value == node.children == node.props)

    def test_base_props_to_html(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_one_props_to_html(self):
        node = HTMLNode(props={"color":"red"})
        self.assertEqual(node.props_to_html(), "color=red")

    def test_many_props_to_html(self):
        three_props = {
                "color":"red",
                "font-size":"15px",
                "font-type":"ariel"
                }
        node = HTMLNode(props=three_props)

        target_string = "color=red font-size=15px font-type=ariel"

        self.assertEqual(node.props_to_html(), target_string)
        self.assertNotEqual(node.props_to_html(), target_string + " ")
