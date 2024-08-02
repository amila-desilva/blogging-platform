import pytest
from io import StringIO
from unittest.mock import patch
from todo_app.tasks import ToDoList

def test_view_tasks_empty():
    todo_list = ToDoList()
    with patch('sys.stdout', new=StringIO()) as fake_out:
        todo_list.view_tasks()
        output = fake_out.getvalue().strip()
    assert "Your to-do list is empty." in output

def test_add_task():
    todo_list = ToDoList()
    with patch('builtins.input', return_value='Test task'):
        todo_list.add_task()
    assert len(todo_list.tasks) == 1
    assert todo_list.tasks[0] == 'Test task'

def test_delete_task_empty():
    todo_list = ToDoList()
    with patch('sys.stdout', new=StringIO()) as fake_out:
        todo_list.delete_task()
        output = fake_out.getvalue().strip()
    assert "Your to-do list is empty. Nothing to delete." in output
