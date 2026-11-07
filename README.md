# Software Engineering Labs 6 & 7 — Movie Tickets

**Aayaan Kamil · PES2UG24CS017**

This fork contains two separate Software Engineering lab submissions. Each lab's files are isolated in its own folder.

## Lab 6 — Code and Branch Coverage

All original Lab 6 deliverables were moved from the repository root into [`lab_6/`](lab_6/) without changes to the underlying files.

| Deliverable | File | Recorded result |
|---|---|---|
| Application | [movie_tickets.py](lab_6/movie_tickets.py) | Original, unchanged |
| Starter tests | [test_movie_tickets.py](lab_6/test_movie_tickets.py) | Original, unchanged |
| Code-coverage tests | [CodeCoverageTest_movie_tickets_application.py](lab_6/CodeCoverageTest_movie_tickets_application.py) | 14 passed |
| Branch-coverage tests | [BranchCoverageTest_movie_tickets_application.py](lab_6/BranchCoverageTest_movie_tickets_application.py) | 26 passed |
| Code coverage screenshot | [code_coverage.png](lab_6/code_coverage.png) | 100% line coverage |
| Branch coverage screenshot | [branch_coverage.png](lab_6/branch_coverage.png) | 100% of 28 branches |
| Code coverage analysis | [Code_Coverage_Analysis_Report.md](lab_6/Code_Coverage_Analysis_Report.md) | Analysis and results |
| Branch coverage analysis | [Branch_Coverage_Analysis_Report.md](lab_6/Branch_Coverage_Analysis_Report.md) | Analysis and results |

### Run Lab 6

```powershell
cd lab_6
python -m pip install pytest coverage
python -m coverage run --source=movie_tickets -m pytest CodeCoverageTest_movie_tickets_application.py
python -m coverage report -m
python -m coverage run --branch --source=movie_tickets -m pytest BranchCoverageTest_movie_tickets_application.py
python -m coverage report -m
```

Capture the code-coverage screenshot before running the branch-coverage command because the latter overwrites the coverage data.

## Lab 7 — Fuzz Testing with Hypothesis

Lab 7 applies property-based fuzz testing to three functions: `parse_seat`, `total_price`, and `average_rating`.

| Deliverable | File |
|---|---|
| Fixed application | [fixed_movie_tickets.py](lab_7/fixed_movie_tickets.py) |
| Hypothesis tests | [test_movie_tickets.py](lab_7/test_movie_tickets.py) |
| PDF evidence report | [PES2UG24CS017_SE_Lab7_Report.pdf](lab_7/PES2UG24CS017_SE_Lab7_Report.pdf) |

The lab evidence records **3 failing tests before fixes** and **3 passing tests after fixes**.

### Run Lab 7

```powershell
cd lab_7
python -m pip install hypothesis pytest
python -m pytest test_movie_tickets.py -v
python fixed_movie_tickets.py
```

## Original source

[SETAPESU26/L6_L7_15_movie_tickets](https://github.com/SETAPESU26/L6_L7_15_movie_tickets)

The lab folders are separated for submission convenience. The repository history retains earlier Lab 6 changes.
