
def is_leap_year(year: int):
    # leap year must be divided by 4, but must not be divided by 100, except if is divided by 400
    return True if not (year % 400) else False if not (year % 100) else True if not (year % 4) else False


def valid_pid(pid: str, detail_data=False):
    try:
        if not pid.isdigit():
            raise ValueError('Personal ID must be a number!')

        pid_length = len(pid)

        if not (9 <= pid_length <= 10):
            raise ValueError('Personal ID must have the length 9 or 10!')

        year = int(pid[:2])
        month = int(pid[2:4])
        day = int(pid[4:6])
        suffix = pid[6:]

        if pid_length == 9 or year > 53:
            year += 1900
        else:
            year += 2000

        if pid_length == 9 and year > 1953:
            raise ValueError(f'Wrong format of personal ID (length: {pid_length}, year: {year})')

        if not (1 <= month <= 12 or 51 <= month <= 62):
            raise ValueError(f'Wrong format of personal ID (month: {month})')

        pid_sex = ''
        if 1 <= month <= 12:
            pid_sex = 'M'
        elif 51 <= month <= 62:
            pid_sex = 'F'
            month -= 50

        month_days = {}
        month_days.update({m: 31 for m in (1, 3, 5, 7, 8, 10, 12)})
        month_days.update({m: 30 for m in (4, 6, 9, 11)})
        month_days.update({2: 29 if is_leap_year(year) else 28})

        if not(1 <= day <= month_days[month]):
            raise ValueError(f'Wrong format of personal ID (day: {day} -> month: {month} -> year: {year})')

        if pid_length == 9 and suffix == '000':
            raise ValueError(f'Wrong format of personal ID (surfix: {suffix})')
        elif pid_length == 10 and int(pid) % 11:
            raise ValueError(f'Wrong validate of personal ID (modulo 11 not a zero: {pid} % 11 = {int(pid) % 11})')
    except ValueError as err:
        if detail_data:
            return False, err.args[0]
        else:
            return False

    if detail_data:
        return True, {'year': year, 'month': month, 'day': day, 'sex': pid_sex}
    else:
        return True


if __name__ == '__main__':
    print('----- VALID ID -----')
    print("input:  valid_pid('5451230147', detail_data=True)}")
    print(f"output: {valid_pid('5451230147', detail_data=True)}")
    print()
    print('----- INVALID ID -----')
    print("input:  valid_pid('5451230142', detail_data=True)}")
    print(f"output: {valid_pid('5451230142', detail_data=True)}")
