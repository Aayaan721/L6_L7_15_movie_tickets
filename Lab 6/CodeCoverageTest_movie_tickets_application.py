"""Lab 6, stage 1: target every executable application statement.

Student: Aayaan Kamil (PES2UG24CS017)
The application file, movie_tickets.py, is intentionally unmodified.
"""

import pytest

from movie_tickets import group_discount, snack_combo, ticket_price


def test_regular_adult_afternoon_weekday():
    assert ticket_price("regular", 25, 15, False) == 150


def test_premium_senior_evening_weekend():
    # 250 + 30 (evening) + 40 (weekend), then 50% senior discount.
    assert ticket_price("premium", 60, 18, True) == 160


def test_recliner_early_morning_child_under_three():
    assert ticket_price("recliner", 2, 11, False) == 0


def test_child_discount_with_morning_and_weekend():
    # 150 - 50 (morning) + 40 (weekend), then half price.
    assert ticket_price("regular", 12, 8, True) == 70


def test_invalid_seat_is_rejected():
    with pytest.raises(ValueError, match="unknown seat"):
        ticket_price("balcony", 25, 15, False)


@pytest.mark.parametrize("invalid_hour", [-1, 24])
def test_invalid_show_time_is_rejected(invalid_hour):
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, invalid_hour, False)


def test_no_tickets_is_rejected():
    with pytest.raises(ValueError, match="no tickets"):
        group_discount(0, False)


def test_small_group_has_no_discount():
    assert group_discount(2, False) == 0


def test_medium_student_group_gets_bonus():
    assert group_discount(5, True) == 15


def test_large_group_gets_standard_discount():
    assert group_discount(10, False) == 15


def test_small_snack_combo_without_coupon():
    assert snack_combo("small", False) == 120


def test_medium_snack_combo_with_coupon():
    assert snack_combo("medium", True) == 130


def test_large_snack_combo_without_coupon():
    assert snack_combo("large", False) == 250
