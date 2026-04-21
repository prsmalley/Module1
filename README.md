# Module 1 - Python Basics

## For Students

### Getting Started
1. Accept the assignment invite link provided by your instructor
2. Once your repo is created, click the green **Code** button and select **Open with Codespaces**
3. Wait for the environment to load — Python and all extensions will be set up automatically

### Completing the Assignment
- Open `assignment01.py` and follow the instructions in the comments
- Complete each task in order (Task 01 through Task 05)
- You can run your code at any time by clicking the **Run** button or typing `python assignment01.py` in the terminal

### Submitting
- When you're done, save your file and commit your changes:
  1. Click the **Source Control** icon in the left sidebar (or press `Ctrl+Shift+G`)
  2. Type a commit message (e.g. "completed assignment 01")
  3. Click **Commit**, then **Sync Changes**
- The autograder will run automatically after every push — check the **Actions** tab in your repo to see your results
- You can push as many times as you like before the deadline

---

## For Instructors

### How This Repo Works
- `assignment01.py` — the student-facing template with task instructions and starter code
- `tests/test_assignment01.py` — autograder tests that check each task's output
- `.github/workflows/grade.yml` — GitHub Action that runs on every push to `main`, executes the tests, and posts results as a commit comment
- `.devcontainer/devcontainer.json` — configures the Codespaces environment (Python 3.11, VS Code extensions)

### Setting Up GitHub Classroom
1. Go to [classroom.github.com](https://classroom.github.com) and create a classroom
2. Click **New assignment** and use this repo as the starter code
3. Set visibility to **Private** so students can't see each other's work
4. Enable **Feedback pull requests** if you want a built-in place to leave inline code comments
5. Share the generated invite link with students

### Autograder
The autograder checks that each task produces the expected output. Results are posted automatically as a commit comment after every push. To add or modify checks, edit `tests/test_assignment01.py`.
