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


class TestParentNode(unittest.TestCase):
    def test_example_parent(self):
        target_html = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        example_parent = ParentNode(
                "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text")
                ],
            )
        self.assertEqual(example_parent.to_html(), target_html)

    def test_invalid_parent(self):
        try:
            node = ParentNode()
        except ValueError as v:
            self.assertNotEqual(str(v), "tag attribute cannot be empty")
            self.assertEqual(str(v), "parent nodes must have children")
            return
        self.assertTrue(False)

    def test_no_tag_to_html(self):
        try:
            node = ParentNode(children=[LeafNode(None, "Normal text")])
            invalid_html = node.to_html()
        except ValueError as v:
            self.assertEqual(str(v), "tag attribute cannot be empty")
            self.assertNotEqual(str(v), "parent nodes must have children")
            return
        self.assertTrue(False)
    
    def test_nested_parent(self):
        nested_parent = ParentNode(
                "html",
                [
                    ParentNode(
                        "body",
                        [LeafNode("p", "Red text", {"color":"red"})],
                        )
                ],
            )
        target_html = "<html><body><p color=\"red\">Red text</p></body></html>"

        self.assertEqual(nested_parent.to_html(), target_html)

if __name__ == "__main__":
    unittest.main()

