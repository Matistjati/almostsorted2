# Fixing almost sorted 2

The problem  [Almost sorted 2](https://open.kattis.com/problems/almostsorted2) is almost surely broken.


It is equivalent to the problem ["Inverted Deck"](https://open.kattis.com/problems/inverteddeck). Inverted Deck is a problem from NWERC, a competition where over 300 people people saw the problem, and 15 judge solutions were written. This means that the judge solutions to inverted deck are almost surely correct. However, when submitting judge solutions to Inverte deck found [here](https://2019.nwerc.eu/), they all fail on test case 9. This means that, supposing Almost sorted 2 and Inverted Deck are isomorphic problems, then the test data of Almost Sorted 2 is almost surely incorrect.

To be extra sure, I stress-tested the judge solutions against an "obviously correct" cubic solution. This is the main contens of the repository (see submissions). 1000 did not result in any solutions disagreeing.

Another indication that something is wrong is that the problem is of difficulty 8.6, unreasonably high for such an easy problem. I haven't been able to find a correct solution online. All easily accessible ones use some weird bypass (the author of this solution most likely overfitted using the test data, as they also attend NUS, the origin of the problem. [The solution in question](https://github.com/abeaumont/competitive-programming/blob/a24c9b89941a59d344b51dc1010de66522b1a0dd/kattis/almostsorted2.cc#L19C7-L19C7))

# What went wrong

The judge solution is almost surely incorrect. Through sheer luck, Calle Svensson wrote a solution that has the same bug as the judge solution. It can be found in realac/zetatwo.py

The primary test case illustrating the issue is:

4

5 5 2 7

For which zetatwo.py says "No", even though you can reverse a prefix to get 2 5 5 7. It is very likely that the judge solution has the exact same bug, where it can't handle a prefix of the same number needing to be reversed.


## Not a statement bug

We also considered the alternative that the author intended "strictly increasing". This would imply that any duplicate number at all results in "No". Submitting a solution that prints "No" if not all numbers are unique yields a wrong answer at test case 5. 

## The proposed solution

Use nwerc1.cpp or nwerc2.cpp as a judge solution, and re-generate the test data. I am of the opinion that we should do a full rejudge, meaning that all incorrect solutions (previously AC) get WA.
