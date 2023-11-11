import tempfile
import unittest.mock as mock
from md_file_manager import *


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
    assert count_md_files("/Users/quinnle/PycharmProjects/md-file-manager") == 2


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


# Test for read_file function
def test_read_file_1():
    expected_output = ["line1\n", "line2\n", "line3"]
    assert read_file("/Users/quinnle/PycharmProjects/md-file-manager/draft.md") == expected_output


def test_read_file_2():
    assert read_file("/Users/quinnle/PycharmProjects/md-file-manager/draft2.md") == ["test"]


def test_read_file_3():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as tmpfile:
        content = "Line 1\nLine 2\nLine 3"
        tmpfile.write(content)
        tmpfile_name = tmpfile.name

    lines = read_file(tmpfile_name)
    assert lines == ["Line 1\n", "Line 2\n", "Line 3"]

    os.remove(tmpfile_name)


@mock.patch("md_file_manager.is_md_file", return_value=False)
def test_read_file_4(mock_is_md_file):
    assert read_file("/path/to/non-md-file.txt") is None


def test_md_file_generate_existing_directory():
    with tempfile.TemporaryDirectory() as tmp_dir:
        md_file_generate(tmp_dir)

        # Check for each of the next 7 days if a file has been created
        today = datetime.date.today()
        for i in range(1, 8):
            file_date = today + datetime.timedelta(days=i)
            file_name = f"{file_date.strftime('%Y%m%d')}.md"
            file_path = os.path.join(tmp_dir, file_name)

            assert os.path.exists(file_path), f"File {file_name} was not created."


def test_customized_md_file_generate():
    with tempfile.TemporaryDirectory() as tmp_dir:
        customized_md_file_generate(tmp_dir, 10)

        today = datetime.date.today()
        count = 0
        for i in range(1, 11):
            file_date = today + datetime.timedelta(days=i)
            file_name = f"{file_date.strftime('%Y%m%d')}.md"
            file_path = os.path.join(tmp_dir, file_name)
            count += 1
            assert os.path.exists(file_path), f"File {file_name} was not created."

        assert count == count_md_files(tmp_dir)


