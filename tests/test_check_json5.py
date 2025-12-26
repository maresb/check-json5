import pytest

from pre_commit_hooks.check_json5 import main


@pytest.mark.parametrize(
    ('filename', 'expected_retval'),
    [
        # Valid JSON (subset of JSON5)
        ('ok_json.json', 0),
        # JSON5-specific features
        ('ok_json5_with_comments.json5', 0),
        ('ok_json5_with_trailing_comma.json5', 0),
        ('ok_json5_unquoted_keys.json5', 0),
        ('ok_json5_numbers.json5', 0),
        ('ok_json5_multiline_string.json5', 0),
        # Invalid files
        ('bad_json5_syntax.json5', 1),
        ('duplicate_key.json5', 1),
        ('nested_duplicate_key.json5', 1),
    ],
)
def test_main(capsys, resource_path, filename, expected_retval):
    ret = main([resource_path(filename)])
    assert ret == expected_retval
    if expected_retval == 1:
        stdout, _ = capsys.readouterr()
        assert filename in stdout


def test_duplicate_key_error_message(capsys, resource_path):
    """Test that duplicate key errors include the key name."""
    ret = main([resource_path('duplicate_key.json5')])
    assert ret == 1
    stdout, _ = capsys.readouterr()
    assert 'Duplicate key' in stdout
    assert 'hello' in stdout


def test_non_utf8_file(tmp_path):
    """Test that non-UTF8 files are rejected."""
    f = tmp_path / 't.json5'
    f.write_bytes(b'\xa9\xfe\x12')
    assert main([str(f)]) == 1


def test_multiple_files(resource_path):
    """Test processing multiple files at once."""
    files = [
        resource_path('ok_json.json'),
        resource_path('ok_json5_with_comments.json5'),
    ]
    assert main(files) == 0


def test_multiple_files_with_one_bad(capsys, resource_path):
    """Test that one bad file causes overall failure."""
    files = [
        resource_path('ok_json.json'),
        resource_path('bad_json5_syntax.json5'),
        resource_path('ok_json5_with_comments.json5'),
    ]
    ret = main(files)
    assert ret == 1
    stdout, _ = capsys.readouterr()
    assert 'bad_json5_syntax.json5' in stdout
    # Good files should not appear in error output
    assert 'ok_json.json' not in stdout


def test_empty_file(tmp_path):
    """Test that empty files are rejected (not valid JSON5)."""
    f = tmp_path / 'empty.json5'
    f.write_text('')
    assert main([str(f)]) == 1


def test_no_files():
    """Test with no files provided."""
    assert main([]) == 0

