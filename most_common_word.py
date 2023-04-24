import click
from src.parse_html import get_page_word_count, get_page_content


@click.command()
@click.option("--number", "-n", default=10, help="Number of words to return.")
@click.argument("exclude", nargs=-1, default=None, type=str)
def cli(number, exclude):
    """
    Returns a count of most common word in the history section of https://en.wikipedia.org/wiki/Microsoft.

    Word count is returned in descending order.


    === Example Use ===

    Default:

    > python most_common_word.py

    Set number of words to return:

    > python most_common_word.py --number 5

    > python most_common_word.py -n 5

    Exclude the words 'the' and 'Microsoft' from list:

    > python most_common_word.py the Microsoft

    Exclude the words 'the' and 'Microsoft' and limit output to 15:

    > python most_common_word.py the Microsoft -n 15

    > python most_common_word.py -n 15 the Microsoft

    """

    page = get_page_content()
    if exclude is None:
        exclude = []

    result = get_page_word_count(page, number, exclude)

    click.echo(result)


if __name__ == "__main__":
    cli()
