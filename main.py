from datetime import date, datetime


def get_birthdays_per_week(dict_users):

    days_of_week = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday",
    }

    today = date.today()

    if (today.year - 1) % 4 == 0:
        day_in_last_year = 366
    else:
        day_in_last_year = 365

    bpw = {day: [] for day in days_of_week.values()}
    birthdays_per_week_empty = {day: [] for day in days_of_week.values()}
    ret_dict = {}
    counter = 0
    for user in dict_users:
        counter += 1
        birthday = user["birthday"]
        x1 = birthday.replace(year=1)
        x2 = today.replace(year=1)
        days_until_birthday = (x1 - x2).days

        if birthday.month == today.month and birthday.day == today.day:
            continue  # Skip if it's today's birthday
        if today.month == 12 and birthday.month == 1:
            days_until_birthday += day_in_last_year
        if 0 <= days_until_birthday <= 6:
            x1 = days_of_week[(today.weekday() + days_until_birthday) % 7]
            bpw[x1].append(user["name"])

    if bpw == birthdays_per_week_empty:
        return {}
    else:

        bpw['Monday'] = bpw['Saturday'] + bpw['Monday']
        bpw['Monday'] = bpw['Sunday'] + bpw['Monday']
        del bpw['Sunday']
        del bpw['Saturday']
        for key, value in bpw.items():
            if bpw[key] != birthdays_per_week_empty[key]:
                ret_dict.update({key: value})
    return ret_dict


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)

    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
