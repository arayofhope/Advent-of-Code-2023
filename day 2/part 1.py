from pathlib import Path

def cube_game(input, max_red, max_green, max_blue):
    answer = 0

    for line in input:

        is_valid = True  

        game, cubes = line.strip().split(": ")
        
        game = game.split(" ")[1]

        cubes = [[c.split(" ") for c in d.split(", ")] for d in cubes.split("; ")]

        ## our cube object now looks something like:
        ## cube = [[['2', 'blue'], ['4', 'red'], ['7', 'green']], 
        # [['17', 'red'], ['3', 'blue'], ['2', 'green']]]
        for draws in cubes:
            for draw in draws:
                number = int(draw[0])
                color = draw[1]

                match color:
                    case 'blue':
                        if number > max_blue:
                            is_valid = False
                    case 'red':
                        if number > max_red:
                            is_valid = False
                    case 'green':
                        if number > max_green:
                            is_valid = False  
                if not is_valid:
                    break
        
        if is_valid:
            answer += int(game)

        print(game)
        print(cubes)

    return answer

def main():
    p = Path(__file__).with_name('input.txt')

    file = open(p)

    print(cube_game(file, 12, 13, 14))

    file.close()    

main()