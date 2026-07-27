''' Дано список:
logs = [
    "LoginTest,PASSED,1.24",
    "PaymentTest,FAILED,2.81",
    "CartTest,PASSED,0.93",
    "SearchTest,FAILED,1.78",
    "LogoutTest,PASSED,0.65",
]
Потрібно реалізувати функції.
parse_logs(logs)
Повертає список словників
[
    {
        "name": "LoginTest",
        "status": "PASSED",
        "duration": 1.24
    },
    ...
]

count_passed(logs)
Повертає кількість успішних тестів.

count_failed(logs)
Повертає кількість невдалих тестів.

get_failed_tests(logs)
Повертає список назв тестів, що впали.

get_average_duration(logs)
Повертає середню тривалість виконання.

sort_by_duration(logs)
Повертає список тестів, відсортований за часом виконання (від більшого до меншого). '''

logs = [
    "LoginTest,PASSED,1.24",
    "PaymentTest,FAILED,2.81",
    "CartTest,PASSED,0.93",
    "SearchTest,FAILED,1.78",
    "LogoutTest,PASSED,0.65",
]


def parse_logs(logs):
    logs_list = []
    for log in logs:
        splitted_logs = log.split(',')
        logs_d = {"name": splitted_logs[0],
                  "status": splitted_logs[1],
                  "duration": float(splitted_logs[2])}
        logs_list.append(logs_d)

    return logs_list


def count_passed(logs):
    count = 0
    for log in logs:
        if log["status"] == "PASSED":
            count += 1
    return count

def count_failed(logs):
    count = 0
    for log in logs:
        if log["status"] == "FAILED":
            count += 1
    return count

def failed_tests(logs):
    failed_tests = []
    for log in logs:
        if log["status"] == "FAILED":
            failed_tests.append(log["name"])
    return failed_tests

def average_duration(logs):
    durations = 0
    for log in logs:
        durations += log["duration"]
    return durations / len(logs)

def sort_by_duration(logs):
    return sorted(logs, key= lambda log: log["duration"], reverse=True)


