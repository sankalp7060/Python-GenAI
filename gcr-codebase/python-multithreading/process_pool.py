from multiprocessing import Pool

def process_file(file):
    return f"Processed {file}"

files = ["file1", "file2", "file3"]

with Pool() as p:
    results = p.map(process_file, files)

for r in results:
    print(r)