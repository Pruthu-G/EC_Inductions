
# Rover Pathfinding Simulation

## 📖 Overview
This Python program simulates a rover navigating a 2D grid map. The rover can move up, down, left, or right, avoiding obstacles, and keeps track of battery consumption based on the number of steps taken to reach a target position using **Breadth-First Search (BFS)**.

## 📦 Classes & Methods

### `class Position`
Represents a cell on the map.

- **Attributes:**
  - `x (int)` — X-coordinate.
  - `y (int)` — Y-coordinate.
  - `traversable (bool)` — Whether the position can be passed through (default `True`).

### `class Map`
Represents the 2D grid map for the rover.

- **Attributes:**
  - `width (int)` — Width of the map.
  - `height (int)` — Height of the map.
  - `grid (list of list of Position)` — 2D grid of `Position` objects.

- **Method:**
  - `get_position(x, y)` — Returns the `Position` at `(x, y)` if within bounds; otherwise, returns `None`.

### `class Rover`
Represents the rover navigating the map.

- **Attributes:**
  - `battery (int)` — Battery level (starts at 100%).
  - `position (Position)` — Current position of the rover.

- **Method:**
  - `traverse(target, map_obj)`  
    Navigates the rover from its current position to a target position using **BFS**.

    - **Arguments:**
      - `target (Position)` — Destination to reach.
      - `map_obj (Map)` — Map object representing the environment.

    - **Returns:**
      - Number of steps taken to reach the target.
      - `-1` if the target is unreachable.

    - **Effects:**
      - Reduces `battery` by the number of steps taken.
      - Updates `position` to the target location if reachable.

## 🚀 Program Flow
1. A 10×10 grid is created.
2. An obstacle is placed at `(2, 2)`.
3. A rover is initialized at `(0, 0)`.
4. The rover attempts to navigate to `(9, 9)`.
5. The program prints:
   - Number of steps taken.
   - Remaining battery percentage.

## 📌 Example Output
```
Steps taken: 18
Battery remaining: 82%
```

## 📦 Dependencies
- `collections.deque` for efficient queue operations in BFS.

## 📌 Notes
- Empty grid cells are traversable unless explicitly marked otherwise.
- The BFS ensures the shortest path is found.
- Battery decreases by **1% per step** taken.
