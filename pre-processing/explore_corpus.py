import argparse

def read_lines_with_amharic(file_path, off_set, number_of_lines, line_brakes):
    """
    Reads a file line by line and yields lines that contain at least one Amharic character.
    
    Parameters:
    file_path (str): The path to the text file.
    
    Yields:
    str: Lines containing at least one Amharic character.
    """
    number_of_lines += off_set

    try:
        with open(file_path, 'r') as file:
            for i, line in enumerate(file):
                if i >= number_of_lines:
                    break
                if i >= off_set:
                    print(line)
                    for _ in range(line_brakes):
                        print()
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    parser = argparse.ArgumentParser(description='''
                                    Prints a given number of lines of sentences from an input file corpus
                                    with a given amount of line brakes. Default number_of_lines is 100 and line brakes is 3''')
    
    parser.add_argument('input_file', type=str, help='The path to the input file')
    parser.add_argument('--off_set', type=int, default=0, help='Starting line or off set')
    parser.add_argument('--number_of_lines', type=int, default=100, help='How many lines to print')
    parser.add_argument('--line_brakes', type=int, default=3, help='How many lines to print')
    
    args = parser.parse_args()

    input_file_path = args.input_file
    off_set = args.off_set
    number_of_lines = args.number_of_lines
    line_brakes = args.line_brakes

    read_lines_with_amharic(input_file_path, off_set, number_of_lines, line_brakes)


if __name__ == "__main__":
    main()
