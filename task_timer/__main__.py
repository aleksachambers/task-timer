import click
from task_timer.run_task import Task

@click.group()
def main():
    """This is my main cli."""

@main.command()
def run():
    """To start the timer, use 'uv run task-timer run'."""
    task = Task()
    task.start()