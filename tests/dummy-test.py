import subprocess as sp

def format_powershell_string(string):
    return string.replace("\n", "")
    
def format_powershell_array(array):
    array = array.split("\n")
    del array[len(array) - 1]
    return array

def test_try_powershell_number():
    number = sp.check_output(['pwsh', '-c', 'return 1+1'])
    assert int(number) == 2

def test_try_powershell_array():
    array = sp.check_output(['pwsh', '-c', 'return @(1,2,3)'])
    array = format_powershell_array(array)
    assert len(array) == 3

def test_try_powershell_string():
    string = sp.check_output(['pwsh', '-c', 'return "hello"'])
    assert format_powershell_string(string) == 'hello'

def test_starting_outzzz():
    assert 1 == 1