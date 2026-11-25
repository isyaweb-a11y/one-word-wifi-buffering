"""One Word for Your Wi-Fi.

A single word offered as the funniest and most accurate description of
my Wi-Fi — the network that has been buffering since 2019 and shows no
sign of ever finishing. One word, no spaces, no punctuation.
Gate: 1-20 characters.
"""

ENTRY = "BufferingSince2019"


def check_wifi_word(text: str) -> str:
    """A Wi-Fi word must be one word that names the eternal buffering."""
    assert text == "BufferingSince2019", "entry must be the one chosen word"
    assert text.isalnum(), "entry must be a single word with no punctuation"
    return text


def main() -> None:
    text = check_wifi_word(" ".join(ENTRY.split()))
    assert 1 <= len(text) <= 20, f"entry is {len(text)} chars, gate is 1-20"
    assert " " not in text, "entry must be a single word"
    assert "\n" not in text, "entry must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
