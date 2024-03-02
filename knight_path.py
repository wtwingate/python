import re

# A little program that calculates the shortest path for a Knight to
# move from one square to another on a chessboard.


class Knight:
    def __init__(self, coords, prev=None):
        self.coords = coords
        self.prev = prev
        self.__deltas = (
            (1, 2),
            (2, 1),
            (-1, 2),
            (-2, 1),
            (1, -2),
            (2, -1),
            (-1, -2),
            (-2, -1),
        )
        self.moves = self.get_moves()

    def get_moves(self):
        coords = []
        for delta in self.__deltas:
            next_coords = []
            next_coords.append(self.coords[0] + delta[0])
            next_coords.append(self.coords[1] + delta[1])

            if 0 <= next_coords[0] <= 7 and 0 <= next_coords[1] <= 7:
                coords.append(next_coords)
        return coords


class Translator:
    def __init__(self):
        self.__translator_keys = {
            "1": 0,
            "2": 1,
            "3": 2,
            "4": 3,
            "5": 4,
            "6": 5,
            "7": 6,
            "8": 7,
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7,
        }

    def standard_to_numeric(self, start_pos, end_pos):
        trans_start = []
        trans_end = []

        trans_start.append(self.__translator_keys[start_pos[0]])
        trans_start.append(self.__translator_keys[start_pos[1]])
        trans_end.append(self.__translator_keys[end_pos[0]])
        trans_end.append(self.__translator_keys[end_pos[1]])

        return trans_start, trans_end


def find_path(start_pos, end_pos):
    queue = [Knight(start_pos)]

    while len(queue) > 0:
        current_knight = queue.pop(0)
        if current_knight.coords == end_pos:
            return current_knight
        for move in current_knight.moves:
            queue.append(Knight(move, current_knight))


def extract_path(knight):
    path = []
    current_knight = knight
    while current_knight != None:
        path.append(current_knight.coords)
        current_knight = current_knight.prev
    path.reverse()
    return path


def print_path(path):
    print(f"You reached your destination in {len(path)} moves!")
    print("Here is your path:")
    for pos in path:
        print(pos)


def get_start_pos():
    start_pos = None
    while not valid_input(start_pos):
        start_pos = input("Please enter your starting coordinates: ")
    return start_pos


def get_end_pos():
    end_pos = None
    while not valid_input(end_pos):
        end_pos = input("Please enter your starting coordinates: ")
    return end_pos


def valid_input(input):
    if len(input) != 2:
        return False
    elif re.match("^[a-h][1-8]$", input):
        return True
    else:
        return False


def main():
    start = [0, 0]
    end = [7, 7]
    print_path(extract_path(find_path(start, end)))


main()
