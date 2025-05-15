def get_user_and_pass() -> tuple[str, str]:
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    return name, password


def is_valid_user_creds(
    user: str, password: str, force_permissions: bool = False
) -> bool:
    if user and force_permissions:
        return True


is_valid_user_creds("dddklld", "3333", False)
