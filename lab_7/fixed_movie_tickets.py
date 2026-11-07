import re


def parse_seat(seat):
    if not isinstance(seat, str):
        return None

    match = re.fullmatch(r"([A-Za-z])([1-9][0-9]*)", seat.strip())
    if not match:
        return None

    return match.group(1).upper(), int(match.group(2))


def total_price(prices_csv):
    if not isinstance(prices_csv, str):
        return 0.0

    try:
        prices = [int(p.strip()) for p in prices_csv.split(",")]
        if any(p < 0 for p in prices):
            return 0.0
        return round(sum(prices) * 1.18, 2)
    except (ValueError, TypeError, OverflowError):
        return 0.0


def average_rating(ratings):
    if not isinstance(ratings, str):
        return 0.0

    try:
        values = [int(r) for r in ratings.split()]
        if not values or any(r < 1 or r > 5 for r in values):
            return 0.0
        return round(sum(values) / len(values), 1)
    except (ValueError, TypeError, OverflowError):
        return 0.0


def main():
    print("==== Running parse_seat ====")
    user_input = input("Enter a seat number (e.g. H12): ")
    result = parse_seat(user_input)
    print("Row and Seat:", result)

    print("\n==== Running total_price ====")
    user_input = input("Enter ticket prices as CSV (e.g. 150,250,400): ")
    result = total_price(user_input)
    print("Total with GST:", result)

    print("\n==== Running average_rating ====")
    user_input = input("Enter ratings separated by spaces (e.g. 4 5 3): ")
    result = average_rating(user_input)
    print("Average Rating:", result)


if __name__ == "__main__":
    main()
