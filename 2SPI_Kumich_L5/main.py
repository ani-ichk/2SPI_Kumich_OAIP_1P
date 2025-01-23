from groundhog_day import groundhog_day
from gears import gears
from brackets import brackets


def main():
    print(groundhog_day(['Groundhog Festival in Punxsutawney.',
                         'Groundhog Festival in Punksutawney.',
                         'Groundhog Festivel in Punxsutowney.']))
    print(gears([[0, 2, 30, 15], [14, 3, 21, 60], [7, 16, 4, 8]], 30, 7))
    print(brackets('[12 / (9) + 2(5{15 * <2 - 3>}6)]'))


if __name__ == "__main__":
    main()