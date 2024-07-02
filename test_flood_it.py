import unittest
from flood_it import FloodItGame, greedy_solve

class TestFloodItGame(unittest.TestCase):
    def test_initialization(self):
        game = FloodItGame(5, 3)
        self.assertEqual(game.size, 5)
        self.assertEqual(game.num_colors, 3)
        self.assertEqual(len(game.board), 5)
        self.assertEqual(len(game.board[0]), 5)

    def test_make_move(self):
        game = FloodItGame(3, 2)
        game.board = [
            [0, 1, 1],
            [0, 1, 0],
            [1, 0, 1]
        ]
        game.make_move(1)
        self.assertEqual(game.board, [
            [1, 1, 1],
            [1, 1, 0],
            [1, 0, 1]
        ])
        self.assertEqual(game.moves, 1)

    def test_is_solved(self):
        game = FloodItGame(3, 2)
        game.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertTrue(game.is_solved())

        game.board = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        self.assertFalse(game.is_solved())

    def test_greedy_solve(self):
        game = FloodItGame(3, 2)
        game.board = [
            [0, 1, 1],
            [0, 1, 0],
            [1, 0, 1]
        ]
        moves = greedy_solve(game)
        self.assertTrue(game.is_solved())
        self.assertLessEqual(len(moves), 3)  # The optimal solution takes 2 moves, but greedy might take 3

if __name__ == '__main__':
    unittest.main()