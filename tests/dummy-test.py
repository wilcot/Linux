import pytest
import subprocess as sp

def run_bash_command(command):
    result = sp.check_output(['bash', '-c', command])
    return result

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


@pytest.mark.incremental
class TestIncremental(object):
    def test_pass(self):
        pass

    def test_fail(self):
        assert 0

    def test_pass_but_skipped(self):
        pass

def test_should_pass():
    pass
