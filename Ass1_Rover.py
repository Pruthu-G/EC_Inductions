from collections import deque

class Position:
    def __init__(self, x, y, traversable=True):
        self.x = x
        self.y = y
        self.traversable = traversable

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[Position(x, y) for y in range(height)] for x in range(width)]

    def get_position(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[x][y]
        return None

class Rover:
    def __init__(self, start_position):
        self.battery = 100
        self.position = start_position

    def traverse(self, target, map_obj):
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False for _ in range(map_obj.height)] for _ in range(map_obj.width)]
        queue = deque()

        queue.append((self.position.x, self.position.y, 0))
        visited[self.position.x][self.position.y] = True

        while queue:
            x, y, steps = queue.popleft()

            if (x, y) == (target.x, target.y):
                self.battery -= steps
                self.position = target
                return steps

            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < map_obj.width and 0 <= ny < map_obj.height:
                    next_pos = map_obj.get_position(nx, ny)
                    if not visited[nx][ny] and next_pos.traversable:
                        queue.append((nx, ny, steps + 1))
                        visited[nx][ny] = True

        return -1

# Example test run (Remove before submitting if required)
if __name__ == "__main__":
    my_map = Map(10, 10)
    my_map.grid[2][2].traversable = False  # example obstacle

    start = my_map.get_position(0, 0)
    target = my_map.get_position(9, 9)
    rover = Rover(start)

    steps_taken = rover.traverse(target, my_map)
    print(f"Steps taken: {steps_taken}")
    print(f"Battery remaining: {rover.battery}%")
