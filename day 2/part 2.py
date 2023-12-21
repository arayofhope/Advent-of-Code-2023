from pathlib import Path

def cube_game(input):
    answer = 0

    for line in input:

        game, cubes = line.strip().split(": ")
        
        game = game.split(" ")[1]

        cubes = [[c.split(" ") for c in d.split(", ")] for d in cubes.split("; ")]

        max_blue = 0
        max_red = 0
        max_green = 0

        ## our cube object now looks something like:
        ## cube = [[['2', 'blue'], ['4', 'red'], ['7', 'green']], 
        # [['17', 'red'], ['3', 'blue'], ['2', 'green']]]
        for draws in cubes:
            for draw in draws:
                number = int(draw[0])
                color = draw[1]

                match color:
                    case 'blue':
                        if int(number) > max_blue:
                            max_blue = number
                    case 'red':
                        if int(number) > max_red:
                            max_red = number
                    case 'green':
                        if int(number) > max_green:
                            max_green = number  
          
        power = max_blue * max_red * max_green

        answer += power
        print(game)
        print(cubes)

    return answer

def main():
    p = Path(__file__).with_name('input.txt')

    file = open(p)

    print(cube_game(file))

    file.close()    

main()