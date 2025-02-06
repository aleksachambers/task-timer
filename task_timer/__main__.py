import click
import time, datetime
from task_timer.run_task import Task

@click.group()
def main():
    """This is my main cli."""

@main.command()
def begin():
    print(Task.start)
    print(Task.current_task)

@main.command()
def end():
    print(Task.end)