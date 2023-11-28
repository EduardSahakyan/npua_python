import random
import time

def create_file(filename):
    with open(filename, 'w') as file:
        for _ in range(100):
            line = ' '.join(str(random.randint(1, 100)) for _ in range(20))
            file.write(line + '\n')

def line_to_int_array(line):
    return list(map(int, line.split()))

def filter_numbers(array):
    return list(filter(lambda x: x > 40, array))

def write_to_file(filename, data):
    with open(filename, 'w') as file:
        for line in data:
            line_str = ' '.join(map(str, line))
            file.write(line_str + '\n')

def read_file_as_generator(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line_to_int_array(line)

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time:.6f} seconds")
        return result
    return wrapper

@measure_execution_time
def main():
    create_file('data.txt')
    with open('data.txt', 'r') as file:
        lines = [line_to_int_array(line) for line in file]
        print("Before")
        for line in lines:
            print(line)
    filtered_data = [filter_numbers(line) for line in lines]
    write_to_file('filtered_data.txt', filtered_data)
    generator = read_file_as_generator('filtered_data.txt')
    print("=========================================================")
    print("After")
    for line in generator:
        print(line)

main()
