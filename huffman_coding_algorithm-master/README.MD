This script can be invoked directly by the python interpreter. It takes as input a text file
that describes an instance of a huffman coding problem. This first line is the number of
symbols in the file. Each following line has weights that correspond to the line number,
i.e. line 2 is 4029539 corresponding to a letter weight pair (1, 4029539).

This code will build a huffman encoding tree and return the maximum and minimum length code
word in the resulting huffman code.

the algorithm begins by building a list of these symbols by iterating over the input file
and creating a list of tuples symbol_list. This list is then put into a minimum heap that
is intended to be mutable. The method __huffman_tree is invoked and returns the object
representing a huffman tree.

__huffman_tree works as follows:

While there is more than one tuple pair within the symbol_heap minimum heap, the first two
tuples of minimum weight are popped from the queue. These two letters are committed to being
siblings within the product tree. Their weight is combined and the two letters are combined
into a "meta letter" represented as a Node object with references to a left letter and a right
letter. Take for example a small set of 8 letters. . .

    symbol_heap = [(2, E), (6, A), (5, B), (9, C), (3, D), (6, F), (8, G), (7, H)]
    length: 8

the min-heap structure bubbles the two minimum values to the front of the heap:

    letter_1 = [(2, E) ... ].pop()
    letter_2 = [(3, D) ... ].pop()

combined weight = 2 + 3
    meta_letter = Node(D, E)

the min-heap after the first call looks like this. .

    symbol_heap = [(5, B), (5, Node(D, E)), (6, A), (9, C), (6, F), (8, G), (7, H)]
    length: 7

let's iterate through this and view the changes. . 

second call:
    [(6, A), (6, F), (10, Node(B, Node(D, E))), (9, C), (8, G), (7, H)]
    length: 6

third call:
    [(7, H), (12, Node(A, F)), (10, Node(B, Node(D, E))), (9, C), (8, G)]
    length: 5

fourth call:
    [(9, C), (12, Node(A, F)), (10, Node(B, Node(D, E))), (15, Node(G, H))]
    length: 4

fifth call:
    [(12, Node(A, F)), (15, Node(G, H)), (19, Node(C, Node(B, Node(D, E))))]
    length: 3

sixth call:
    [(27, Node(Node(A, F), Node(G, H))), (19, Node(C, Node(B, Node(D, E)))]
    length: 2

seventh call: 
    [(46, Node(Node(Node(A, F), Node(G, H))), Node(C, Node(B, Node(D, E))))]
    END WHILE

__huffman_tree returns a tuple with the nodes stacked in layers. These nodes were created
from the original set of all weight-letter tuples. The first call paired D, E, who becomes
the lowest set of leaves in the tree. node D & E is paired with sibling B in the second
call. In the third, A & F are paired. Fourth, G & H. Fifth, C with the node whose siblings
B and the pair D & E. This forms the right branch of the tree. Sixth, A, F, G, & H become
siblings in the tree. Last, the two brances of the tree are joined in the seventh call.

The huffman codes generated in this example are:

A  000
B  110
C  10
D  1110
E  1111
F  001
G  010
H  011

This is how the __huffman_tree algorithm generates a huffman tree representing the sought
after encoding. 

This tree can be unraveled by a recursive algorithm, walk_tree.

walk_tree begins by taking this processed tree at the root. It begins with an empty python
dictionary and an empty prefix string that is populated by recursive calls of the walk_tree
algorithm that spread exponentially. This is quite complex, but is mapped out below.

walk_tree accounts for 4 cases of that are found walking the tree.

For each node "meta-letter"
    for the left child:
        if the left branch is also a node,  call walk_tree recursively, add a 0 to prefix
        else a leaf has been reached, add this leaf to the code dictionary with prefix + 0

    for the left child:
        if the right branch is also a node, call walk_tree recursively add a 1 to prefix
        else a leaf has been reached, add this leaf to the code dictionary with prefix + 1

At each node, if either child is itself a node, walk_tree must be called again in order to
split the prefix code. e.g. if level 0 and 1 of the left-branch have no leaves, walk-tree
must be called at level 1 twice. This gives the left child a prefix 00 and the right child
a prefix 11. Effectively, this walks the tree, by allowing the generation of prefix codes
upon divergence at each node. These codes are saved into the code dictionary that is returned
once every leaf has been reached. In python as this dictionary code is the same object used in
each recursive call. rule: Default parameter values are evaluated when, and only when, the
"def" statement they belong to is executed. This object is sticky and persists throughout the
recursion, never duplicated, and only appended to when a leaf is reached.
