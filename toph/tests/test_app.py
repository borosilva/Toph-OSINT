from toph.app import run
import sys
import unittest

def test_disabling_capturing(capsys):
    print("hello")
    sys.stderr.write("world\n")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
    assert captured.err == "world\n"
    print("next")
    captured = capsys.readouterr()
    assert captured.out == "next\n"

def test_app(capsys):
    run()
    captured = capsys.readouterr()
    assert len(captured.out) == 542