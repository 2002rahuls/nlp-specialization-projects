import argparse
from autocorrect import load_dictionary, get_corrections

def main():
    parser = argparse.ArgumentParser(description="Simple Autocorrect CLI")
    parser.add_argument('--word', type=str, required=True, help="Misspelled word")
    args = parser.parse_args()

    dictionary = load_dictionary()
    suggestions = get_corrections(args.word, dictionary)

    print("Suggestions:")
    for i, suggestion in enumerate(suggestions, 1):
        print(f"{i}. {suggestion}")

if __name__ == "__main__":
    main()
