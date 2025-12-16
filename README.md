# Password Hash Analyzer (Educational)

This project demonstrates how offline password hash matching works using
dictionary-based techniques. It is intended strictly for educational and
defensive cybersecurity learning purposes.

The program takes a list of known password hashes and compares them against
hashed values of common passwords from a wordlist. the contained word list is
specifically the Hashmob wordlist micro version:[https://hashmob.net/resources/hashmob](link)

## Features
- Supports SHA-256 hashing
- Fast hash lookup using Python sets
- Clear console output of matched hashes
- Uses synthetic, non-real test data

## How It Works
1. Load hashes from a file
2. Hash each word in the wordlist
3. Compare generated hashes to the target list
4. Report successful matches

## Usage
```bash
python cracker.py

