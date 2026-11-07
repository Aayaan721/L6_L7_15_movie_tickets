# Branch Coverage Analysis Report — SE Lab 6

**Student:** Aayaan Kamil  
**SRN:** PES2UG24CS017  
**Experiment:** Code and Branch Coverage Analysis  
**Application:** `movie_tickets.py`  
**Test file:** `BranchCoverageTest_movie_tickets_application.py`

## Objective

Measure whether conditional decisions take their required alternative outcomes during testing, identify missing branches, and reach at least 90% branch coverage as specified by the Lab 6 handout.

## Test method and execution

Python 3.x with `pytest` and `coverage` was used. Execute these commands from the repository root:

```powershell
py -m pip install coverage pytest
py -m coverage run --branch --source=movie_tickets -m pytest BranchCoverageTest_movie_tickets_application.py
py -m coverage report -m
```

The `--branch` flag enables branch tracking. `--source=movie_tickets` limits measurement to the application. `BrPart` shows partially covered branch points; the `Missing` column identifies uncovered destinations, if any.

## Observed results

| Metric | Recorded result |
|---|---:|
| Tests collected | 26 |
| Tests passed | 26 |
| Executable application statements (`Stmts`) | 38 |
| Missing statements (`Miss`) | 0 |
| Measured branches (`Branch`) | 28 |
| Partially covered branches (`BrPart`) | 0 |
| Missing branches | 0 |
| Reported combined coverage (`Cover`) | **100%** |
| Branch outcomes covered | **28/28 (100%)** |
| Minimum required by handout | 90% |

**Evidence:** [Branch-coverage terminal screenshot](branch_coverage.png). This was captured from the student's Windows terminal.

## Branch and edge-case analysis

| Application logic | Test scenarios and alternative outcomes |
|---|---|
| Seat validation | Valid seat proceeds; unknown seat raises `ValueError` |
| Show-hour validation | Hours 0–23 proceed; negative hour and 24 raise `ValueError` |
| Time-of-day decision | Before noon discount; noon/afternoon unchanged; 18:00 onward evening surcharge |
| Weekend decision | Weekend surcharge applied; weekday surcharge absent |
| Age decision | Under 3 is free; ages 3–12 half-price; 13–59 normal price; 60+ half-price |
| Group count validation | Positive ticket count proceeds; zero/negative count raises `ValueError` |
| Group quantity tiers | 1–4 no discount; 5–9 gets 10%; 10+ gets 15% |
| Student bonus | Eligible discounted student group receives extra 5%; nonstudent/no-discount group does not |
| Snack size | Small, medium, and else/large price paths |
| Coupon decision | Coupon reduces snack cost; no coupon keeps original price |

The 26 parameterized test instances exercise both true and false outcomes across the decision logic, as confirmed by zero missing/partial branches in the coverage report.

## Interpretation

With branch measurement enabled, all 28 measured branch outcomes are executed. The zero `BrPart` and missing-branch counts demonstrate that no measured branch outcome was left untested. This is stronger than line coverage alone: a program can execute a conditional line without visiting both paths. Branch coverage still does not guarantee every combination of inputs or all possible execution paths has been tested.

## Conclusion

**PASS — 100% branch coverage (28/28), 26/26 tests passed.** No untested measured branch outcomes were identified; the application source remained unchanged. Both the stated 90% branch target and the rubric's greater-than-90% criterion are met.

**Source:** Lab 6: Code and Branch Coverage Analysis, supplied student handout (requirements and evaluation rubric).