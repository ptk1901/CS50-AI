class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count
sentence3 = Sentence()
sentence = Sentence((1,2) , 5)
sentence.cells.add((3,4))
sentence.cells.add((5,6))
sentence.count = 5
sentence2 = Sentence((3,4) , 4)
sentence2.cells.add((5,8))
sentence2.cells.add((5,7))
sentence2.count = 7
print(sentence.cells & sentence2.cells)
if (sentence.cells & sentence2.cells == set()):
    print("hi")

