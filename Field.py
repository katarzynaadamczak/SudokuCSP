import numpy as np


class Field:
    def __init__(self, number, example, row, column):
        self.number = number
        self.domain = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.from_example = example
        self.row = row
        self.column = column

    def get_domain_size(self):
        return self.domain.size
