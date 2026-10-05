""" Module to explore enumerate"""


def print_playlist(playlist):
    """Print each song with its position number"""
    for index, song in enumerate(playlist, start=1):
        print(index, song)


playlist = ["Yaro yaro", "Megamai vanthu", "Vinnai thandi"]
print_playlist(playlist)


def print_tasks(tasks):
    """Print each Tasks in format: TaskN:<Task>: """
    for index, task in enumerate(tasks, start=1):
        print(f"Task{index}: {task}")


tasks = ["Reading", "Writing", "Drawing", "Coding"]
print_tasks(tasks)


def print_indexes(scores, threshold):
    """Print each index of score greater than Threshold"""
    for index, score in enumerate(scores):
        if score > threshold:
            print(index)


def print_index(scores, threshold):
    """Print each index of score greater than Threshold using range and len"""
    for index in range(len(scores)):  # Not a preferred way. Choose enumerate over range and len since python provide built in feature
        if scores[index] > threshold:
            print(index)


scores = [20, 30, 45, 32, 67]
print_indexes(scores, 30)
