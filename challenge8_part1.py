# Advent of Code 2019: Day 8, Part 1
# https://adventofcode.com/2019/day/8


def decode(encoded: [int], width: int, height: int) -> [[int]]:
    decoded = []
    layers = int(len(encoded) / (width * height))
    for l in range(0, layers, 1):
        layer = []
        for h in range(0, height, 1):
            row = []
            for w in range(0, width, 1):
                row.append(encoded[l * width * height + h * width + w])
            layer.append(row)
        decoded.append(layer)

    return decoded


def count_digits_in_layer(layer: [[int]], digit: int = 0) -> int:
    counter = 0
    for row in layer:
        for pixel in row:
            if pixel == digit:
                counter += 1
    return counter


def calculateCheckSum(image: [[[int]]]) -> int:
    checkSum = -1

    sorted_image = sorted(image, key=lambda x: count_digits_in_layer(x))

    oneDigits = count_digits_in_layer(sorted_image[0], 1)
    twoDigits = count_digits_in_layer(sorted_image[0], 2)
    print(f"Found {oneDigits} 1s and {twoDigits} 2s")
    checkSum = oneDigits * twoDigits

    return checkSum


def printLayer(layer: [[int]]):
    for row in layer:
        for pixel in row:
            print(pixel, end="")
        print("")
    print("")


# test = [0, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 2, 0, 0, 0, 0]
# decoded = decode(test, 2, 2)
# printLayer(decoded[0])
# printLayer(decoded[1])
# print(f"CheckSum: {calculateCheckSum(decoded)}")

received = list(map(lambda x: int(x), open(
    "./res/challenge8.txt").readline().strip()))

decoded = decode(received, 25, 6)
printLayer(decoded[0])
printLayer(decoded[1])
print(f"CheckSum: {calculateCheckSum(decoded)}")
