REM activate the project virtual environment and start running all the tests from the testCases directory and save the report to the reports directory
start venv\Scripts\activate & python -m pytest "testCases" --html=./reports/latest_run_report.html

