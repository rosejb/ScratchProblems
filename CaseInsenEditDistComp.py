def case_insen_compare(s1, s2, tol):
    if abs(len(s1) - len(s2)) > tol:
        return False

    init_work = {'words': sorted([s1, s2], key=len), 'mismatches': 0}
    work_items = [init_work]

    for work_dict in work_items:
        s1 = work_dict['words'][0]
        s2 = work_dict['words'][1]
        mismatch_count = work_dict['mismatches']

        for i in range(len(s1)):
            if s1[0].lower() != s2[0].lower():
                mismatch_count += 1
                if mismatch_count > tol:
                    break

                new_work = {'words': sorted([s1, s2[1:]], key=len),
                            'mismatches': mismatch_count}
                work_items.append(new_work)

        if mismatch_count + len(s2) - len(s1) <= tol:
            return True

    return False

def case_insen_compare_rec(s1, s2, tol, mismatch_count = 0):
    if abs(len(s1) - len(s2)) > tol - mismatch_count:
        return False

    s1, s2 = sorted([s1, s2], key=len)

    for i in range(len(s1)):
        if s1[0].lower() != s2[0].lower():
            mismatch_count += 1

            if mismatch_count > tol:
                return False

            if case_insen_compare_rec(s1, s2[1:], tol, mismatch_count):
                return True

    return len(s2) - len(s1) + mismatch_count <= tol


def greet(name: str):
    print(f'Oh hi {name}')


print('This is different')

print('Testing Iterative Implementation')
print(case_insen_compare('abc', 'ABC', 1))  # True
print(case_insen_compare('abc', 'def', 1))  # False
print(case_insen_compare('abc', 'ABCD', 1))  # True
print(case_insen_compare('abc', u'AC', 1))  # True


print('\nTesting Recursive Implementation')
print(case_insen_compare_rec('abc', 'ABC', 1))  # True
print(case_insen_compare_rec('abc', 'def', 1))  # False
print(case_insen_compare_rec('abc', 'ABCD', 1))  # True
print(case_insen_compare_rec('abc', u'AC', 1))  # True
