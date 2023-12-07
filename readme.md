# Fixing almost sorted 2

The problem  [Almost sorted 2](https://open.kattis.com/problems/almostsorted2) is almost surely broken.


It is equivalent to the following [problem](https://open.kattis.com/problems/inverteddeck). However, when submitting judge solutions from [here](https://2019.nwerc.eu/), they all fail on test case 9. I have no doubt that these correctly solve the problem, as there are 15 different judge solutions written by experienced problemsetters.

In this repository I have included the means to stress-test these against a naive solution and arbitrarly many cases. 1000 did not fail any. Still, all these solutions get WA.

# What went wrong

The judge solution is almost surely incorrect. Through sheer luck, Calle Svensson wrote a solution that has the same bug as the judge solution. It can be found in realac/zetatwo.py

The primary test case illustrating the issue is:

4

5 5 2 7

For which zetatwo.py says "No" for, even though you can reverse a prefix to get 2 5 5 7. It is very likely that the judge solution has the exact same bug, where it can't handle a prefix of the same number needing to be reversed.


## Not a statement bug

We also considered the alternative that the author intended "strictly increasing". This would imply that any duplicate number at all results in "No". Submitting a solution that prints "No" if not all numbers are unique yields a wrong answer at test case 5. 

## The proposed solution

Use nwerc1.cpp or nwerc2.cpp as judge solution, and re-generate the test data.
