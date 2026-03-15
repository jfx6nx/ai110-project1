from logic_utils import check_guess

# Github Copilot generated tests for check_guess function in logic_utils.py
def test_guess_too_high():
    outcome, message = check_guess(guess=60, secret=50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low():
    outcome, message = check_guess(guess=30, secret=50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_guess_correct():
    outcome, message = check_guess(guess=50, secret=50)
    assert outcome == "Win"
    assert "Correct" in message


def test_guess_one_above():
    outcome, _ = check_guess(guess=51, secret=50)
    assert outcome == "Too High"


def test_guess_one_below():
    outcome, _ = check_guess(guess=49, secret=50)
    assert outcome == "Too Low"


def test_guess_zero():
    outcome, _ = check_guess(guess=0, secret=50)
    assert outcome == "Too Low"


def test_guess_equals_secret_at_boundaries():
    outcome, _ = check_guess(guess=1, secret=1)
    assert outcome == "Win"
