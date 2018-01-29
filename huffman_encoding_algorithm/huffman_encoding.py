import Queue
from operator import itemgetter


class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Huffman_Algo:
    def __init__(self, file_string):
        INDEX_OFFSET = 1
        self.processed_tree = None
        self.symbol_list = []
        with open(file_string, 'r') as input_file:
            self.symbol_count = input_file.readline()
            print self.symbol_count
            # create list of tuples to represent letters
            for i, line in enumerate(input_file):
                letter = str(i + INDEX_OFFSET)
                weight = int(line.strip())
                print letter, weight
                huffman_letter = (weight, letter)
                self.symbol_list.append(huffman_letter)
        self.symbol_heap = Queue.PriorityQueue()
        # create heap of letters
        for letter in self.symbol_list:
            self.symbol_heap.put(letter)
        #build huffman_tree
        self.processed_tree = self.__huffman_tree()

    def print_symbol_list(self):
        for count, row in enumerate(self.symbol_list):
            if count % 5 == 0:
                print '({} {}), '.format(row[0], row[1])
            else:
                print('({} {}), '.format(row[0], row[1])),

    def __huffman_tree(self):
        while self.symbol_heap.qsize() > 1:
            letter_1, letter_2 = self.symbol_heap.get(), self.symbol_heap.get()
            meta_letter = Node(letter_1, letter_2)
            combined_weight = letter_1[0] + letter_2[0]
            self.symbol_heap.put((combined_weight, meta_letter))
        return self.symbol_heap.get()


class Huffman_Utility:
    @staticmethod
    def print_codes(algo, code):
        symbol_list = algo.symbol_list
        first_weight, first_letter = max(symbol_list, key=itemgetter(0))
        last_weight, last_letter = min(symbol_list, key=itemgetter(0))
        print "\t{:8}  {:10}  {:10}".format("letter", "weight", "code length")
        print "first:  {:<8}  {:<10}  {:<10}".format(
            first_letter, first_weight, len(code[first_letter]))
        print "last:   {:<8}  {:<10}  {:<10}".format(
            last_letter, last_weight, len(code[last_letter]))

    @staticmethod
    def walk_tree(vertex, prefix="", code={}):
        if isinstance(vertex[1].left[1], Node):
            Huffman_Utility.walk_tree(vertex[1].left, prefix + "0", code)
        else:
            code[vertex[1].left[1]] = prefix + "0"
        if isinstance(vertex[1].right[1], Node):
            Huffman_Utility.walk_tree(vertex[1].right, prefix + "1", code)
        else:
            code[vertex[1].right[1]] = prefix + "1"
        return code


def main():
    huffman_algo = Huffman_Algo("huffman_input.txt")
    huffman_code = Huffman_Utility.walk_tree(huffman_algo.processed_tree)
    Huffman_Utility.print_codes(huffman_algo, huffman_code)

main()
