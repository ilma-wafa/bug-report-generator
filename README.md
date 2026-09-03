# Bug Report Generator

> A lightweight QA-focused tool for creating structured and professional bug reports.

A simple Streamlit application that helps organize defect information into a consistent bug report format.

This project was built to practice **software testing, defect documentation, test case design, and QA workflow thinking**.

## Live Demo

Try the application:

[**Launch Bug Report Generator**](https://bug-report-generator-2vbb8kzkhyytyryven9bmk.streamlit.app/)

## Application Preview

![Bug Report Generator application preview](Screenshot.png)

## Key Features

- Generate structured bug reports from user-provided defect information
- Capture essential defect details including:
  - Bug title
  - Bug type
  - Severity
  - Steps to reproduce
  - Expected behavior
  - Actual behavior
- Download generated bug reports for further use
- Simple Streamlit-based user interface
- QA-focused test plan covering negative, input validation, boundary, and edge-case scenarios

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Application development and report generation |
| Streamlit | Web application interface |
| Markdown | Test documentation |

## How It Works

1. Enter the relevant bug information in the application.
2. Select the appropriate bug type and severity.
3. Provide the steps to reproduce the issue.
4. Enter the expected and actual behavior.
5. Generate the bug report.
6. Download the generated report for further use.

## QA Testing

Testing for this project focuses on validating user input and identifying potential defects across common and edge-case scenarios.

### Test Coverage

| Test Case | Scenario | Testing Technique |
|-----------|----------|-------------------|
| TC001 | Submit the form with an empty title | Negative Testing |
| TC002 | Submit the form with a spaces-only title | Negative Testing |
| TC003 | Enter special characters in the bug title | Input Validation |
| TC004 | Enter 1000+ characters | Boundary Value Analysis |

### Testing Approach

The test scenarios were selected to cover:

- **Negative Testing** — validating how the application behaves with invalid or missing input
- **Input Validation** — checking how user-provided values are handled
- **Boundary Value Analysis** — testing behavior with unusually large input
- **Edge Cases** — exploring inputs that may expose unexpected application behavior

For the complete test cases and expected results, see the [Test Plan](test_plan.md).

> **Testing status:** Test cases are currently documented in the test plan. Execution results will be added as testing is completed.

## Project Structure

```text
bug-report-generator/
│
├── app.py
├── bug_report_generator.py
├── bug_report_Login_Fail.txt
├── test_plan.md
├── Screenshot.png
└── README.md
