import sys


path_to_file = 'books/frankenstein.txt'
report_begin_message = "--- Begin report of {} ---"
report_words_count_message = "{} words found in the document\n"
report_char_count_message = "The '{0}' character was found {1} times"
report_end_message = "--- End report ---"


def words_count(text: str) -> int:
    return len(text.split())


def character_count(text: str) -> dict:
    result = dict()
    for i in text:
        char = i.lower()
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1
    return result


def print_report(filename: str, text: str):
    print(report_begin_message.format(filename))
    print(report_words_count_message.format(words_count(text)))

    char_pairs = [(k, v) for k, v in character_count(text).items() if k.isalpha()]
    char_pairs.sort(key=lambda x: x[1], reverse=True)
    for pair in char_pairs:
        print(report_char_count_message.format(pair[0], pair[1]))

    print(report_end_message)


if __name__ == "__main__":
    with open(path_to_file) as f:
        file_contents = f.read()
        print_report(path_to_file, file_contents)
