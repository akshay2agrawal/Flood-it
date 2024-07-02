import random

class FloodItGame:
    def __init__(self, size, num_colors):
        self.size = size
        self.num_colors = num_colors
        self.board = self._create_board()
        self.moves = 0

    def _create_board(self):
        board = []
        for row in range(self.size):
            new_row = []
            for col in range(self.size):
                # Generate a random color (represented by an integer)
                random_color = random.randint(0, self.num_colors - 1)
                new_row.append(random_color)
            board.append(new_row)
        return board

    def __str__(self):
        board_string = ""
        for row in self.board:
            # Convert each number in the row to a string
            row_string = ' '.join(str(cell) for cell in row)
            # Add this row to the board string
            board_string += row_string + '\n'
        # Remove the last newline character
        return board_string.strip()

    def _flood_fill(self, color):
            origin_color = self.board[0][0]
            # If the color matches the origin, no changes occur
            if origin_color == color:
                return

            stack = [(0, 0)] # DFS stack
            visited = set()

            while stack:
                x, y = stack.pop()
                # Discard and continue with other tiles if a tile is already visited or does not have the same color as origin.
                if (x, y) in visited or self.board[x][y] != origin_color:
                    continue

                visited.add((x, y))
                # Change to new color
                self.board[x][y] = color

                # move forward, add the neighbouring nodes to stack
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.size and 0 <= ny < self.size:
                        stack.append((nx, ny))

    def make_move(self, color):
        self._flood_fill(color)
        self.moves += 1

    def is_solved(self):
        # Get the color of the top-left corner tile
        target_color = self.board[0][0]
        
        # Check each tile on the board
        for row in range(self.size):
            for col in range(self.size):
                current_color = self.board[row][col]
                # If any tile doesn't match the target color, the puzzle isn't solved
                if current_color != target_color:
                    return False
        
        # If we've checked all tiles and haven't returned False, the puzzle is solved
        return True

def get_best_move(game):
    origin_color = game.board[0][0]
    color_counts = [0] * game.num_colors

    def count_connected(x, y, color, visited):
        # Check if the current position is out of bounds or already visited
        if (x, y) in visited or x < 0 or x >= game.size or y < 0 or y >= game.size:
            return 0  # Stop recursion
        
        # Check if the current tile matches the target color
        if game.board[x][y] != color and (x, y) != (0, 0):
            return 0  # Stop recursion if color doesn't match (except for origin)
        
        visited.add((x, y))
        count = 1
        
        # Recursively check all four adjacent tiles (right, down, left, up)
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            count += count_connected(x + dx, y + dy, color, visited)
        
        return count

    # Count tiles already connected to origin
    connected_to_origin = count_connected(0, 0, origin_color, set())

    for color in range(game.num_colors):
        if color == origin_color:
            color_counts[color] = connected_to_origin
        else:
            color_counts[color] = count_connected(0, 0, color, set())

    max_count = max(color_counts)
    
    # Find all colors that have the maximum count
    best_colors = [color for color, count in enumerate(color_counts) if count == max_count]
    
    # Return the lowest ranked color among the best colors
    return min(best_colors)

def greedy_solve(game):
    moves = []
    max_moves = game.size * game.size  # upper bound on number of moves
    while not game.is_solved() and len(moves) < max_moves:
        best_color = get_best_move(game)
        if best_color == game.board[0][0]:
            # If best move is current color, choose next available color
            best_color = (best_color + 1) % game.num_colors
        game.make_move(best_color)
        print(f'\nMove made for color: {best_color}')
        print(f"{game}")
        moves.append(best_color)
    return moves

if __name__ == "__main__":
    # Example usage
    game = FloodItGame(6, 3)
    print("Initial board:")
    print(game)
    moves = greedy_solve(game)
    print(f"\nSolved in {len(moves)} moves: {moves}")