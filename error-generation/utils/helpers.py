import argparse
import types
import time
import csv
import os

def convert_to_int(string):
    try:
        return int(string)
    except ValueError:
        print("Error: Cannot convert to an integer.")
        return None
    

def read_file_and_yield_line(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file_and_yield_line_with_offset(off_set):

    def read_file_and_yield_line(file_path):
        try:
            with open(file_path, 'r') as file:
                for i, line in enumerate(file):
                    if i >= off_set:
                        yield line.strip()
                        print(f"done line {i}")
        except FileNotFoundError:
            print(f"The file at {file_path} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    return read_file_and_yield_line


def write_lines_to_file(lines, output_file_path):
    try:
        with open(output_file_path, 'a') as file:
            for line in lines:
                if line is None or line == "":
                    pass
                else:
                    file.write(line + '\n')
    except FileNotFoundError:
        with open(output_file_path, 'w') as file:
            for line in lines:
                file.write(line + '\n')
    except Exception as e:
        print(f"An error occurred: {e}")


def write_lines_to_csv_file(headers):
    def inner(lines, output_file_path):
        file_exists = os.path.isfile(output_file_path)

        try:
            with open(output_file_path, mode='a', newline='') as file:
                writer = csv.writer(file)

                if not file_exists and headers:
                    writer.writerow(headers)

                for line in lines:
                    if line is not None:
                        writer.writerow(line)

        except Exception as e:
            print(f"An error occurred: {e}")

    return inner
    

def transformer(lines, transformer_func, progress_report=False):
    for i, line in enumerate(lines, start=1):
        if progress_report:
            print(i)
        yield transformer_func(line)

def transformer_to_multi_lines(lines, transformer_func):
    for line in lines:
        transformer_func_result = transformer_func(line)
        # if the transformer fun return iterable unpack and yield each
        if isinstance(transformer_func_result, types.GeneratorType):
            for res in transformer_func_result:
                yield res
        # else if the transformer return non iterable just yield the result
        else:
            yield transformer_func_result

def arg_parser(description, input_dict):
    parser = argparse.ArgumentParser(description)
    
    for key in input_dict:
        flag = key if input_dict[key].get('required', False) else f"--{key}"
        parser.add_argument(flag, type=input_dict[key].get('type', str), help=input_dict[key].get('help', ""),
                            default=input_dict[key].get('default', None))
            
    return parser.parse_args()
    

standard_input_args = {
    "input_file": {
        "required": True,
        "type": str,
        "help": "The path to the input file"
    },
}

standard_input_output_args = {
    "input_file": standard_input_args.get("input_file", None),
    "output_file": {
        "required": True,
        "type": str,
        "help": "The path to the output file"
    },
}

input_output_with_offset_args = {
    "input_file": standard_input_args.get("input_file", None),
    "output_file": standard_input_output_args.get("output_file", None),
    "off_set": {
        "required": False,
        "type": int,
        "help": "Offset value, or starting line of the input file",
        "default": 0
    },
}

def with_info(func):
    evalFn = lambda f: f()
    
    @evalFn
    def wrap(*args, **kwargs): 
        start = time.time() 
        print(f"Started running {func.__name__} at :", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start)))
        result = func(*args, **kwargs) 
        end = time.time() 
        print(f"Finished running {func.__name__}  at :", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start)))
        print(f"{func.__name__} took :", end-start, "sec to finish")
        return result
    
    return wrap

    
        
    