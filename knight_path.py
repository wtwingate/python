import re

# A little program that calculates the shortest path for a Knight to
# move from one square to another on a chessboard.


RANKS = {
    "1": 0,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
}

FILES = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
}


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
        print(translate_coords(pos), end=" ")
    print()


def translate_coords(position):
    for key, value in FILES.items():
        if value == position[0]:
            file = key
    for key, value in RANKS.items():
        if value == position[1]:
            rank = key
    return file + rank


def get_position(pos_name):
    position = None
    while True:
        position = input(f"Enter your {pos_name} position: ").lower()
        if valid_input(position):
            break
    return position


def valid_input(input):
    if input == None:
        return False
    elif re.match("^[a-h][1-8]$", input):
        return True
    else:
        return False


def translate_notation(position):
    translated_pos = []
    translated_pos.append(FILES[position[0]])
    translated_pos.append(RANKS[position[1]])
    return translated_pos


def introduction():
    print(
        """
This program caculates the shortest path for a Knight to move
between any two locations on a chessboard.

Simply enter your starting and ending positions using standard
"file-first" algebraic notation (files are labeled a - h, and
ranks are labeled 1 - 8.) Then, sit back and watch the algorithm
do its magic!

Note: there are often multiple "shortest" paths that a Knight
can take. This program only prints out the first one it finds.
"""
    )


def main():
    introduction()
    start_pos = translate_notation(get_position("starting"))
    end_pos = translate_notation(get_position("ending"))
    print_path(extract_path(find_path(start_pos, end_pos)))


main()
