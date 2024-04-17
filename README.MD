# Microsoft Wikipedia Page History Section Word Counter

Python command-line tool for counting the occurrence of words in the history section of the [Microsoft Wikipedia page](https://en.wikipedia.org/wiki/Microsoft).

## Setup

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Open a terminal or command prompt.
2. Navigate to the project root directory
3. Run the CLI script with the following command:

```bash
python most_common_word.py
```

### Optional arguments

- `-h`, `--help`: Show the help message and exit.
- `-n`, `--num_words`: Number of words to count (default is 10).
- `-e`, `--exclude`: List of words to exclude from counting.

### Customize number of words output

You can customize the number of words to show in the ouput using the `-n` or `--num_words` optinal argument.

Example below will only return 5 words along with thier count:

```bash
python most_common_word.py -n 5
```

### Exclude words in the output

You can specify words to exclude from the output using the `-e` or `--exclude` optinal argument.

Example below will exclude the words **the**, **in**, and **of** from the output:

```text
python most_common_word.py -e the in of
```
