# from lxml import etree
from xml.etree import ElementTree
inp = input()
# inp = '''
#       <cube color="blue">
#           <cube color="red">
#               <cube color="green">
#               </cube>
#           </cube>
#           <cube color="red">
#           </cube>
#       </cube>
#       '''
root = ElementTree.fromstring(inp)
# print(f'root: {root}')
elems = {root.attrib['color']: 1}
# for child in root:
#     print(child.tag, child.attrib)
# for element in root.iter("cube"):
#     print(element.attrib)
def recur(node, level):
    for child in node:
        if child.attrib['color'] not in elems:
            elems[child.attrib['color']] = level
        else:
            elems[child.attrib['color']] += level
        recur(child, level+1)
recur(root, 2)
print(elems['red'], elems['green'], elems['blue'])

# root = ElementTree.Element("cube")
# root.set("color", "blue")
#
# cube_ch = ElementTree.SubElement(root, "cube")
# cube_ch.set("color", "red")
#
# cube_ch_1 = ElementTree.SubElement(root, "cube")
# cube_ch_1.set("color", "red")
#
# cube_grch = ElementTree.SubElement(cube_ch, "cube")
# cube_grch.set("color", "green")
#
# tree = ElementTree.ElementTree(root)
# tree.write("cubes.xml")

