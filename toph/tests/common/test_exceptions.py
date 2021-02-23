from toph.common.exceptions import printException

def test_exceptions(capsys):
        printException(__name__)
        captured = capsys.readouterr()
        assert captured.out == "[Error][toph.tests.common.test_exceptions]\n"
