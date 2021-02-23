from toph.app import run
from unittest import mock

def test_app(capsys):

    with mock.patch('builtins.input', return_value=1):
        run()
        captured = capsys.readouterr()
        assert len(captured.out) == 836