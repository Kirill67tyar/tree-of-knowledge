from pprint import pprint as pp
"""

"""

# 3_6_6
from xml.etree import ElementTree

# xml_data = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'

xml_data = input()
tree = ElementTree.fromstring(xml_data)
data = {}
level = 1
cls_el = type(tree)
data[tree.attrib['color']] = level


def rec_tree(elem, level):
    for e in elem:
        if isinstance(e, cls_el):
            data[e.attrib['color']] = data.get(e.attrib['color'], 0) + level
            rec_tree(e, level + 1)


rec_tree(tree, level + 1)
output = list(data.items())
output.sort(key=lambda x: x[0], reverse=True)
output = [quantity for color, quantity in output]
print(*output)