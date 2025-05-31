# data_init.py
from Dad_income import Family

fam = Family("Dad")
fam.salary.add(35000, "2024-12-25", to_card=False)
fam.salary.add(30000, "2025-02-10", to_card=False)
fam.salary.add(20000, "2025-03-06", to_card=False)
fam.salary.add(33000, "2025-04-09", to_card=False)
fam.salary.add(33233, "2025-05-05", to_card=False)
fam.pension.add(2750, "2025-01-18")
fam.pension.add(2750, "2025-02-18")
fam.pension.add(3100, "2025-03-18")
fam.pension.add(3100, "2025-04-18")
fam.pension.add(3100, "2025-05-18")
