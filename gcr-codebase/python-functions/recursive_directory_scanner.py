import os

def scan_directory(path):
    files = []
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            files.extend(scan_directory(full_path))
        else:
            files.append(full_path)
    return files
