def count_unsigned(logs):
    count = 0
    for log in logs:
        if not log.endswith("--signed"):
            count += 1
    return count

print("Unsigned Entries:", count_unsigned(["Event A --signed", "Event B", "Event C --signed"]))