import pytest
import subprocess as sp
def run_bash_command(command,suppressErrorAndReturnOutput = False):
    try:
        result = sp.check_output(['bash', '-c', command])
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


def test_delete_usertest2_and_validate(setup_test_users):
    run_bash_command('sudo userdel testuser2')
    result = run_bash_command('getent passwd testuser2', True)
    print(result)
    assert 'testuser2' not in str(result)
