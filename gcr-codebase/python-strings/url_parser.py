def parse_url(url):
    parts = url.split("//")
    protocol = parts[0] + "//"
    rest = parts[1].split("/", 1)
    base = protocol + rest[0]
    path = "/" + rest[1] if len(rest) > 1 else ""
    return base, path

base, path = parse_url("https://example.com/products/item1")
print("Base URL:", base)
print("Path:", path)