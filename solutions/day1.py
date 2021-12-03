from pathlib import Path

def _get_depths():

    data_path = Path('data/day1.txt')
    depths = list(map(int, data_path.read_text().split('\n')))

    return depths

def puzzle1():
    """
    count how many times the depths increase
    """

    depths = _get_depths()

    return sum(x[1] > x[0] for x in zip(depths[:-1], depths[1:]))

def puzzle2():
    """
    count how many times the depths increase using a sliding window
    """

    depths = _get_depths()

    # depths = [199,200,208,210,200,207,240,269,260,263]

    window_sums = [sum(depths[i:i+3]) for i in range(len(depths)-2)]

    return sum(x[1] > x[0] for x in zip(window_sums[:-1], window_sums[1:]))


if __name__ == '__main__':
    print('puzzle1: ',puzzle1())
    print('puzzle2: ',puzzle2())