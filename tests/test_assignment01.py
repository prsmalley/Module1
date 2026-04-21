import subprocess
import sys

def run_assignment():
    result = subprocess.run(
        [sys.executable, 'assignment01.py'],
        capture_output=True, text=True
    )
    return result.stdout, result.returncode

def test_runs_without_errors():
    _, returncode = run_assignment()
    assert returncode == 0, "Code crashed — check for syntax or runtime errors."

def test_task01_output():
    output, _ = run_assignment()
    assert 'Task 01' in output, "Missing Task 01 print statement."

def test_task02_output():
    output, _ = run_assignment()
    assert 'The amount off is:' in output, "Task 02: amount_off not printed correctly."

def test_task03_output():
    output, _ = run_assignment()
    assert 'The area is:' in output, "Task 03: area not printed correctly."

def test_task04_output():
    output, _ = run_assignment()
    assert 'Task 04' in output, "Missing Task 04 section."

def test_task05_output():
    output, _ = run_assignment()
    assert 'Task 05' in output, "Missing Task 05 section."
    assert 'Weather Report' in output, "Task 05: Weather report not printed."

if __name__ == '__main__':
    tests = [
        test_runs_without_errors,
        test_task01_output,
        test_task02_output,
        test_task03_output,
        test_task04_output,
        test_task05_output,
    ]
    passed = 0
    for test in tests:
        try:
            test()
            print(f"  ✅ PASSED: {test.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"  ❌ FAILED: {test.__name__} — {e}")

    print(f"\n{passed}/{len(tests)} checks passed.")
    if passed < len(tests):
        sys.exit(1)  # Causes the Action to show as failed in GitHub
