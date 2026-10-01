import random
import sys

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    return text.split()

def build_chains(words, chain_length=2):
    chains = {}
    for i in range(len(words) - chain_length):
        key = tuple(words[i:i + chain_length])
        next_word = words[i + chain_length]
        if key not in chains:
            chains[key] = []
        chains[key].append(next_word)
    return chains

def generate_text(chains, length, chain_length=2):
    starts = [k for k in chains.keys() if k[0][0].isupper()]
    if not starts:
        starts = list(chains.keys())
    
    current = random.choice(starts)
    result = list(current)
    
    while len(result) < length:
        if current in chains:
            next_word = random.choice(chains[current])
            result.append(next_word)
            current = tuple(list(current[1:]) + [next_word])
        else:
            break
    
    return ' '.join(result)

if __name__ == '__main__':
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print("Использование: python markov.py <имя_файла> <длина_текста> [длина_цепочки]")
        print("По умолчанию длина цепочки = 2")
        sys.exit(1)
    
    filename = sys.argv[1]
    length = int(sys.argv[2])
    
    # Если передан третий аргумент, используем его как длину цепочки
    if len(sys.argv) == 4:
        chain_length = int(sys.argv[3])
    else:
        chain_length = 2
    
    words = read_file(filename)
    chains = build_chains(words, chain_length=chain_length)
    text = generate_text(chains, length, chain_length=chain_length)
    print(text)
