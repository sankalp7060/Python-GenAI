class CaseInsensitiveDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)
    
    def __getitem__(self, key):
        return super().__getitem__(key.lower())

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

print(headers["content-type"] == headers["Content-Type"])