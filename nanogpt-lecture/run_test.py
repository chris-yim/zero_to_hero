if __name__ == "__main__":
    with open('input.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    print("length of dataset in characters: ", len(text))

    print(text[:1000])

    chars = sorted(list(set(text)))
