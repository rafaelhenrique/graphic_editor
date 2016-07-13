import numpy as np


def create_matrix(columns=0, lines=0):
    """Create matrix columns x lines (m x n)"""
    try:
        columns = int(columns)
        lines = int(lines)
        line = ["O" for _ in range(columns)]
        return np.array([line for _ in range(lines)])
    except ValueError:
        msg = ("Invalid values: columns={!r}, lines={!r}\n"
               "Only integer values are accepted on create_matrix").format(
               columns, lines)
        print(msg)


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
    return True
