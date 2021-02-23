from toph.menu.menu import printMenu
from unittest import mock

def test_printMenuSucces(capsys):
    with mock.patch('builtins.input', return_value=1):
        printMenu()
        captured = capsys.readouterr()
        assert len(captured.out) == 294

def test_printMenuError(capsys):
    with mock.patch('builtins.input', return_value='a'):
        printMenu()
        captured = capsys.readouterr()
        assert len(captured.out) == 318