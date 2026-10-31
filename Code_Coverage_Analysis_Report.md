# Code Coverage Analysis Report — SE Lab 6

**Student:** Aayaan Kamil  
**SRN:** PES2UG24CS017  
**Experiment:** Code and Branch Coverage Analysis  
**Application:** `movie_tickets.py`  
**Test file:** `CodeCoverageTest_movie_tickets_application.py`

## Objective

Measure how many executable statements in the movie-ticket application are exercised by the code-coverage test suite, identify missed statements, and meet the laboratory requirement of at least 90% code coverage.

## Test method and execution

Python 3.x with `pytest` and `coverage` was used. Execute the following commands from the repository root:

```powershell
py -m pip install coverage pytest
py -m coverage run --source=movie_tickets -m pytest CodeCoverageTest_movie_tickets_application.py
py -m coverage report -m
```

The `--source=movie_tickets` option restricts measurement to the application, excluding the test files. The report's `-m` option lists uncovered lines if any exist. No branch measurement is enabled for this stage.

## Observed results

| Metric | Recorded result |
|---|---:|
| Tests collected | 14 |
| Tests passed | 14 |
| Executable application statements (`Stmts`) | 38 |
| Missing statements (`Miss`) | 0 |
| Measured line coverage | **100%** |
| Minimum required by handout | 90% |

**Evidence:** [Code-coverage terminal screenshot](code_coverage.png). This was captured from the student's Windows terminal.

## Test-case coverage analysis

- **`ticket_price()`:** Exercises regular, premium, and recliner seat choices; morning, afternoon, and evening adjustments; weekday and weekend handling; a free ticket for a child under age 3; a child discount; a senior discount; invalid seat errors; and invalid show hours below 0 and above 23.
- **`group_discount()`:** Exercises invalid ticket count, a small group receiving no discount, the 5-ticket discounted tier with student bonus, and the 10-ticket tier without student bonus.
- **`snack_combo()`:** Exercises small, medium, and large/other-size pricing, and both coupon and non-coupon paths.

The code coverage suite was selected to execute every statement, but **100% line coverage alone does not establish that every branch outcome was tested**. Alternate decision outcomes are assessed separately in the branch-coverage report.

## Interpretation

All 38 measured statements executed during the suite, with zero missed lines. Therefore the submission exceeds the stated 90% code-coverage requirement. The source application was not changed to obtain the result. High coverage improves confidence in test reach but does not by itself prove correctness for every possible input.

## Conclusion

**PASS — 100% code (line) coverage, 14/14 tests passed.** No uncovered executable lines were identified in the measured application. See `Branch_Coverage_Analysis_Report.md` for decision/branch coverage.

**Source:** Lab 6: Code and Branch Coverage Analysis, supplied student handout (requirements and evaluation rubric).