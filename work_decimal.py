import decimal


# print(round(1.5, 0))
# print(round(2.5, 0))
target1 = 1.5
target2 = 2.5

rounded_coins = decimal.Decimal(target1).quantize(
    decimal.Decimal("0.00"), rounding=decimal.ROUND_HALF_UP
)
rounded_coins2 = decimal.Decimal(target2).quantize(
    decimal.Decimal("0."), rounding=decimal.ROUND_HALF_UP
)
pass
