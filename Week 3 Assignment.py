"""
RECORD CHECK  -  my version
===========================

Name  : Hania
Lane  : IT
Date  : 09/10/2026
Run it: python template.py
"""

def status_of(percent):
    """Return status based on percentage threshold."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check(value, limit):
    """Calculate and return difference and percentage."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent

def print_report(label, value, limit, difference, percent, status):
    """Print the formatted record report with borders."""
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Used        : {value:>10.2f}")
    print(f"  Total       : {limit:>10.2f}")
    print(f"  Free        : {difference:>10.2f}")
    print(f"  Percent     : {percent:>10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)


def status_of(percent):
    """Return status based on percentage threshold."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check(value, limit):
    """Calculate and return difference and percentage."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent

def print_report(label, value, limit, difference, percent, status):
    """Print the formatted record report with borders."""
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Used        : {value:>10.2f}")
    print(f"  Total       : {limit:>10.2f}")
    print(f"  Free        : {difference:>10.2f}")
    print(f"  Percent     : {percent:>10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)


# 2. Ask for your three values.



# =================================================================== OUTPUT
# 4. Print the report.



# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it

if __name__ == "__main__":
    over_limit_count = 0

    while True:
        print()
        label = input("Enter hostname (or 'quit' to stop): ").strip()
        if label.lower() == "quit":
            break

        value = float(input("Enter GB used: "))
        limit = float(input("Enter GB total: "))

        difference, percent = check(value, limit)
        status = status_of(percent)

        if status == "OVER LIMIT":
            over_limit_count += 1

        print_report(label, value, limit, difference, percent, status)

    print(f"\nTotal OVER LIMIT records found: {over_limit_count}")