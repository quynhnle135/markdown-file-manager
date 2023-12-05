import tempfile
from unittest.mock import patch
from md_file_manager import *


def test_path_exists_1():
    assert path_exists("/Users/quinnle/Desktop") == True


def test_path_exists_2():
    assert path_exists("/Users/quinnle/nothing") == False


def test_is_md_file_1():
    assert is_md_file("/Users/quinnle/PycharmProjects/md-file-manager/draft.md") == True


def test_is_md_file_2():
    assert is_md_file("/Users/quinnle/PycharmProjects/md-file-manager/draft.txt") == False


def test_count_md_files_1():
    assert count_md_files("/Users/quinnle/PycharmProjects/md-file-manager/folder1") == 21


def test_count_md_files_2():
    assert count_md_files("/Users/quinnle/PycharmProjects/md-file-manager/md_files") == 8


def test_count_md_files_3():
    assert count_md_files("/Users/quinnle/PycharmProjects/md-file-manager") == 2


def test_read_file_1():
    expected_output = ['# Heading 1\n', '## Heading 2']
    assert read_file("/Users/quinnle/PycharmProjects/md-file-manager/draft.md") == expected_output


def test_read_file_2():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as tmpfile:
        content = "Line 1\nLine 2\nLine 3"
        tmpfile.write(content)
        tmpfile_name = tmpfile.name

    lines = read_file(tmpfile_name)
    assert lines == ["Line 1\n", "Line 2\n", "Line 3"]

    os.remove(tmpfile_name)


@patch("md_file_manager.is_md_file", return_value=False)
def test_read_file_4(mock_is_md_file):
    assert read_file("/path/to/non-md-file.txt") is None




