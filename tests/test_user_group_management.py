import pytest
import subprocess as sp
def run_bash_command(command,suppressErrorAndReturnOutput = False):
    try:
        result = sp.check_output(command,shell=True)
        return result
    except sp.CalledProcessError as exception:
        if suppressErrorAndReturnOutput:
            return exception.output
        else:
            raise exception

@pytest.fixture(scope='module')
def setup_test_users(request):
    testUserNames = ['testuser1', 'testuser2']
    for username in testUserNames:
        run_bash_command(f"sudo useradd {username} -m")

    def teardown_user():
        for username in testUserNames:
            try: # some tests may delete users, so we're going to ignore errors here
                run_bash_command(f"sudo userdel {username} -r")
            except Exception as e:
                print(e)
    request.addfinalizer(teardown_user)


def test_validate_usertest1_exists(setup_test_users):
    result = run_bash_command('getent passwd testuser1')
    assert 'testuser1' in str(result)

def test_check_if_users_exist_in_passwd_file(setup_test_users):
    # stores user information
    result = run_bash_command(
        'sudo cat /etc/passwd | grep -i "testuser"') #let grep match on just testuser
    assert ('testuser1' in str(result) and 'testuser2' in str(result))


def test_check_if_users_exist_in_shaddow_file(setup_test_users):
    # stores passwords/ authentication
    result = run_bash_command("sudo cat /etc/shadow | grep -i '\(testuser1\|testuser2\)'")
    assert ('testuser1' in str(result) and 'testuser2' in str(result))


def test_delete_usertest2_and_validate(setup_test_users):
    run_bash_command('sudo userdel testuser2')
    result = run_bash_command('getent passwd testuser2', True)
    print(result)
    assert 'testuser2' not in str(result)
