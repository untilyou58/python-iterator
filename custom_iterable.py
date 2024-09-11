from datetime import date, timedelta


class DateRange:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __iter__(self):
        current_date = self.start_date
        while current_date <= self.end_date:
            yield current_date
            current_date += timedelta(days=1)


# Usage
start = date(2023, 1, 1)
end = date(2023, 1, 10)
for d in DateRange(start, end):
    print(d)

# Output:
# 2023-01-01
# 2023-01-02
# 2023-01-03
# 2023-01-04
# 2023-01-05
# 2023-01-06
# 2023-01-07
# 2023-01-08
# 2023-01-09
# 2023-01-10
