from pathlib import Path

def calculate_sum(input_file):

    answer = 0

    file_content = input_file.readlines()

    first_dig = None

    second_dig = None

    for line in file_content:
        for character in line:
            if character.isdigit():
                if first_dig == None:
                    first_dig = character
                second_dig = character

        calibration_value = first_dig + second_dig

        answer += int(calibration_value)

        first_dig = None
        second_dig = None

    return answer

def main():
    p = Path(__file__).with_name('input.txt')

    file = open(p)

    print(calculate_sum(file))

    file.close()

main()