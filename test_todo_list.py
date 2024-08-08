import pytest
from todo_list import ToDoList  # Import the ToDoList class from your module

@pytest.fixture
def todo_list():
    """Fixture to create a new ToDoList instance for each test."""
    return ToDoList()

def test_add_task(todo_list):
    """Test adding a task to the list."""
    todo_list.add_task("Test task")
    assert len(todo_list.tasks) == 1
    assert todo_list.tasks[0] == {'task': 'Test task', 'completed': False}

def test_remove_task(todo_list):
    """Test removing a task from the list."""
    todo_list.add_task("Task to remove")
    todo_list.remove_task(0)
    assert len(todo_list.tasks) == 0

def test_complete_task(todo_list):
    """Test marking a task as completed."""
    todo_list.add_task("Task to complete")
    todo_list.complete_task(0)
    assert todo_list.tasks[0]['completed'] is True

def test_display_tasks_empty(capsys, todo_list):
    """Test displaying tasks when the list is empty."""
    todo_list.display_tasks()
    captured = capsys.readouterr()
    assert captured.out == "No tasks in the list.\n"

def test_display_tasks_not_empty(capsys, todo_list):
    """Test displaying tasks when the list is not empty."""
    todo_list.add_task("Task 1")
    todo_list.add_task("Task 2")
    todo_list.complete_task(0)
    todo_list.display_tasks()
    captured = capsys.readouterr()
    expected_output = (
        "1. Task 1 - Done\n"
        "2. Task 2 - Not Done\n"
    )
    assert captured.out == expected_output
