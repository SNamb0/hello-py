import time
import sys

def print_slowly(text: str, delay: float = 1.0):
    """Prints a string character by character with a delay between each."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def main():
    print_slowly("Hello, World!\n", 1.0)

if __name__ == "__main__":
    main()
