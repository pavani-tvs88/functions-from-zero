import click
from mylib.bot import scrape

# click.echo(click.style('Some more text', bg='blue', fg='white'))


@click.command()
@click.option(
    "--name", prompt="Wikipedia Page to scrape", help="Web Page we want to scrape."
)
@click.option("--length", default=3, help="Length of summary in sentences.")
def info(name, length):
    summary = scrape(name, length=length)
    click.echo(click.style(f"{summary}:", bg="white", fg="blue"))


if __name__ == "__main__":
    info()
