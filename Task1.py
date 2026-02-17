try:
    with open("sample.txt","tr") as fh:
        data = fh.read()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")
else:
    print(data)