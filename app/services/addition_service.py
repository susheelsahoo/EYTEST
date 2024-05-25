from multiprocessing import Pool

def add_pair(pair):
    return sum(pair)

def process_addition(numbers):
    with Pool() as pool:
        result = pool.map(add_pair, numbers)
    return result

