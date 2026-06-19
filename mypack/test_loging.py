import pytest


@pytest.mark.regression
@pytest.mark.smoke
def test_login(setup):
    print("this is login")
    assert True == True


@pytest.mark.regression
def test_login_facebook(setup):
    print("this is not login")
    assert True == True

# @pytest.mark.skip : Decorator to skip the function while runntime is maximum
#pytest mypack -s -v -m "smoke and regression"
#-n 2 for parllel testing
