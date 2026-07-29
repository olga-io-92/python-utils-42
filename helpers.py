def optimized_function(data):
    result = []
    data_set = set(data)
    for item in data_set:
        result.append(item * 2)
    return result

def read_large_file(file_path):
    with open(file_path, 'r') as file:
        chunk_size = 1024
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

def process_file(file_path):
    data = ''
    for chunk in read_large_file(file_path):
        data += chunk
    return optimized_function(data.split())