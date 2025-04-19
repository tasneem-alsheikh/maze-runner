"""
Main entry point for the maze runner game.
"""

import argparse
from src.game import run_game
from src.explorer import Explorer
from src.maze import create_maze
from src.explorer_enhanced import Explorer

def main():
    maze = create_maze(30, 30, "static")
    explorer = Explorer(maze, visualize=False)
    time_taken, moves = explorer.solve()
    backtrack_count = explorer.backtrack_count
    
    print("\n=== Static Maze Solo Run ===")
    print(f"Time = {time_taken:.2f}s, Moves = {len(moves)}, Backtracks = {backtrack_count}")
    print("=============================")

if __name__ == "__main__":
    main()
