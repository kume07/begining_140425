import os
import json
import constatns


def setup_database() -> None:
    database_name = constatns.DATABASE_NAME
    print(database_name)
    if os.path.exists(database_name):
        return

    with open(database_name, mode="w", encoding="utf-8") as file:

        json.dump([], file=file, indent=4)
