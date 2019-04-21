def case_insen_compare(s1, s2, tol):
    if abs(len(s1) - len(s2)) > tol:
        return False

    init_work = sorted([s1, s2], key=len)
    init_work.append(0)
    work_items = [init_work]

    for item in work_items:
        s1 = item[0]
        s2 = item[1]
        mismatch_count = item[2]

        for i in range(len(s1)):
            if s1[0].lower() != s2[0].lower():
                mismatch_count += 1
                if mismatch_count > tol:
                    break

                new_work = sorted([s1, s2[1:]], key=len)
                new_work.append(mismatch_count)
                work_items.append(new_work)

        if mismatch_count + len(s2) - len(s1) <= tol:
            return True

    return False

print(case_insen_compare('abc', 'ABC', 1))  # True
print(case_insen_compare('abc', 'def', 1))  # False
print(case_insen_compare('abc', 'ABCD', 1))  # True
print(case_insen_compare('abc', u'AC', 1))  # True
