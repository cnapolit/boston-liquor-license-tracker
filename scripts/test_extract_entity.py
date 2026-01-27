"""
Simple tests for the scripts directory.
"""
import extract_entity
import pytest

empty_lines = [[], [" "], ["\t"], ["\n"], ["", "", ""]]
@pytest.mark.parametrize("lines", empty_lines)
def test_parse_entity_receives_empty_lines_returns_empty_result(lines):
    # When
    result = extract_entity.parse_entity(lines)
    # Then
    assert all(value is None for value in result.values())

# The list of inputs
header_lines = [(1, "Some Company LLC"), (365, "some lower case company inc.")]
@pytest.mark.parametrize("number,business_name", header_lines)
def test_parse_entity_includes_section_header_returns_name_and_number(number, business_name):
    # Given
    line = [f"{number}. {business_name}"]
    # When
    result = extract_entity.parse_entity(line)
    # Then
    assert result["entity_number"] == number
    assert result["business_name"] == business_name

fields = [
    ("Doing Business As:", "dba_name", "ABC Corp"),
    ("License #:","license_number", "LB-123456"),
    ("123 Boston St, Boston, MA 02116"), 
]
@pytest.mark.parametrize("line,key,value", fields)
def test_parse_entity_recognizes_field_returns_result(field, key, value):
    # Given
    line = [field + " " + value]
    # When
    result = extract_entity.parse_entity(line)
    # Then
    assert result[key] == value