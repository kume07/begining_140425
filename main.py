import database

import utils

import auth


def main():
    database.setup_database()

    name, password = auth.get_user_and_pass()

    utils.process_devision(56, divisor=3)
    utils.process_substraction(subtrahend=56, minuend=5)
    utils.process_mult(56, 3)


if __name__ == "__main__":
    main()
