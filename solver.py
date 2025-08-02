import possible_moves
import queue
from collections import defaultdict


class Solver:
    def __init__(self):
        self.cube = possible_moves.MovesAndActions()
        self.cube.scramble(10)
        self.shuffled = self.cube.current[:]
        self.actions = [[self.cube.front, self.cube.back,  self.cube.top, self.cube.bottom,  self.cube.right,
                        self.cube.left],  [self.cube.front_prime, self.cube.back_prime, self.cube.top_prime,
                                           self.cube.bottom_prime, self.cube.right_prime, self.cube.left_prime]]
        self.moveQueue = queue.Queue()
        self.backMoveQueue = queue.Queue()
        self.moveQueue.put(self.cube.current)
        self.backMoveQueue.put(self.cube.solved_array)
        self.front_visited = defaultdict(int)
        self.back_visited = defaultdict(int)
        self.back_visited[''.join(self.cube.solved_array)] = 1
        self.route = []
        self.total_moves, self.count = 0, 0
        self.parent, self.child = {}, {}
        self.found_connect = None

    def start_bfs(self, runs):
        cur_root = self.moveQueue.get()
        if cur_root == self.cube.solved_array:
            print('solution found in first pass raw')
            self.found_connect = cur_root
            return cur_root
        if self.count < runs:
            self.count += 1
            if cur_root:
                temp = cur_root[:]
                temp_string = ''.join(temp)
                for i in range(len(self.actions)):
                    for j in range(len(self.actions[0])):
                        res = self.actions[i][j](temp)
                        res_string = ''.join(res)
                        if self.front_visited[res_string] > 0:
                            continue
                        else:
                            self.moveQueue.put(res)
                            self.front_visited[res_string] = 1
                            self.parent[res_string] = temp_string

                        if self.back_visited[res_string] > 0:
                            print('solution found through 2 sided')
                            self.found_connect = res
                            return res

            self.start_bfs(runs)

    def second_bfs(self, runs):
        cur_root = self.backMoveQueue.get()
        if self.count < runs:
            self.count += 1
            if cur_root:
                temp = cur_root[:]
                temp_string = ''.join(temp)
                for i in range(len(self.actions)):
                    for j in range(len(self.actions[0])):
                        res = self.actions[i][j](temp)
                        res_string = ''.join(res)
                        if self.back_visited[res_string] > 0:
                            self.total_moves += 1
                            continue
                        else:
                            self.backMoveQueue.put(res)
                            self.back_visited[res_string] = 1
                            self.child[res_string] = temp_string

                        if self.front_visited[res_string] > 0:
                            print('solution found back pass')
                            self.found_connect = res
                            return res
            self.second_bfs(runs)

    def run_bfs(self):
        while not self.found_connect:
            self.start_bfs(5)
            self.count = 0
            self.second_bfs(5)
            self.count = 0
        return 0

    def path_find(self):
        temp_path = []
        cur = ''.join(self.found_connect[:])
        while cur != ''.join(self.shuffled):
            temp_path.append(self.parent[cur])
            cur = self.parent[cur]
        temp_path.reverse()
        cur = ''.join(self.found_connect[:])
        while cur != ''.join(self.cube.solved_array):
            cur = self.child[cur]
            temp_path.append(cur)
        self.route = temp_path
        self.total_moves = len(temp_path)

    def find_solution(self):
        print('The Starting Shuffled Array: ')
        print(self.shuffled, '\n')
        self.run_bfs()
        self.path_find()
        print(self.total_moves, "Steps needed to find Solution\n")
        print('Path to solution: ')
        print(self.route)


if __name__ == '__main__':
    solve = Solver()
    solve.find_solution()

#python solver.py