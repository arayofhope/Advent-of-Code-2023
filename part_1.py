from pathlib import Path

def cube_game(input, max_red, max_green, max_blue):

    return "Hello World"

def main():
    p = Path(__file__).with_name('input.txt')

    file = open(p)

    print(cube_game(file, 12, 13, 14))

    file.close()    

main()