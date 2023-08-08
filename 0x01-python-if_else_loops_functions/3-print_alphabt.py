#!/usr/bin/python3
for alpha_lowercase in range(97, 123):
    if (alpha_lowercase == 101) or (alpha_lowercase == 113):
        continue
    print("{:c}".format(alpha_lowercase), end='')
