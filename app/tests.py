import numpy as np
from mock import patch

from app import app


class TestGraphicEditor:
    """
    Run tests on GraphicEditor
    """
    def setup(self):
        pass

    def test_create_matrix(self):
        matrix = app.create_matrix(5, 6)
        expected_matrix = np.array([['O', 'O', 'O', 'O', 'O'],
                                   ['O', 'O', 'O', 'O', 'O'],
                                   ['O', 'O', 'O', 'O', 'O'],
                                   ['O', 'O', 'O', 'O', 'O'],
                                   ['O', 'O', 'O', 'O', 'O'],
                                   ['O', 'O', 'O', 'O', 'O']], dtype='<U1')
        assert (matrix == expected_matrix).all()

    def test_read_command(self):
        keys = ["", "I 5 6\n", "L 2 3 A\n", "", "ABC", "X", "\n"]
        with patch.object(app, 'input', return_value=None) as app_input:
            # option X cancel iteration of for loop
            # on read_command function
            app_input.side_effect = keys
            parsed_commands = app.read_command()
            assert parsed_commands == [
                ['I', '5', '6'],
                ['L', '2', '3', 'A'],
                ['X']
            ]

    def test_execute_commands(self):
        parsed_commands = [
            ['I', '5', '6'],
            ['L', '2', '3', 'A'],
            ['S', 'one.bmp'],
            ['G', '2', '3', 'J'],
            ['V', '2', '3', '4', 'W'],
            ['H', '3', '4', '2', 'Z'],
        ]
        assert app.execute_commands(parsed_commands)
