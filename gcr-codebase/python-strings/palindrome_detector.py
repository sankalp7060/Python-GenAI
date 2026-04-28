def find_palindromes(ids):
    result = []
    for i in ids:
        if i == i[::-1]:
            result.append(i)
    return result

print(find_palindromes(["ABA12", "1221", "XYZ"]))