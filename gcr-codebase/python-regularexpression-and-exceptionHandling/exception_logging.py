try:
    int("abc")
except Exception as e:
    with open("error.log", "a") as f:
        f.write(f"{type(e).__name__}: {e}\n")