def is_angram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    print(sorted(s1))
    print(sorted(s2))

    return sorted(s1) == sorted(s2)

print(is_angram("hi", "ih"))
