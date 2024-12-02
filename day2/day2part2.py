def is_valid(report):
    print(f"Report: {report}")
    valid_increase = False
    valid_decrease = False
    valid_diff = False
    # is all increasing or decreasing
    # validate increasing or decreasing
    if check_for_increasing(report):
        valid_increase = is_all_increasing(report)
        print(f"Is valid increase: {valid_increase}")
    else:
        valid_decrease = is_all_decreasing(report)
        print(f"Is valid decrease: {valid_decrease}")

    # differs by at least one and at most three
    valid_diff = is_valid_diff(report)
    print(f"Is valid diff: {valid_diff}")

    return valid_diff & (valid_increase or valid_decrease)


def is_valid_diff(report):
    i = 0
    while i < len(report) - 1:
        diff = abs(report[i] - report[i + 1])
        if diff == 0 or diff > 3:
            return False
        else:
            i += 1

    return True


def check_for_increasing(report):
    return report[0] < report[1]


def is_all_increasing(report):
    i = 0
    while i < len(report) - 1:
        if report[i] > report[i + 1]:
            return False
        else:
            i += 1

    return True


def is_all_decreasing(report):
    i = 0
    while i < len(report) - 1:
        if report[i] < report[i + 1]:
            return False
        else:
            i += 1

    return True


def is_valid_when_removed(report):
    for i in range(len(report)):
        temp_report = report[:i] + report[i + 1 :]
        if is_valid(temp_report):
            return True


if __name__ == "__main__":
    reports = []

    with open("day2.txt", "r") as file:
        data = file.read()

    lines = data.split("\n")

    reports = []
    for line in lines:
        reports.append(list(map(int, line.split())))

    counter = 0
    for report in reports:
        if is_valid(report) or is_valid_when_removed(report):
            counter += 1

    print(f"Number of valid reports is: {counter}")
