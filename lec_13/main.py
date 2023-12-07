import time
import threading
from multiprocessing import Process, Manager

def count_words(filename):
    word_freq = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

def count_words_multithread(filename, num_threads):
    word_freq = {}
    lock = threading.Lock()

    def process_chunk(chunk):
        local_freq = {}
        for line in chunk:
            words = line.strip().split()
            for word in words:
                local_freq[word] = local_freq.get(word, 0) + 1

        with lock:
            for word, count in local_freq.items():
                word_freq[word] = word_freq.get(word, 0) + count

    with open(filename, 'r') as file:
        lines = file.readlines()

    chunk_size = len(lines) // num_threads
    threads = []

    for i in range(num_threads):
        start = i * chunk_size
        end = start + chunk_size if i < num_threads - 1 else len(lines)
        chunk = lines[start:end]

        thread = threading.Thread(target=process_chunk, args=(chunk,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return word_freq

def count_words_multiprocess(filename, num_processes):
    word_freq = Manager().dict()

    def process_chunk(chunk, result_dict):
        local_freq = {}
        for line in chunk:
            words = line.strip().split()
            for word in words:
                local_freq[word] = local_freq.get(word, 0) + 1

        for word, count in local_freq.items():
            result_dict[word] = result_dict.get(word, 0) + count

    with open(filename, 'r') as file:
        lines = file.readlines()

    chunk_size = len(lines) // num_processes
    processes = []

    for i in range(num_processes):
        start = i * chunk_size
        end = start + chunk_size if i < num_processes - 1 else len(lines)
        chunk = lines[start:end]

        process = Process(target=process_chunk, args=(chunk, word_freq))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    return dict(word_freq)

def measure_execution_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

def main(filename, num_threads, num_processes):
    sequential_result, sequential_time = measure_execution_time(count_words, filename)

    multithreading_result, multithreading_time = measure_execution_time(count_words_multithread, filename, num_threads)

    multiprocessing_result, multiprocessing_time = measure_execution_time(count_words_multiprocess, filename, num_processes)

    print("\nSequential Result:")
    print(sequential_result)
    print(f"Sequential Execution Time: {sequential_time:.4f} seconds")

    print("\nMultithreading Result:")
    print(multithreading_result)
    print(f"Multithreading Execution Time: {multithreading_time:.4f} seconds")

    print("\nMultiprocessing Result:")
    print(multiprocessing_result)
    print(f"Multiprocessing Execution Time: {multiprocessing_time:.4f} seconds")

    multithreading_speedup = sequential_time / multithreading_time
    multiprocessing_speedup = sequential_time / multiprocessing_time

    print(f"\nMultithreading Speedup: {multithreading_speedup:.4f}x")
    print(f"Multiprocessing Speedup: {multiprocessing_speedup:.4f}x")

main("lec_13/text.txt", 4, 4)
