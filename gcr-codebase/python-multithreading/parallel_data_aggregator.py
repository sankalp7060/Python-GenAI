from multiprocessing import Pool

def process_file(file):
    return f"Processed {file}"

files = ["sales.csv", "marketing.csv", "finance.csv"]

with Pool() as p:
    p.map(process_file, files)

print("All data merged successfully.")