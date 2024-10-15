class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        props_string = ""
        if self.props == None:
            return props_string
        for key in self.props:
            props_string += f"{key}=\"{self.props[key]}\" "

        return props_string[:-1]

    def __repr__(self):
        return f"Tag: {self.tag} \nValue: {self.value} \nChildren: {self.children} \nProperties: {self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value == None:
            raise ValueError("leaf nodes must have a value attribute")
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("leaf nodes must have a value attribute")
        
        if self.tag == None:
            return self.value
        
        start = f"<{self.tag}"
        end = f"</{self.tag}>"
        if self.props != None:
            start += " " + self.props_to_html()
        start += ">"

        return start + self.value + end

