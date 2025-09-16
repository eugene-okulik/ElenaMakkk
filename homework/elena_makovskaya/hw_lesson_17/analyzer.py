# вызов в терминале чтобы получить все совпадения:
# python3 analyzer.py /Users/elenamakovskaya/ElenaMakkk/homework/eugene_okulik/data/logs --text WARN

# вызов в терминале чтобы получить только первую строку:
# python3 analyzer.py /Users/elenamakovskaya/ElenaMakkk/homework/eugene_okulik/data/logs --text WARN --full no

import os
import argparse
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)


def get_files_from_directory(folder_path):
    files = []
    for entry in os.listdir(folder_path):
        file_path = os.path.join(folder_path, entry)
        if os.path.isfile(file_path):
            files.append(file_path)
    return files


def find_text_in_line(line, search_text):
    words = line.split()
    search_text_lower = search_text.lower()
    for i, word in enumerate(words):
        if search_text_lower in word.lower():
            return i, words
    return None, None


def get_context_snippet(words, index, count_words=5):
    start = max(0, index - count_words)
    end = min(len(words), index + count_words + 1)
    snippet_words = words[start:end]
    return snippet_words


def highlight_search_text(words, search_text):
    search_text_lower = search_text.lower()
    highlighted_words = []
    for word in words:
        word_lower = word.lower()
        if search_text_lower in word_lower:
            highlighted_word = Fore.RED + Style.NORMAL + word + Style.RESET_ALL
            highlighted_words.append(highlighted_word)
        else:
            highlighted_words.append(word)
    return " ".join(highlighted_words)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('folder_path', help='Путь к папке с логами')
    parser.add_argument('--text', help='Текст для поиска')
    parser.add_argument("--full", help="Укажите 'no' если хотите получить только первое совпадение")

    args = parser.parse_args()

    folder_path = args.folder_path
    search_text = args.text
    full_snippets = args.full
    files = get_files_from_directory(folder_path)

    for file_path in files:
        with open(file_path) as f:
            for line_number, line in enumerate(f, start=1):
                index, words = find_text_in_line(line, search_text)
                if index is not None:
                    snippet_words = get_context_snippet(words, index, count_words=5)
                    highlighted_snippet = highlight_search_text(snippet_words, search_text)
                    print(f"Файл: {os.path.basename(file_path)}, Строка: {line_number}")
                    print(f"Искомый фрагмент: {highlighted_snippet}\n")
                    if full_snippets == 'no':
                        return


main()
