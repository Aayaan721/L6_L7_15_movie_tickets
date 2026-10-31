"""Lab 6, stage 2: exercise both outcomes of each decision branch.

Student: Aayaan Kamil (PES2UG24CS017)
Run under `coverage run --branch` for the branch-coverage result.
"""

import pytest

from movie_tickets import group_discount, snack_combo, ticket_price


@pytest.mark.parametrize(
    ("seat", "age", "hour", "weekend", "expected"),
    [
        ("regular", 25, 15, False, 150),  # normal adult / afternoon
        ("premium", 60, 18, True, 160),  # senior / evening / weekend
        ("recliner", 2, 11, False, 0),  # child under 3 / morning
        ("regular", 12, 8, True, 70),  # child exactly 12 / morning
        ("premium", 13, 12, False, 250),  # adult exactly 13 / noon
        ("regular", 3, 0, False, 50),  # child exactly 3 / earliest hour
        ("regular", 59, 17, False, 150),  # just below senior age
        ("regular", 60, 23, False, 90),  # senior boundary / latest hour
        ("recliner", 25, 18, False, 430),  # recliner / evening
    ],
)
def test_ticket_price_decision_paths(seat, age, hour, weekend, expected):
    assert ticket_price(seat, age, hour, weekend) == expected


def test_invalid_seat():
    with pytest.raises(ValueError, match="unknown seat"):
        ticket_price("balcony", 25, 15, False)


@pytest.mark.parametrize("hour", [-1, 24])
def test_show_hour_outside_valid_range(hour):
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, hour, False)


@pytest.mark.parametrize("tickets", [0, -1])
def test_invalid_group_size(tickets):
    with pytest.raises(ValueError, match="no tickets"):
        group_discount(tickets, False)


@pytest.mark.parametrize(
    ("tickets", "student", "expected"),
    [
        (1, False, 0),  # no qualifying discount
        (4, True, 0),  # student status alone does not earn 5%
        (5, False, 10),  # lower 10% tier boundary
        (9, True, 15),  # upper boundary of 10% tier + student
        (10, False, 15),  # lower 15% tier boundary
        (10, True, 20),  # largest tier + student bonus
    ],
)
def test_group_discount_decision_paths(tickets, student, expected):
    assert group_discount(tickets, student) == expected


@pytest.mark.parametrize(
    ("size", "coupon", "expected"),
    [
        ("small", False, 120),
        ("small", True, 70),
        ("medium", False, 180),
        ("medium", True, 130),
        ("large", False, 250),
        ("large", True, 200),
    ],
)
def test_snack_combo_decision_paths(size, coupon, expected):
    assert snack_combo(size, coupon) == expected
