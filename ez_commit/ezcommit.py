import click


@click.command()
def test():
    """A CLI Tool that does nothing for now"""
    click.echo(f"Hello this is a boilerplate CLI tool")


if __name__ == "__main__":
    test()
