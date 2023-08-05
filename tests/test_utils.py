from utils import mask_card, mask_account, format_operation

def test_mask_card():
    card_number = "1234567890123456"
    expected_result = "123456******3456"
    assert mask_card(card_number) == expected_result

def test_mask_account():
    account_number = "1234567890"
    expected_result = "**7890"
    assert mask_account(account_number) == expected_result
