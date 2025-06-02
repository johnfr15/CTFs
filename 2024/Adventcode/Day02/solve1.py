import requests

COOKIES = {
    "session": "53616c7465645f5f0b6cd6815d3911002a6b35e26ce8046f681ef754e8bc2f562c77daebb367f9679f18f9add4ebb1b8037705eaddfb11215b6ec3009af649aa",
}

def get_reports():
    res = requests.get("https://adventofcode.com/2024/day/2/input", cookies=COOKIES)
    lines = res.text.split("\n")
    lines = [ line.split(" ") for line in lines ]
    lines.pop()

    pairs = [ [int(e) for e in line] for line in lines ]
    return pairs

def sanitize(reports: list[list[int]]) -> list[list[int]]:
    cleaned: list[list[int]] = []

    for report in reports:
        inc = report[0] < report[1]

        n_unsafe = count_unsafe(report)

        if n_unsafe == 1:
            report = remove_unsafelevel(report, inc)
            if is_safe(report):
                print(report)
                cleaned.append(report)
        if n_unsafe == 0:
            if is_safe(report):
                print(report)
                cleaned.append(report)

    return cleaned


def remove_unsafelevel(lst, inc):
    for idx, e in enumerate(lst):
        if idx == 0: continue
        if inc and lst[idx-1] >= lst[idx]:
            del lst[idx-1]
            return lst
        if not inc and lst[idx-1] <= lst[idx]:
            del lst[idx-1]
            return lst
    return lst

def count_unsafe(report):
    inc = report[0] < report[1]
    c = 0
    for idx, e in enumerate(report):
        if idx == 0: continue
        if inc and report[idx-1] >= report[idx]: c += 1
        if not inc and report[idx-1] <= report[idx]: c += 1

    return c

def is_safe(report):
    diff = [ abs(report[i-1] - report[i]) for i in range(1, len(report)) ]
    maximum = max(diff)
    minimum = min(diff)
    if maximum < 4 and minimum > 0:
        return 1
    return 0


def solve(reports: list[list[int]]):
    safe = 0
    
    for report in reports:
        diff = [ abs(report[i-1] - report[i]) for i in range(1, len(report)) ]
        maximum = max(diff)
        minimum = min(diff)
        if maximum < 4 and minimum > 0:
            safe += 1

    return safe





def is_sorted_and_valid(report):
    """Checks if the report is sorted and all adjacent differences are valid."""
    diffs = [abs(report[i] - report[i + 1]) for i in range(len(report) - 1)]
    return (all(report[i] < report[i + 1] for i in range(len(report) - 1)) or
            all(report[i] > report[i + 1] for i in range(len(report) - 1))) and \
           all(1 <= d <= 3 for d in diffs)

def can_be_safe_with_one_removal(report):
    """Checks if removing one level from the report makes it safe."""
    for i in range(len(report)):
        # Create a new report without the i-th level
        modified_report = report[:i] + report[i + 1:]
        if is_sorted_and_valid(modified_report):
            return True
    return False

def solve_with_dampener(reports):
    """Counts reports that are safe or can be made safe with one level removed."""
    safe_count = 0

    for report in reports:
        if is_sorted_and_valid(report) or can_be_safe_with_one_removal(report):
            safe_count += 1

    return safe_count




if __name__ == "__main__":

    print( [ i for i in range(5) ] )
    # reports = get_reports()
    # res = solve_with_dampener(reports)
    # print(res)