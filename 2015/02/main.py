import os
os.chdir('./2015/02/')


def main():
    part1()
    part2()


def calculateWrappingPaper(length, width, height):
    side1 = length * width
    side2 = width * height
    side3 = height * length

    smallest_side = min(side1, side2, side3)

    surface_area = (2*side1) + (2*side2) + (2*side3)

    required_wrapping_paper = surface_area + smallest_side

    return required_wrapping_paper


def part1():
    total = 0

    with open('input.txt', 'r') as f:
        for line in f:
            dimensions = [int(d) for d in line.split('x')]
            l, w, h = dimensions
            total += calculateWrappingPaper(l, w, h)

    print(total)


def part2():
    total = 0
    with open('input.txt', 'r') as f:
        for line in f:
            dimensions = [int(d) for d in line.split('x')]
            l, w, h = dimensions
            total += calculateRibbon(l, w, h)
    print(total)


def calculateRibbon(length, width, height):
    # 2x3x4 dimensions requires 2+2+3+3 = 10 feet of ribbon to wrap
    #                       and 2*3*4   = 24 feet of ribbon for the bow,
    # for a total of 34 feet
    dimensions = [length, width, height]
    dimensions.sort()
    first_smallest = dimensions[0]
    second_smallest = dimensions[1]

    ribbon_for_wrap = (2*first_smallest) + (2*second_smallest)
    ribbon_for_bow = length * width * height

    required_ribbon = ribbon_for_wrap + ribbon_for_bow
    return required_ribbon


if __name__ == "__main__":
    main()
