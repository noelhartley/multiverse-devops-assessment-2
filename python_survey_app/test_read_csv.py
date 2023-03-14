import pytest
import csv

from read_csv import csv_data

def test_list():
  #arrange - creating an object that is needed for the test - the csv file and expected result which is a list
  file = open('results.csv')
  expected_result = list
  
  #act - calling the function that is under test - outputting the csv file as a list
  output = type(csv_data(file))

  #assert - testing the result of calling the output function vs the test(expected_result) 
  assert output == expected_result