def psd(salary, debt_quota):
    if debt_quota >= salary:
        return 100
    return (debt_quota * 100) / salary


def solidary_tax(tax, salary, debt_quota):
    if (500000 < salary <= 1500000) or (45 < psd(salary, debt_quota) <= 65):
        return salary * ((tax - 3) / 100)
    elif (salary > 1500000 and psd(salary, debt_quota) < 65) or salary > 4000000:
        return salary * (tax / 100)
    return 0.0


print(solidary_tax(5, 3000000, 2900000))


