import hashlib


def load_hashes(path):
    #"""Load hashes from file into a set."""
    with open(path, "r") as file:
        return {line.strip() for line in file if line.strip()}


def hash_word(word):
   # """Return SHA-256 hash of a word."""
    return hashlib.sha256(word.encode()).hexdigest()


def crack_hashes(hashes, wordlist_path):
    #"""Match wordlist entries against known hashes."""
    results = {}

    with open(wordlist_path, "r") as file:
        for word in file:
            word = word.strip()
            hashed = hash_word(word)

            if hashed in hashes:
                results[hashed] = word
                print(f"[+] Match found: {hashed} -> {word}")

    return results


def main():
    hashes = load_hashes("hashes.txt")
    results = crack_hashes(hashes, "wordlist.txt")

    print("\nSummary:")
    for h, p in results.items():
        print(f"{h} : {p}")


if __name__ == "__main__":
    main()
