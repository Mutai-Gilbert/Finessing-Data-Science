from collections import defaultdict

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
(48000, 0.7), (76000, 6),
(69000, 6.5), (76000, 7.5),(60000, 2.5), (83000, 10),
(48000, 1.9), (63000, 4.2)]

salary_by_tenure = defaultdict(list)

def tenure_bucket(tenure):
    if tenure < 2:
        return "Less than two"
    elif tenure < 5:
        return "Between two and five"
    else:
        return "More than five"
for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure[bucket].append(salary)


average_salary_by_bucket = {
    tenure_bucket: round(sum(salaries) / len(salaries))
    for tenure_bucket, salaries in salary_by_tenure.items()
}




print(average_salary_by_bucket)