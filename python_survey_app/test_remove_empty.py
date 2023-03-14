import pytest

# Test remove_empty_lines function
def test_remove_empty_rows():
    #arrange - creating an object (dataframe) that is needed for the test, containing dummy data to pass into the test function
    dummy_data = [
        ['1', 'Noel', 'Hartley', 'Yes', 'a', '9'],
        ['2', 'Aimee', 'Hartley', 'Yes', 'Yes', '2'],
        ['', '', '', '', '', ''],
        ['3', 'Penny', 'Hartley', '3', 'b', '15'],
        ['', '', '', '', '', ''],
        ['', '', '', '', '', ''],
        ['4', 'Amy', 'Holden', '', '', '8'],
        ['', '', '', '', '', '']
    ]
    #act - calling the function that is under test - expected_data is a dataframe with no empty rows
    expected_result = [
        ['1', 'Noel', 'Hartley', 'Yes', 'a', '9'],
        ['2', 'Aimee', 'Hartley', 'Yes', 'Yes', '2'],
        ['3', 'Penny', 'Hartley', '3', 'b', '15'],
        ['4', 'Amy', 'Holden', '', '', '8']
    ]
    #assert - testing the result of calling the output function vs the test(expected_data) 
    assert test_remove_empty_rows(dummy_data) == expected_result
