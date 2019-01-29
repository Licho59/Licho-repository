from __future__ import division
import random
from math import *
from PIL import Image, ImageDraw
#Creates a class, Node, with an attribute for barycentric coordinates and cartesian coordinates


class Node:
    def __init__(self, bary1, bary2, bary3):
        self.bary1 = bary1
        self.bary2 = bary2
        self.bary3 = bary3
        self.x = None
        self.y = None

    def __eq__(self, other):
        return self.bary1 == other.bary1 and self.bary2 == other.bary2 and self.bary3 == other.bary3
    '''def __ne__(self, other)
        return not self = other'''

#Creates a class, Connection, with attributes for its end nodes, the length of the segment,
#and the cartesian coordinates of its midpoint


class Connection:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.midpoint_x = (node1.x + node2.x) / 2
        self.midpoint_y = (node1.y + node2.y) / 2
        self.length = sqrt((node1.x - node2.x)**2 + (node1.y - node2.y)**2)
        self.length_x = abs(node1.x - node2.x)
        self.length_y = abs(node1.y - node2.y)

    def __eq__(self, other):
        return self.node1 == other.node1 and self.node2 == other.node2


iters = 5  # number of iterations
r = 0.2  # Roughness parameter
a = Node(1, 0, 0)
a.x = 2
a.y = 0
b = Node(0, 1, 0)
b.x = 0
b.y = 0
c = Node(0, 0, 1)
c.x = 1
c.y = sqrt(3) / 2
conns = [Connection(a, b), Connection(b, c), Connection(c, a)]
update = conns[:]


def visualizeNet(conns):
    bitmap_dimension = (600, 400)
    im = Image.new('RGB', bitmap_dimension, 'white')
    draw = ImageDraw.Draw(im)
    for j in conns:
        a = j.node1
        b = j.node2
        draw.line((a.x * 200 + 100, a.y * 200 + 100, b.x *
                   200 + 100, b.y * 200 + 100), "black")
        #draw.ellipse((a.x*200 - 3 + 100, a.y*200 - 3 + 100, a.x*200 + 3 + 100, a.y*200 + 3 + 100), "black")
        #draw.ellipse((b.x*200 - 3 + 100, b.y*200 - 3 + 100, b.x*200 + 3 + 100, b.y*200 + 3 + 100), "black")
    im.save('mountain_python.bmp')
    im.show('mountain_python.bmp')


for i in range(iters):
    new_nodes = []
    for j in conns:
        a = j.node1
        b = j.node2
        midpoint = Node((a.bary1 + b.bary1) / 2, (a.bary2 +
                                                  b.bary2) / 2, (a.bary3 + b.bary3) / 2)
        midpoint.x = j.midpoint_x + r * random.random() * j.length - r * j.length / 2
        midpoint.y = j.midpoint_y + r * random.random() * j.length - r * j.length / 2
        update.remove(j)
        update.append(Connection(a, midpoint))
        update.append(Connection(midpoint, b))
        new_nodes.append(midpoint)
    for j in new_nodes:
        n = Node(j.bary1 + 1 / (2**(i + 1)),
                 j.bary2 - 1 / (2**(i + 1)), j.bary3)
        m = Node(j.bary1 + 1 / (2**(i + 1)),
                 j.bary2, j.bary3 - 1 / (2**(i + 1)))
        k = Node(j.bary1, j.bary2 + 1 / (2**(i + 1)),
                 j.bary3 - 1 / (2**(i + 1)))
        if n in new_nodes:
            update.append(Connection(new_nodes[new_nodes.index(n)], j))
        if m in new_nodes:
            update.append(Connection(new_nodes[new_nodes.index(m)], j))
        if k in new_nodes:
            update.append(Connection(new_nodes[new_nodes.index(k)], j))
    conns = update[:]
visualizeNet(conns)
