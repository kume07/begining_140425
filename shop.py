import decimal
import logging
from pywebio.input import slider, FLOAT, NUMBER

from pywebio.input import input as pw_input

from pywebio.output import put_html, put_success

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("shop.log"), logging.StreamHandler()],
)

CHEESE_PRICE = decimal.Decimal(286.3)
POTATO_PRICE = decimal.Decimal(40)

logging.debug("debug")
logging.info("info")
# HEADER
put_html("<h1>Welcome to our shop</h1>")

# INPUT SECTION

cheese_weight = slider(
    "Cheese", type=FLOAT, min_value=0, max_value=5, value=0.15, required=True
)
cheese_weight = decimal.Decimal(cheese_weight).quantize(
    decimal.Decimal("0.000"), rounding=decimal.ROUND_HALF_UP
)

potato_weight = pw_input("Potato", type=NUMBER, required=True, min=0, max=10, value=3)
potato_weight = decimal.Decimal(potato_weight).quantize(
    decimal.Decimal("0.000"), rounding=decimal.ROUND_HALF_UP
)
logging.info(f"{potato_weight=}")

cheese_cost = (CHEESE_PRICE * cheese_weight).quantize(
    decimal.Decimal("0.00"), rounding=decimal.ROUND_HALF_UP
)
potato_cost = (POTATO_PRICE * potato_weight).quantize(
    decimal.Decimal("0.00"), rounding=decimal.ROUND_HALF_UP
)
total_cost = cheese_cost + potato_cost
put_success(
    f"Total cost: \ncheese_cost\t{cheese_cost} \npotato_cost\t{potato_cost} \ntotal_cost\t{total_cost}"
)
