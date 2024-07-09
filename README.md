
# Highlight and Replace Words in Text Files

This repository contains a Python script that highlights and replaces specific words in a text file. The script reads a file, highlights occurrences of a given word, prompts the user to specify which occurrences to replace, and then updates the file accordingly.

## Table of Contents

- [Description](#description)
- [Usage](#usage)
- [Example](#example)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

## Description

The script `replace_word.py` provides the following functionalities:
- Reads a specified text file.
- Highlights all occurrences of a given word in each line, numbering each occurrence.
- Prompts the user to specify replacements in the format `lineNumber.wordNumber` or type `all` to replace all occurrences.
- Updates the file with the new word based on user input.

## Usage

1. **Run the script**:
    ```bash
    python replace_word.py
    ```

2. **Follow the prompts**:
    - Enter the file name.
    - Enter the word to be highlighted and replaced.
    - Enter the new word.
    - Specify replacements in the format `lineNumber.wordNumber` or type `all` to replace all occurrences.
