# Maze Explorer Game

A simple maze exploration game built with Pygame where you can either manually navigate through a maze or watch an automated solver find its way to the exit.

## Getting Started

### 1. Connect to Your VM

1. Open **<span style="color:red">Visual Studio Code</span>**
2. Install the "Remote - SSH" extension if you haven't already
3. Connect to your VM using SSH:
   - Press `Ctrl+Shift+P` to open the command palette
   - Type "Remote-SSH: Connect to Host..."
   - Enter your VM's SSH connection details
   - Enter your credentials when prompted

### 2. Project Setup

1. Clone this repository to your VM
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Game

### Basic Usage
Run the game with default settings (30x30 random maze):
```bash
python main.py
```

### Manual Mode (Interactive)
Use arrow keys to navigate through the maze:
```bash
# Run with default random maze
python main.py

# Run with static maze
python main.py --type static

# Run with custom maze dimensions
python main.py --width 40 --height 40
```

### Automated Mode (Explorer)
The explorer will automatically solve the maze and show statistics:

#### Without Visualization (Text-only)
```bash
# Run with default random maze
python main.py --auto

# Run with static maze
python main.py --type static --auto

# Run with custom maze dimensions
python main.py --width 40 --height 40 --auto
```

#### With Visualization (Watch the Explorer in Action)
```bash
# Run with default random maze
python main.py --auto --visualize

# Run with static maze
python main.py --type static --auto --visualize

# Run with custom maze dimensions
python main.py --width 40 --height 40 --auto --visualize
```

Available arguments:
- `--type`: Choose between "random" (default) or "static" maze generation
- `--width`: Set maze width (default: 30, ignored for static mazes)
- `--height`: Set maze height (default: 30, ignored for static mazes)
- `--auto`: Enable automated maze exploration
- `--visualize`: Show real-time visualization of the automated exploration

## Maze Types

### Random Maze (Default)
- Generated using depth-first search algorithm
- Different layout each time you run the program
- Customizable dimensions
- Default type if no type is specified

### Static Maze
- Predefined maze pattern
- Fixed dimensions (50x50)
- Same layout every time
- Width and height arguments are ignored

## How to Play

### Manual Mode
1. Controls:
- Use the arrow keys to move the player (<span style="color:blue">blue circle</span>)
- Start at the <span style="color:green">green square</span>
- Reach the <span style="color:red">red square</span> to win
- Avoid the <span style="color:black">black walls</span>

### Automated Mode
- The explorer uses the right-hand rule algorithm to solve the maze
- Automatically finds the path from start to finish
- Displays detailed statistics at the end:
  - Total time taken
  - Total moves made
  - Number of backtrack operations
  - Average moves per second
- Works with both random and static mazes
- Optional real-time visualization:
  - Shows the explorer's position in <span style="color:blue">blue</span>
  - Updates at 30 frames per second
  - Pauses for 2 seconds at the end to show the final state

## Project Structure

```
maze-runner/
├── src/
│   ├── __init__.py
│   ├── constants.py
│   ├── maze.py
│   ├── player.py
│   ├── game.py
│   └── explorer.py
├── main.py
├── requirements.txt
└── README.md
```

## Code Overview

### Main Files
- `main.py`: Entry point of the game. Handles command-line arguments and initializes the game with specified parameters.
- `requirements.txt`: Lists all Python package dependencies required to run the game.

### Source Files (`src/` directory)
- `__init__.py`: Makes the src directory a Python package.
- `constants.py`: Contains all game constants like colors, screen dimensions, cell sizes, and game settings.
- `maze.py`: Implements maze generation using depth-first search algorithm and handles maze-related operations.
- `player.py`: Manages player movement, collision detection, and rendering of the player character.
- `game.py`: Core game implementation including the main game loop, event handling, and game state management.
- `explorer.py`: Implements automated maze solving using the right-hand rule algorithm and visualization.

## Game Features

- Randomly generated maze using depth-first search algorithm
- Predefined static maze option
- Manual and automated exploration modes
- Real-time visualization of automated exploration
- Smooth player movement
- Collision detection with walls
- Win condition when reaching the exit
- Performance metrics (time and moves) for automated solving

## Development

The project is organized into several modules:
- `constants.py`: Game constants and settings
- `maze.py`: Maze generation and management
- `player.py`: Player movement and rendering
- `game.py`: Game implementation and main loop
- `explorer.py`: Automated maze solving implementation and visualization

## Student Questions

### Question 1 (10 points)
Explain how the automated maze explorer works. Your answer should include:
1. The algorithm used by the explorer
2. How it handles getting stuck in loops
3. The backtracking strategy it employs
4. The statistics it provides at the end of exploration

To answer this question:
1. Run the explorer both with and without visualization
2. Observe its behavior in different maze types
3. Analyze the statistics it provides
4. Read the source code in `explorer.py` to understand the implementation details

Your answer should demonstrate a clear understanding of:
- The right-hand rule algorithm
- The loop detection mechanism
- The backtracking strategy
- The performance metrics collected

### Question 2 (30 points)
Modify the main program to run multiple maze explorers simultaneously. This is because we want to find the best route out of the maze. Your solution should:
1. Allow running multiple explorers in parallel
2. Collect and compare statistics from all explorers
3. Display a summary of results showing which explorer performed best

*Hints*:
- To get full marks, use Celery and RabbitMQ to distribute the exploration tasks. If you don't use Celery, RabbitMQ and redis, you will still get marks but you will not get the full 30 points.
- Implement a task queue system
- Do not visualize the exploration, just run it in parallel
- Store results for comparison

**To answer this question:** 
1. Study the current explorer implementation
2. Design a parallel execution system
3. Implement task distribution
4. Create a results comparison system

### Question 3 (10 points)
Analyze and compare the performance of different maze explorers on the static maze. Your analysis should:

1. Run multiple explorers (at least 4 ) simultaneously on the static maze
2. Collect and compare the following metrics for each explorer:
   - Total time taken to solve the maze
   - Number of moves made
   - *Optional*:
     - Number of backtrack operations

3. What do you notice regarding the performance of the explorers? Explain the results and the observations you made.


### Question 4 (20 points)
Based on your analysis from Question 3, propose and implement enhancements to the maze explorer to overcome its limitations. Your solution should:

1. Identify and explain the main limitations of the current explorer:

2. Propose specific improvements to the exploration algorithm:

3. Implement at least two of the proposed improvements:

Your answer should include:
1. A detailed explanation of the identified limitations
2. Documentation of your proposed improvements
3. The modified code with clear comments explaining the changes

### Question 5 (20 points)

Compare the performance of your enhanced explorer with the original:
   - Run both versions on the static maze
   - Collect and compare all relevant metrics
   - Create visualizations showing the improvements
   - Document the trade-offs of your enhancements
Your answer should include:
1. Performance comparison results and analysis
2. Discussion of any trade-offs or new limitations introduced

### Final points 6 (10 points)
1. Solve the static maze in 150 moves or less to get 10 points.
2. Solve the static maze in 135 moves or less to get 15 points.
3. Solve the static maze in 130 moves or less to get 100% in your assignment.

### Bonus points
1. Fastest solver to get top  10% routes (number of moves)
2. Finding a solution with no backtrack operations
3. Least number of moves.