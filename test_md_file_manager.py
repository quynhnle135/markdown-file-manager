import tempfile
import unittest.mock as mock
from md_file_manager import *
import os
import datetime


# Test for path_exists function
def test_path_exists_1():
    assert path_exists("/Users/quinnle/Desktop") == True


def test_path_exists_2():
    assert path_exists("/Users/quinnle/nothing") == False


# Test for is_md_file function
def test_is_md_file_1():
    assert is_md_file("/Users/quinnle/PycharmProjects/md-file-manager/draft.md") == True


def test_is_md_file_2():
    assert is_md_file("/Users/quinnle/PycharmProjects/md-file-manager/draft.txt") == False


# Test for count_md_files function
def test_count_md_files_1():
    assert count_md_files("/Users/quinnle/PycharmProjects/md-file-manager/folder1") == 10


def test_count_md_files_2():
    assert count_md_files("/Users/quinnle/PycharmProjects/md-file-manager/md_files") == 8


def test_count_md_files_3():
    assert count_md_files("/Users/quinnle/PycharmProjects/md-file-manager") == 1


# Test for generate_single_md_file function
def test_generate_single_md_file_1():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmp_dir:
        generate_single_md_file(tmp_dir)

        file_date = datetime.date.today()
        expected_file_name = f"{file_date.strftime('%y%m%d')}.md"
        expected_file_path = os.path.join(tmp_dir, expected_file_name)

        assert os.path.exists(expected_file_path) == True


# Test for generate_single_md_file function using mock
@mock.patch('os.path.exists')
@mock.patch('builtins.open', new_callable=mock.mock_open)
def test_generate_single_md_file_2(mock_open, mock_exists):
    # Set up the mock to return True for any path
    mock_exists.return_value = True

    # Call the function with a mock path
    generate_single_md_file('mock/path')

    # Construct the expected file name
    file_date = datetime.date.today()
    expected_file_name = f"{file_date.strftime('%y%m%d')}.md"
    expected_file_path = os.path.join("mock/path", expected_file_name)

    # Check if it was called correctly
    mock_open.assert_called_once_with(expected_file_path, "w")