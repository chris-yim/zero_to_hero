from loguru import logger

if __name__ == '__main__':
    words = open('names.txt', 'r').read().splitlines()

    logger.info(f"Number of names: {len(words)}")
    logger.info(f"Shortest name: {min(len(word) for word in words)}")
    logger.info(f"Longest name: {max(len(word) for word in words)}")

    b = {}
    for w in words:
        chs = ['<S>'] + list(w) + ['<E>']
        for ch1, ch2 in zip(chs, chs[1:]):
            bigram = (ch1, ch2)
            b[bigram] = b.get(bigram, 0) + 1
    print(sorted(b.items(), key=lambda x: x[1], reverse=True))

    import torch
    a = torch.zeros((3,5), dtype=torch.int32)
    a[1,3] = 1
    print(a)