def print_grid(cols, rows, width, height):
    """Draws a grid from arguments for cols, rows, cell width & height"""

    line_a = '+ ' + '- '* width
    line_b = '| ' + '  '* width
    print(line_a * cols + '+')

    def row_height(line_b, line_a):
        for i in range(0, height):
            print(line_b)
        print(line_a)

    def print_row():
        row_height(line_b * cols + '|', line_a * cols + '+')

    for i in range(0, rows):
        print_row()

print_grid(cols = 6, rows = 4, width = 5, height = 2)
