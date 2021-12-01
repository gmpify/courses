class Matrix:
    def __init__(self, matrix_string):
        rows_string = matrix_string.splitlines()

        self.matrix = [[int(x) for x in row.split()] for row in rows_string]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.matrix]
