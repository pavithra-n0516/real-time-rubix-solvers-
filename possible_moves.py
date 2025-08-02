import random


class MovesAndActions:
    def __init__(self):
        self.solved_array = ['wbr', 'wrg', 'wgo', 'wob', 'rby', 'ryg', 'rgw', 'rwb', 'gwr', 'gry', 'gyo', 'gow',
                             'obw', 'owg', 'ogy', 'oyb', 'byr', 'brw', 'bwo', 'boy', 'ygr', 'yrb', 'ybo', 'yog']
        self.current = self.solved_array[:]
        self.front_twist_clockwise = {0: 1, 1: 2, 2: 3, 3: 0, 6: 11, 7: 8, 8: 13, 11: 12, 12: 17, 13: 18, 17: 6, 18: 7}
        self.right_twist_clockwise = {1: 5, 2: 6, 6: 20, 5: 23, 20: 14, 23: 13, 14: 2, 13: 1, 8: 9, 9: 10, 10: 11,
                                      11: 8}
        self.left_twist_clockwise = {0: 12, 3: 15, 12: 22, 15: 21, 22: 4, 21: 7, 4: 0, 7: 3, 16: 17, 17: 18, 18: 19,
                                     19: 16}
        self.top_twist_clockwise = {4: 5, 5: 6, 6: 7, 7: 4, 1: 17, 0: 16, 17: 21, 16: 20, 21: 9, 20: 8, 9: 1, 8: 0}
        self.bot_twist_clockwise = {12: 13, 13: 14, 14: 15, 15: 12, 3: 11, 2: 10, 11: 23, 10: 22, 23: 19, 22: 18, 19: 3,
                                    18: 2}
        self.back_twist_clockwise = {20: 21, 21: 22, 22: 23, 23: 20, 10: 5, 9: 4, 5: 16, 4: 19, 16: 15, 19: 14, 15: 10,
                                     14: 9}

    def front(self, change):
        copy = change[:]
        test = copy[:]
        for i in self.front_twist_clockwise:
            cur = i
            needed = self.front_twist_clockwise[i]
            test[needed] = copy[cur]
        return test

    def front_prime(self, change):
        copy = change[:]
        test = copy[:]
        for i in self.front_twist_clockwise:
            cur = self.front_twist_clockwise[i]
            needed = i
            test[needed] = copy[cur]
        return test

    def back(self, change):
        copy = change[:]
        test = copy[:]
        for i in self.back_twist_clockwise:
            cur = i
            needed = self.back_twist_clockwise[i]
            test[needed] = copy[cur]

        return test

    def back_prime(self, change):

        copy = change[:]
        test = copy[:]
        for i in self.back_twist_clockwise:
            needed = i
            cur = self.back_twist_clockwise[i]
            test[needed] = copy[cur]
        return test

    def right(self, change):

        copy = change[:]
        test = copy[:]
        for i in self.right_twist_clockwise:
            cur = i
            needed = self.right_twist_clockwise[i]
            test[needed] = copy[cur]
        return test

    def right_prime(self, change):
        copy = change[:]
        test = copy[:]
        for i in self.right_twist_clockwise:
            needed = i
            cur = self.right_twist_clockwise[i]
            test[needed] = copy[cur]
        return test

    def left(self, change):
        copy = change[:]
        test = copy[:]
        for i in self.left_twist_clockwise:
            cur = i
            needed = self.left_twist_clockwise[i]
            test[needed] = copy[cur]
        return test

    def left_prime(self, change):
        copy = change[:]
        test = copy[:]
        for i in self.left_twist_clockwise:
            needed = i
            cur = self.left_twist_clockwise[i]
            test[needed] = copy[cur]
        return test

    def top(self, change):
        copy = change[:]
        test = copy[:]
        for i in self.top_twist_clockwise:
            cur = i
            needed = self.top_twist_clockwise[i]
            test[needed] = copy[cur]
        return test

    def top_prime(self, change):
        copy = change[:]
        test = copy[:]
        for i in self.top_twist_clockwise:
            needed = i
            cur = self.top_twist_clockwise[i]
            test[needed] = copy[cur]
        return test

    def bottom(self, change):
        copy = change[:]
        test = copy[:]
        for i in self.bot_twist_clockwise:
            cur = i
            needed = self.bot_twist_clockwise[i]
            test[needed] = copy[cur]
        return test

    def bottom_prime(self, change):
        copy = change[:]
        test = copy[:]
        for i in self.bot_twist_clockwise:
            needed = i
            cur = self.bot_twist_clockwise[i]
            test[needed] = copy[cur]
        return test

    def scramble(self, moves):
        possible_moves = [self.front, self.front_prime, self.back, self.back_prime, self.top,
                          self.top_prime, self.bottom, self.bottom_prime, self.right, self.right_prime,
                          self.left, self.left_prime]
        for _ in range(moves):
            num = random.randint(0, 11)
            self.current = possible_moves[num](self.current)


if __name__ == '__main__':
    cube = MovesAndActions()
    print(cube.current)
    cube.scramble(15)
    print(cube.current)