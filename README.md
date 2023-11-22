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
- Markdown File Generation: Automatically generate Markdown files with specified number of days and templates.
- File Reading: Read and display the contents of a Markdown file.
- File Counting: Count the number of Markdown files in a specified directory.


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
MD File Manager

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Check if the specified path exists in the system
  -f FILE, --file FILE  Verify the specified file is a Markdown (.md) file
  -r READ, --read READ  Read and display the contents of a specified file.
  -co COUNT, --count COUNT
                        Count the number of Markdown (.md) files in the specified directory. Use '.' to count files in the current directory.
  -g GENERATE, --generate GENERATE
                        Generate multiple Markdown files. If specified is not entered, default amount of files will be created is 7.
  -a ADD, --add ADD     Add new content to existing files.
  -u UPDATE, --update UPDATE
                        Updated contents of Markdown files in the specified directory.
  -d DAYS, --days DAYS  Number of days to generate files for (default: 7).
  -ct CONTENT, --content CONTENT
                        New content for updating.
  -cj, --coding         Generate file with Coding Journal template
  -dp, --practice       Generate file with Daily Practice template
```


