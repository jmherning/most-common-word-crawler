import argparse
import requests
from bs4 import BeautifulSoup
import pandas as pd
from collections import Counter
from typing import List


def scrape_history_section(url: str) -> str:
    """
    Scrapes the history section of a Wikipedia page.

    Args:
        url (str): The URL of the Wikipedia page.

    Returns:
        str: The text content of the history section.
    """

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any HTTP error status
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the starting point (h2 tag with "History")
        start_tag = soup.find('span', {'id': 'History'}).parent

        # Find the end point (next h2 tag)
        end_tag = start_tag.find_next('h2')

        # Extract text from all p tags between start and end tags
        text = ''
        current_tag = start_tag.find_next_sibling()
        while current_tag and current_tag != end_tag:
            if current_tag.name == 'p':
                text += current_tag.get_text() + ' '
            current_tag = current_tag.next_sibling

        return text

    except requests.RequestException as e:
        print(f"Error occurred while fetching the page: {e}")

        return ''


def count_words(text: str, num_words: int = 10, exclude: List[str] = []) -> pd.DataFrame:
    """
    Counts the occurrences of words in the given text.

    Args:
        text (str): The text in which words will be counted.
        num_words (int, optional): Number of top words to count. Defaults to 10.
        exclude (List[str], optional): List of words to exclude from counting. Defaults to [].

    Returns:
        pandas.DataFrame: DataFrame containing the counted words and their occurrences.
    """

    words = text.split()
    words = [word.lower() for word in words if word.isalnum() and word.lower() not in exclude]
    word_count = Counter(words)
    df = pd.DataFrame.from_dict(word_count, orient='index', columns=['# of occurrences']) 
    df = df.sort_values(by='# of occurrences', ascending=False)

    return df.head(num_words)


def parse_arguments():
    """
    Parses command line arguments.

    Returns:
        argparse.Namespace: The parsed arguments.
    """

    parser = argparse.ArgumentParser(description='Word count of the history section of a Wikipedia page')
    parser.add_argument('-n', '--num_words', type=int, default=10, help='Number of words to count (default is 10)')
    parser.add_argument('-e', '--exclude', nargs='+', default=[], help='List of words to exclude')
    args = parser.parse_args()

    # Validate the num_words argument
    if args.num_words <= 0:
        parser.error("The number of words to count (-n) must be an int greater than zero.")

    return args


def main():
    url = 'https://en.wikipedia.org/wiki/Microsoft'
    args = parse_arguments()
    text = scrape_history_section(url)
    result = count_words(text, args.num_words, args.exclude)

    print(result)

if __name__ == "__main__":
    main()










# import argparse
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# from collections import Counter
# from typing import List




# def scrape_history_section() -> str:
#     """
#     Scrapes the history section of the Microsoft Wikipedia page.

#     Returns:
#         str: The text content of the history section.
#     """
#     url = 'https://en.wikipedia.org/wiki/Microsoft'
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Raise an exception for any HTTP error status
#         soup = BeautifulSoup(response.text, 'html.parser')

#         # Find the starting point (h2 tag with "History")
#         start_tag = soup.find('span', {'id': 'History'}).parent

#         # Find the end point (next h2 tag)
#         end_tag = start_tag.find_next('h2')

#         # Extract text from all p tags between start and end tags
#         text = ''
#         current_tag = start_tag.find_next_sibling()
#         while current_tag and current_tag != end_tag:
#             if current_tag.name == 'p':
#                 text += current_tag.get_text() + ' '
#             current_tag = current_tag.next_sibling

#         return text
#     except requests.RequestException as e:
#         print(f"Error occurred while fetching the page: {e}")
#         return ''





# def word_count(text: str, num_words: int = 10, exclude: List[str] = []) -> pd.DataFrame:
#     """
#     Counts the occurrences of words in the given text.

#     Args:
#         text (str): The text in which words will be counted.
#         num_words (int, optional): Number of top words to count. Defaults to 10.
#         exclude (List[str], optional): List of words to exclude from counting. Defaults to [].

#     Returns:
#         pandas.DataFrame: DataFrame containing the counted words and their occurrences.
#     """

#     words = text.split()
#     words = [word.lower() for word in words if word.isalnum() and word.lower() not in exclude]
#     word_count = Counter(words)
#     df = pd.DataFrame.from_dict(word_count, orient='index', columns=['Count'])
#     df = df.sort_values(by='Count', ascending=False)
#     return df.head(num_words)


# def main():

#     parser = argparse.ArgumentParser(description='Word count of the history section of the Microsoft Wikipedia page')
#     parser.add_argument('-n', '--num_words', type=int, default=10, help='Number of words to count (default is 10)')
#     parser.add_argument('-e', '--exclude', nargs='+', default=[], help='List of words to exclude')
#     args = parser.parse_args()

#     text = scrape_history_section()
#     result = word_count(text, args.num_words, args.exclude)
#     print(result)


# if __name__ == "__main__":
#     main()






# import argparse
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# from collections import Counter
# from typing import List


# def scrape_website(url: str) -> str:
#     """
#     Scrapes the given website and extracts text from paragraphs.

#     Args:
#         url (str): The URL of the website to scrape.

#     Returns:
#         str: The concatenated text from all paragraphs on the website.
#     """

#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     text = ' '.join([p.get_text() for p in soup.find_all('p')])

#     return text


# def word_count(text: str, num_words: int =10, exclude: List[str] = []):
#     """
#     Counts the occurrences of words in the given text.

#     Args:
#         text (str): The text in which words will be counted.
#         num_words (int, optional): Number of top words to count. Defaults to 10.
#         exclude (list, optional): List of words to exclude from counting. Defaults to [].

#     Returns:
#         pandas.DataFrame: DataFrame containing the counted words and their occurrences.
#     """

#     words = text.split()
#     words = [word.lower() for word in words if word.isalnum() and word.lower() not in exclude]
#     word_count = Counter(words)
#     df = pd.DataFrame.from_dict(word_count, orient='index', columns=['Count'])
#     df = df.sort_values(by='Count', ascending=False)

#     return df.head(num_words)


# def main():
#     parser = argparse.ArgumentParser(description='Word count of a website')
#     parser.add_argument('url', type=str, help='URL of the website')
#     parser.add_argument('-n', '--num_words', type=int, default=10, help='Number of words to count (default is 10)')
#     parser.add_argument('-e', '--exclude', nargs='+', default=[], help='List of words to exclude')
#     args = parser.parse_args()

#     text = scrape_website(args.url)
#     result = word_count(text, args.num_words, args.exclude)
#     print(result)


# if __name__ == "__main__":
#     main()













# import argparse
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# from collections import Counter
# import re

# def get_text_from_url(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     # Find all text elements on the page
#     text_elements = soup.find_all(text=True)
#     # Filter out script and style elements
#     visible_text = filter(lambda elem: elem.parent.name not in ['script', 'style'], text_elements)
#     return ' '.join(visible_text)

# def count_words(text, exclude_words=None):
#     # Convert text to lowercase and split into words
#     words = re.findall(r'\b\w+\b', text.lower())
#     # Exclude words if specified
#     if exclude_words:
#         words = [word for word in words if word not in exclude_words]
#     # Count the occurrence of each word
#     word_counts = Counter(words)
#     # Convert to DataFrame
#     word_df = pd.DataFrame(word_counts.items(), columns=['Word', 'Count'])
#     # Sort by count in descending order
#     word_df = word_df.sort_values(by='Count', ascending=False)
#     return word_df

# def main():
#     parser = argparse.ArgumentParser(description="Count words on a website")
#     parser.add_argument("url", type=str, help="URL of the website to scrape")
#     parser.add_argument("--top", type=int, default=10, help="Number of top words to display (default: 10)")
#     parser.add_argument("--exclude", nargs="+", help="List of words to exclude from the count")
#     args = parser.parse_args()

#     # Get text from URL
#     text = get_text_from_url(args.url)

#     # Count words
#     word_df = count_words(text, args.exclude)

#     # Display top words
#     print(word_df.head(args.top))

# if __name__ == "__main__":
#     main()















# import click
# from src.parse_html import get_page_word_count, get_page_content


# @click.command()
# @click.option("--number", "-n", default=10, help="Number of words to return.")
# @click.argument("exclude", nargs=-1, default=None, type=str)
# def cli(number, exclude):
#     """
#     Returns a count of most common word in the history section of https://en.wikipedia.org/wiki/Microsoft.

#     Word count is returned in descending order.


#     === Example Use ===

#     Default:

#     > python most_common_word.py

#     Set number of words to return:

#     > python most_common_word.py --number 5

#     > python most_common_word.py -n 5

#     Exclude the words 'the' and 'Microsoft' from list:

#     > python most_common_word.py the Microsoft

#     Exclude the words 'the' and 'Microsoft' and limit output to 15:

#     > python most_common_word.py the Microsoft -n 15

#     > python most_common_word.py -n 15 the Microsoft

#     """

#     page = get_page_content()
#     if exclude is None:
#         exclude = []

#     result = get_page_word_count(page, number, exclude)

#     click.echo(result)


# if __name__ == "__main__":
#     cli()
