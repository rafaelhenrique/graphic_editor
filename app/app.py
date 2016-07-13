import numpy as np


def create_matrix(columns=0, lines=0):
    """Create matrix columns x lines (m x n)"""
    columns = int(columns)
    lines = int(lines)
    line = ["O" for _ in range(columns)]
    return np.array([line for _ in range(lines)])


def color_pixel(matrix, column, line, color):
    column = int(column) - 1
    line = int(line) - 1
    matrix[line][column] = color


def write_image(matrix, filename):
    np.savetxt(filename, matrix, delimiter="", fmt="%s")


def read_command():
    """Read commands and return parsed lines"""
    commands = []
    while True:
        command_line = input()
        command_line = command_line.split()
        valid_commands = ('I', 'C', 'L', 'V', 'H', 'K', 'F', 'S', 'X')

        if not command_line:
            continue

        if command_line[0] not in valid_commands:
            continue

        commands.append(command_line)
        if command_line[0] == "X":
            break
    return commands


def execute_commands(parsed_commands):
    """Execute parsed commands to manipulate matrix"""
    for command_line in parsed_commands:
        if command_line[0] == "I" and len(command_line) == 3:
            columns, lines = command_line[1:]
            matrix = create_matrix(columns, lines)
        if command_line[0] == "L" and len(command_line) == 4:
            column, line, color = command_line[1:]
            color_pixel(matrix, column, line, color)
        if command_line[0] == "S" and len(command_line) == 2:
            filename = command_line[1]
            write_image(matrix, filename)
    return True
