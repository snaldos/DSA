# test_approx_match.py

import os
import tempfile

import pytest

from dynamic_programming.approx_match import (edit_distance,
                                              num_approximate_string_matching)


def test_edit_distance():
    # Test cases for edit_distance
    assert (
        edit_distance("kitten", "sitting") == 3
    )  # Replace 'k'->'s', 'e'->'i', add 'g'
    assert edit_distance("flaw", "lawn") == 2  # Replace 'f'->'l', 'w'->'n'
    assert edit_distance("intention", "execution") == 5  # Multiple edits
    assert edit_distance("", "abc") == 3  # Insert all characters
    assert edit_distance("abc", "") == 3  # Delete all characters
    assert edit_distance("abc", "abc") == 0  # No edits needed


def test_edit_distance_basic():
    assert edit_distance("kitten", "sitting") == 3
    assert edit_distance("flaw", "lawn") == 2
    assert edit_distance("abc", "abc") == 0
    assert edit_distance("", "abc") == 3
    assert edit_distance("abc", "") == 3


def test_num_approximate_string_matching(tmp_path):
    # Create a temporary file with some words
    content = "kitten sitting biten mitten"
    test_file = tmp_path / "test.txt"
    test_file.write_text(content)

    # We expect the average edit distance between "kitten" and the file words
    distances = [edit_distance("kitten", word) for word in content.split()]
    expected_average = sum(distances) / len(distances)

    result = num_approximate_string_matching(str(test_file), "kitten")
    assert result == expected_average


def test_num_approximate_string_matching_file_not_found():
    result = num_approximate_string_matching("non_existent_file.txt", "kitten")
    assert result == -1
