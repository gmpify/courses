import re

class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    print (input_string)
    head_position = input_string.index(";")
    head, tail = input_string[0:head_position], input_string[head_position:]
    if head == tail:
        return SgfTree()

    m = re.match(r";\w*(\[\w*\])*", head)
    print (head, m)
    properties = {
        m[1]: m[2]
    }
    return SgfTree(properties, parse_recur(tail))


def parse_a(input_string):
    node = re.match(r"\(;(.*)\)", input_string)

    if not node:
        raise ValueError("InvalidInput")

    properties = re.match(r"([A-Z]+)(\[\w+\])+", node[1])
    if not properties:
        raise ValueError("InvalidInput")

    
    return SgfTree()
