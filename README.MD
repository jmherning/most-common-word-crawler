# Most Common Word Web Page Scraper

This CLI tool will scrape text from a web page and then return a list of words and the number of times each word is found.
Currenlty only designed to work with the history section of https://en.wikipedia.org/wiki/Microsoft.

## Usage Examples

### Default
This will return the 10 most common words found.
Will not exclude any words by default.

```
python most_common_word.py
```

### Set number of words to return

```
python most_common_word.py --number 5
```

```
python most_common_word.py -n 5
```

### Exclude the words 'the' and 'Microsoft' from list

```
python most_common_word.py the Microsoft
```

### Exclude the words 'the' and 'Microsoft' and limit output to 15

```
python most_common_word.py the Microsoft -n 15
```

```
python most_common_word.py -n 15 the Microsoft
```
