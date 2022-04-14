import unittest
import io
import contextlib

from src.game_of_life import GameOfLife


class TestCase:
  def __init__(self, desc, pattern, x, y, result):
    self.desc = desc
    self.pattern = pattern
    self.x = x
    self.y = y
    self.result = result

class GameOfLifeTest(unittest.TestCase):

    def test_run_doesnt_do_much(self):
        game = GameOfLife()
        fake_stdout = io.StringIO()

        with contextlib.redirect_stdout(fake_stdout):
            game.run()

        output = fake_stdout.getvalue()
        fake_stdout.close()

        self.assertEqual(output, "I don't do much, yet.\n")

    def test_evolve(self):
        game = GameOfLife()
        fake_stdout = io.StringIO()
        tests = [
            TestCase("single square", ((1, 1)), 1, 1, 0)
        ]
        for t in tests:
            # set the state
            game.init(t.pattern)
            # test that the next evolution for a coordinate is correct
            result = game.evolve(t.x,t.y)

            print("Test %s, got %d, want %d" %( t.desc, result, t.result))
            self.assertEqual(t.result,result)
