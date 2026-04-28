def format_filename(filename):
    return filename.strip().replace(" ", "_").lower()

print(format_filename("My Report FINAL .txt"))