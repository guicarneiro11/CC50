from cs50 import get_string


def main():
    text = get_string("Text: ")
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    L = (letters / words) * 100
    S = (sentences / words) * 100

    index = round(0.0588 * L - 0.296 * S - 15.8)

    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


def count_letters(text):
    """Conta o número de letras no texto."""
    return sum(c.isalpha() for c in text)


def count_words(text):
    """Conta o número de palavras no texto."""
    return len(text.split())


def count_sentences(text):
    """Conta o número de sentenças no texto."""
    return text.count(".") + text.count("!") + text.count("?")


if __name__ == "__main__":
    main()
