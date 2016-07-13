import numpy as np


def create_matrix(columns=0, lines=0):
    """Create matrix columns x lines (m x n)"""
    line = ["O" for _ in range(columns)]
    return np.array([line for _ in range(lines)])


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
