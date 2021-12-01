def print_row_grid(number_of_columns, cell_size):
    for _ in range(number_of_columns):
        print('+', '- ' * cell_size, end = '')
    print('+')

def print_column_grid(number_of_columns, cell_size):
    for _ in range(number_of_columns):
        print('|', '  ' * cell_size, end = '')
    print('|')

def print_table(number_of_rows, number_of_columns, cell_size = 4):
    for _ in range(number_of_rows):
        print_row_grid(number_of_columns, cell_size)
        for __ in range(cell_size):
            print_column_grid(number_of_columns, cell_size)
    print_row_grid(number_of_columns, cell_size)

print_table(4, 3)
