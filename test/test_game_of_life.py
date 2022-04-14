import unittest
import io
import contextlib

from src.game_of_life import GameOfLife

class GameOfLifeTest(unittest.TestCase):

    def test_dies_by_underpopulation(self):
        game = GameOfLife()
        fake_stdout = io.StringIO()

        with contextlib.redirect_stdout(fake_stdout):
            game.run("0,0 -1,0 1,0")

        output = fake_stdout.getvalue()
        fake_stdout.close()

        self.assertEqual(output.strip(), "0,0")
