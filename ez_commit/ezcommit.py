import click
from ollama import generate
import subprocess


def get_git_diff():
    """
    Checks for staged changes using `git diff --staged --histogram`.
    If a diff is found, returns it; otherwise, returns None.
    """
    try:
        result = subprocess.run(
            ["git", "diff", "--staged", "--histogram"],
            capture_output=True,
            text=True,
            check=True,
        )

        diff_output = result.stdout.strip()

        if diff_output:
            return diff_output
        else:
            return None

    except subprocess.CalledProcessError as e:

        click.echo(
            click.style(
                "Error: Not inside a Git repository or no staged changes.", fg="red"
            ),
            err=True,
        )
    except FileNotFoundError:

        click.echo(
            click.style(
                "Error: Git is not installed or not found in the system PATH.", fg="red"
            ),
            err=True,
        )
    except Exception as e:

        click.echo(click.style(f"Unexpected error: {e}", fg="red"), err=True)

    return None


def is_inside_git_repo():
    """Checks if the current directory is inside a Git repository."""
    try:
        subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            capture_output=True,
            text=True,
            check=True,
        )
        return True
    except subprocess.CalledProcessError:

        click.echo(
            click.style(
                "Error: This command must be run inside a Git repository.", fg="red"
            ),
            err=True,
        )
    except FileNotFoundError:

        click.echo(
            click.style(
                "Error: Git is not installed or not found in the system PATH.", fg="red"
            ),
            err=True,
        )
    except Exception as e:

        click.echo(click.style(f"Unexpected error: {e}", fg="red"), err=True)

    return False


def check_git_installed():
    """Checks if Git is installed and accessible"""
    try:
        subprocess.run(
            ["git", "--version"], capture_output=True, text=True, check=True
        ).stdout.strip()
        return True
    except subprocess.CalledProcessError:

        click.echo(
            click.style("Error: Git command failed unexpectedly.", fg="red"), err=True
        )
    except FileNotFoundError:

        click.echo(
            click.style(
                "Error: Git is not installed or not found in the system PATH.", fg="red"
            ),
            err=True,
        )
    except Exception as e:

        click.echo(click.style(f"Unexpected error: {e}", fg="red"), err=True)

    return False


@click.command()
def main():
    """A CLI Tool that does nothing for now"""

    if not check_git_installed() or not is_inside_git_repo():
        raise click.Abort()

    diff = get_git_diff()
    if diff:
        print("Staged Changes Found:")
        print(diff)
    else:
        print("No staged changes detected.")
        raise click.Abort()
    response = generate(
        "gemma3:1b",
        "What is 2+2?",
    )
    click.echo(f"{response['response'].strip()}")


if __name__ == "__main__":
    main()
