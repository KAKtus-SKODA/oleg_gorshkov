def get_mask_card_number(card_number: str) -> str:
    """ Маскирует номер карты, оставляя видимыми первые 6 и последние 4 цифры,
    с разделением на блоки по 4 символа и звездочками вместо скрытых цифр """
    masked_part = '*' * (len(card_number) - 6 - 4)
    masked_number = f"{card_number[:6]}{masked_part}{card_number[-4:]}"
    parts = []
    for i in range(0, len(masked_number), 4):
        parts.append(masked_number[i:i + 4])
    return " ".join(parts)


input_card_number = "7000792289606361"
masked_output = get_mask_card_number(input_card_number)
print(f"Исходный номер карты: {input_card_number}")
print(f"Маскированный номер карты: {masked_output}")


def get_mask_account(account_number: str) -> str:
    """ Маскирует номер банковского счета, оставляя видимыми последние 4 цифры,
    и 2 звездочкивместо скрытых цифр """
    last_four_digits = account_number[-4:]
    masked_account = "**" + last_four_digits
    return masked_account


masked_number = get_mask_account("73654108430135874305")
print(masked_number)
