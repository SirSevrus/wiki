from colorama import Fore, init

init(autoreset=True)

def highlight_word(line, word):
    highlighted_line = ""
    i = 0
    word_count = 1
    while i < len(line):
        if line[i:i+len(word)] == word:
            highlighted_line += f"{Fore.RED}{word_count}:{word}{Fore.RESET}"
            i += len(word)
            word_count += 1
        else:
            highlighted_line += line[i]
            i += 1
    return highlighted_line, word_count - 1

def replace_word_in_line(line, word, newWord, word_index):
    parts = line.split(word, word_index + 1)
    if len(parts) > word_index:
        return word.join(parts[:word_index]) + newWord + word.join(parts[word_index + 1:])
    return line

def replaceWord(fileName, word, newWord):
    try:
        with open(fileName, 'r') as file:
            data = file.readlines()
        
        occurrences = []
        for count, line in enumerate(data, 1):
            if word in line:
                highlighted_line, word_count = highlight_word(line, word)
                print(f'Line No : {count}')
                print(highlighted_line)
                for i in range(1, word_count + 1):
                    occurrences.append((count, i))
        
        to_replace = input("Specify replacements (format: lineNumber.wordNumber) or type 'all' to replace all: ").strip().lower()
        
        lines_to_replace = []
        if to_replace == 'all':
            lines_to_replace = occurrences
        else:
            entries = to_replace.split()
            for entry in entries:
                line_num, word_num = map(int, entry.split('.'))
                lines_to_replace.append((line_num, word_num))
        
        with open(fileName, 'w') as file:
            for count, line in enumerate(data, 1):
                words_in_line = line.count(word)
                for line_num, word_num in lines_to_replace:
                    if count == line_num and words_in_line >= word_num:
                        line = replace_word_in_line(line, word, newWord, word_num - 1)
                file.write(line)
                
    except FileNotFoundError:
        print('[ERROR] File Not Found :', fileName)

replaceWord('test.txt', 'i', 'Is')
