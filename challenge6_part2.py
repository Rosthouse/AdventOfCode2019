# Advent of Code 2019: Day 6, Part 2
# https://adventofcode.com/2019/day/6

from anytree import Node, RenderTree, AsciiStyle, search, PreOrderIter, util

def create_orbit_tree(orbits: [str]) -> Node:
    root = Node("COM")
    for orbit in orbits:
        planets = orbit.strip().split(")")
        parent = search.find(root, lambda n: n.name == planets[0])
        if parent == None:
            parent = Node(planets[0], root)
        
        child = search.find(root, lambda n: n.name == planets[1])
        if child == None:
            child = Node(planets[1], parent)
        else:
            child.parent = parent
        
    return root

def count_orbits(tree) -> int:
    ancestorCounts: [int] = [len(node.ancestors) for node in PreOrderIter(tree)]
    count = 0 # Why 1: the first node has 0 ancestors and would therefore count as -1 orbits in the first loop. This just corrects that.
    for i in ancestorCounts:
        count += i
    
    return count

def count_orbital_transfers(tree: Node, fr: str, to) -> int:
    fromNode: Node = search.find(tree, lambda n: n.name == fr)
    toNode: Node = search.find(tree, lambda n: n.name == to)
    commonAncestor: Node = util.commonancestors(fromNode, toNode)[-1]

    return fromNode.parent.depth - commonAncestor.depth + toNode.parent.depth - commonAncestor.depth


def print_tree(tree) -> None:
    for pre, _, node in RenderTree(orbitTree, style=AsciiStyle()):
        print("%s%s" % (pre, node.name))
        input()


inputText = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN""".splitlines()

orbitTree = create_orbit_tree(inputText)
# print_tree(orbitTree)
print("Expected 4: " + str(count_orbital_transfers(orbitTree, "YOU", "SAN")))

orbitInput = open("./res/challenge6.txt").readlines()
orbitTree = create_orbit_tree(orbitInput)
# # print_tree(orbitTree)
# print("Counted orbits: " + str(count_orbits(orbitTree)))
print("Orbital Transfers: " + str(count_orbital_transfers(orbitTree, "YOU", "SAN")))


