from pathlib import Path
from typing import List, Tuple

def _get_commands() -> List[Tuple[str, int]]:

    data_path = Path('data/day2.txt')
    commands = []
    for line in data_path.read_text().split('\n'):
        direction, amount = line.split()
        commands.append((direction, int(amount)))

    return commands

def puzzle1():
    """
    get product of hoizontal and vertical position
    """

    commands = _get_commands()

    vertical = 0
    horizontal = 0
    for command in commands:

        match command[0]:
            case 'up':
                vertical -= command[1]
            case 'down':
                vertical += command[1]
            case 'forward':
                horizontal += command[1]

    return vertical * horizontal

def puzzle2():
    commands = _get_commands()

    vertical = 0
    horizontal = 0
    aim = 0
    for command in commands:

        match command[0]:
            case 'up':
                aim -= command[1]
            case 'down':
                aim += command[1]
            case 'forward':
                horizontal += command[1]
                vertical += command[1] * aim

    return vertical * horizontal

if __name__ == '__main__':
    print('puzzle1: ',puzzle1())
    print('puzzle2: ',puzzle2())