"""Demonstrate measurement formatting and display-only units."""

from labplotlib import Measurement


def main() -> None:
    pressure = Measurement.from_pm(2_000_000, 100_000)
    print("Automatic:", pressure)
    print("Raw:", pressure.to_string(format="raw"))
    print("Scientific:", pressure.to_string(format="scientific"))

    print("Display in MPa:", pressure.to_string(unit="Pa", prefix="mega"))
    print("Display in kPa:", pressure.to_string(unit="Pa", prefix="kilo"))
    print("Stored value in Pa:", pressure.value)

    doubled = pressure * 2
    print("Arithmetic result:", doubled.to_string(unit="Pa", prefix="mega"))


if __name__ == "__main__":
    main()
