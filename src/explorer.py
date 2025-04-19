"""
Maze Explorer module with enhanced solving.
"""
import time
import pygame
from heapq import heappush, heappop
from typing import Tuple, List
from src.constants import BLUE, WHITE, CELL_SIZE, WINDOW_SIZE

class Explorer:
    def __init__(self, maze, visualize: bool = False):
        self.maze = maze
        self.x, self.y = maze.start_pos
        self.moves = []
        self.start_time = None
        self.end_time = None
        self.visualize = visualize
        self.visited = set()  # Track all visited positions
        self.backtrack_count = 0
        if visualize:
            pygame.init()
            self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
            pygame.display.set_caption("Maze Explorer - Enhanced")
            self.clock = pygame.time.Clock()

    def heuristic(self, pos: Tuple[int, int]) -> int:
        """A* heuristic: Manhattan distance to end."""
        x, y = pos
        end_x, end_y = self.maze.end_pos
        return abs(x - end_x) + abs(y - end_y)

    def can_move_to(self, x: int, y: int) -> bool:
        """Check if a position is valid and open."""
        return (0 <= x < self.maze.width and 
                0 <= y < self.maze.height and 
                self.maze.grid[y][x] == 0)

    def draw_state(self):
        """Draw the maze and explorer (simplified)."""
        self.screen.fill(WHITE)
        for y in range(self.maze.height):
            for x in range(self.maze.width):
                if self.maze.grid[y][x] == 1:
                    pygame.draw.rect(self.screen, (0, 0, 0),
                                    (x * CELL_SIZE, y * CELL_SIZE,
                                    CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(self.screen, (0, 255, 0),
                        (self.maze.start_pos[0] * CELL_SIZE,
                        self.maze.start_pos[1] * CELL_SIZE,
                        CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(self.screen, (255, 0, 0),
                        (self.maze.end_pos[0] * CELL_SIZE,
                        self.maze.end_pos[1] * CELL_SIZE,
                        CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(self.screen, BLUE,
                        (self.x * CELL_SIZE, self.y * CELL_SIZE,
                        CELL_SIZE, CELL_SIZE))
        pygame.display.flip()
        self.clock.tick(30)

    def print_statistics(self, time_taken: float):
        """Print exploration stats."""
        print("\n=== Maze Exploration Statistics ===")
        print(f"Total time taken: {time_taken:.2f} seconds")
        print(f"Total moves made: {len(self.moves)}")
        print(f"Number of backtrack operations: {self.backtrack_count}")
        print(f"Average moves per second: {len(self.moves)/time_taken:.2f}")
        print("==================================\n")

    def solve(self) -> Tuple[float, List[Tuple[int, int]]]:
        """
        Solve with A* algorithm and visited tracking.
        """
        self.start_time = time.time()
        
        # Improvement 1: A* with priority queue
        queue = [(self.heuristic((self.x, self.y)), 0, (self.x, self.y))]
        came_from = {}
        g_scores = {self.maze.start_pos: 0}
        self.visited.add((self.x, self.y))

        while queue:
            _, g, (x, y) = heappop(queue)
            self.x, self.y = x, y
            self.moves.append((x, y))

            if (x, y) == self.maze.end_pos:
                break

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                if not self.can_move_to(new_x, new_y):
                    continue

                # Improvement 2: Skip visited spots to avoid loops
                if (new_x, new_y) in self.visited:
                    self.backtrack_count += 1
                    continue

                tentative_g = g + 1
                if tentative_g < g_scores.get((new_x, new_y), float('inf')):
                    came_from[(new_x, new_y)] = (x, y)
                    g_scores[(new_x, new_y)] = tentative_g
                    f_score = tentative_g + self.heuristic((new_x, new_y))
                    heappush(queue, (f_score, tentative_g, (new_x, new_y)))
                    self.visited.add((new_x, new_y))

            if self.visualize:
                self.draw_state()

        # Reconstruct the optimal path
        current = self.maze.end_pos
        self.moves = []
        while current in came_from:
            self.moves.append(current)
            current = came_from[current]
        self.moves.append(self.maze.start_pos)
        self.moves.reverse()

        self.end_time = time.time()
        time_taken = self.end_time - self.start_time
        
        if self.visualize:
            pygame.time.wait(2000)
            pygame.quit()
        
        self.print_statistics(time_taken)
        return time_taken, self.moves
