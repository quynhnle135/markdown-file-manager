# Markdown File Manager

A versatile Python Command Line Interface (CLI) tool for managing Markdown files. This application allows for file validation, creation, reading, and automated generation of Markdown files based on customizable date ranges.

## Technical Stack:
- Python: Primary programming language.
- Argparse: For parsing command-line arguments.
- Pytest: For writing and executing tests.
- Python Standard Library Modules (os, datetime): For OS interactions and date/time management.
- File I/O Operations: Core functionality for handling files.

## Features:

- Path Validation: Check if a specified path exists in the system.
- Markdown Validation: Verify whether a specified file is a Markdown (.md) file.
- Markdown Creation: Create a new Markdown file in a specified directory.
- File Reading: Read and display the contents of a Markdown file.
- File Counting: Count the number of Markdown files in a specified directory.
- File Generation: Automatically generate Markdown files for the next 7 days.
- Customized File Generation: Generate Markdown files for a specified number of days in a given directory.

## Installation:

```commandline
git clone https://github.com/quynhnle135/markdown-file-manager.git

cd md-file-manager
```

## Usage:

For program's instruction and commandlines

```commandline
python main.py -h
```

What it looks like after running the command above

```commandline
Welcome to MD File Manager program.

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Check if the specified path exists in the system
  -m VALIDATEMD, --validatemd VALIDATEMD
                        Verify the specified file is a Markdown (.md) file
  -cr CREATEMD, --createmd CREATEMD
                        Create a new Markdown (.md) file in the specified directory. Use '.' to indicate the current directory.
  -rd READMD, --readmd READMD
                        Read and display the contents of a specified file.
  -co COUNT, --count COUNT
                        Count the number of Markdown (.md) files in the specified directory. Use '.' to count files in the current directory.
  -g GENERATE, --generate GENERATE
                        Generate 7 Markdown (.md) files for the next 7 days, starting from tomorrow.
  -gc GENERATECUSTOMIZE, --generatecustomize GENERATECUSTOMIZE
                        Directory to generate Markdown files.
  -d DAYS, --days DAYS  Number of days to generate files for (default: 7).
  -uf UPDATEMD, --updatemd UPDATEMD
                        Updated content of the specified Markdown file.
  -nc NEWCONTENT, --newcontent NEWCONTENT
                        New content for updating.
  -u UPDATE, --update UPDATE
                        Updated contents of Markdown files in the specified directory.
```

## Examples:

#### Check if path exists

```commandline
(venv) quinnle@Quinns-MBP md-file-manager % python main.py -p /Users/quinnle/PycharmProjects/md-file-manager

>>> The path /Users/quinnle/PycharmProjects/md-file-manager exists.
```

### Validate if a file is a Markdown file
```commandline
(venv) quinnle@Quinns-MBP md-file-manager % python main.py -m /Users/quinnle/PycharmProjects/md-file-manager/draft.md                                                     

>>> /Users/quinnle/PycharmProjects/md-file-manager/draft.md is a valid Markdonw file
```

#### Generate 7 .md files in the given directory
```commandline
(venv) quinnle@Quinns-MBP md-file-manager % python main.py -g /Users/quinnle/PycharmProjects/md-file-manager/md_files

>>> 7 Markdown files are created in /Users/quinnle/PycharmProjects/md-file-manager/md_files directory.
```

