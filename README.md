# Software Engineering Lab 6 — Code and Branch Coverage

**Aayaan Kamil · PES2UG24CS017**

This repository root contains all Lab 6 submission deliverables. The original `Lab 6/` nesting has been removed to make the files immediately visible.

| Deliverable | File | Verified result |
|---|---|---|
| Application | [movie_tickets.py](movie_tickets.py) | Original, unchanged |
| Starter tests | [test_movie_tickets.py](test_movie_tickets.py) | Original, unchanged |
| Code-coverage tests | [CodeCoverageTest_movie_tickets_application.py](CodeCoverageTest_movie_tickets_application.py) | 14 passed |
| Branch-coverage tests | [BranchCoverageTest_movie_tickets_application.py](BranchCoverageTest_movie_tickets_application.py) | 26 passed |
| Code-coverage screenshot | [code_coverage.png](code_coverage.png) | 100% line coverage |
| Branch-coverage screenshot | [branch_coverage.png](branch_coverage.png) | 100% of 28 branches |
| Code coverage analysis and report | [Code_Coverage_Analysis_Report.md](Code_Coverage_Analysis_Report.md) | Interpretation, test strategy, results |
| Branch coverage analysis and report | [Branch_Coverage_Analysis_Report.md](Branch_Coverage_Analysis_Report.md) | Branch paths, interpretation, results |

## Run from this repository root (Windows PowerShell)

```powershell
py -m pip install coverage pytest
py -m coverage run --source=movie_tickets -m pytest CodeCoverageTest_movie_tickets_application.py
py -m coverage report -m
py -m coverage run --branch --source=movie_tickets -m pytest BranchCoverageTest_movie_tickets_application.py
py -m coverage report -m
```

Take the code-coverage screenshot before running the branch coverage command, because the second run replaces the earlier coverage measurement.

The original two required coverage commits are preserved in history; this later commit reorganizes the files and adds the optional written analysis reports.
