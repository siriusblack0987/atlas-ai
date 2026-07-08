current_user = None


def save_profile(user):
    global current_user

    current_user = user

    return current_user


def get_profile():

    return current_user