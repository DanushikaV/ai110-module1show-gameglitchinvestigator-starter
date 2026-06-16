def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 20
    elif difficulty == "Normal":
        return 1, 100
    elif difficulty == "Hard":
        return 1, 500
    return 1, 100


def parse_guess(raw: str):
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in str(raw):
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    guess = int(guess)
    secret = int(secret)

    if guess == secret:
        return "Win"
    elif guess > secret:
        return "Too High"
    else:
        return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    return max(0, current_score - 5)