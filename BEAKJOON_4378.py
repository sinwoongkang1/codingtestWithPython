# import sys
# error_input = list(sys.stdin.readline().strip())
#
# stack = {
#     "1": "`", "2": "1", "3": "2", "4": "3", "5": "4", "6": "5", "7": "6", "8": "7", "9": "8", "0": "9", "-": "0", "=": "-",
#     "W": "Q", "E": "W", "R": "E", "T": "R", "Y": "T", "U": "Y", "I": "U", "O": "I", "P": "O", "[": "P", "]": "[", "\\": "]",
#     "S": "A", "D": "S", "F": "D", "G": "F", "H": "G", "J": "H", "K": "J", "L": "K", ";": "L", "'": ";",
#     "X": "Z", "C": "X", "V": "C", "B": "V", "N": "B", "M": "N", ",": "M", ".":",", "/": ".", " ": " "
# }
#
# for i in range(len(error_input)):
#     if error_input[i] in stack:
#         a = stack.get(error_input[i])
#         error_input[i] = a
#
# print(*error_input, sep="")

def replace_method(error_str):
    correct_str = ""

    stack = {
        "1": "`", "2": "1", "3": "2", "4": "3", "5": "4", "6": "5", "7": "6", "8": "7", "9": "8", "0": "9", "-": "0", "=": "-",
        "w": "q", "e": "w", "r": "e", "t": "r", "y": "t", "u": "y", "i": "u", "o": "i", "p": "o", "[": "p", "]": "[", "\\": "]",
        "s": "a", "d": "s", "f": "d", "g": "f", "h": "g", "j": "h", "k": "j", "l": "k", ";": "l", "'": ";",
        "x": "z", "c": "x", "v": "c", "b": "v", "n": "b", "m": "n", ",": "m", ".":",", "/": ".", " ": " "
    }

    return stack[error_str.lower()].upper()


if __name__ == "__main__":
    while True:
        try:
            for type_word in input():
                print(replace_method(type_word), end='')
            print()
        except:
            break