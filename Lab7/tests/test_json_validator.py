import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from json_validator import validate

def read_file(path):
    with open(path, "r") as f:
        return f.read()

def test_easy_correct():
    json_text = read_file("tests/test_data/easy_correct.json")
    valid, msg = validate(json_text)
    assert valid, msg

def test_easy_broken():
    json_text = read_file("tests/test_data/easy_broken.json")
    valid, msg = validate(json_text)
    assert valid, msg

def test_medium_correct():
    json_text = read_file("tests/test_data/medium_correct.json")
    valid, msg = validate(json_text)
    assert valid, msg

def test_medium_broken():
    json_text = read_file("tests/test_data/medium_broken.json")
    valid, msg = validate(json_text)
    assert valid, msg