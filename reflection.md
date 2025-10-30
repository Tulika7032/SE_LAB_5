1. Which issues were the easiest to fix, and which were the hardest?
The easiest issues to fix were formatting and style problems like adding docstrings, removing trailing spaces, and switching to f-strings. These didn’t affect functionality. 
The hardest were handling exceptions and input validation, since they required understanding program logic to avoid breaking the code.

2. Did the static analysis tools report any false positives?
Yes, Pylint flagged function names like addItem and removeItem for not following snake_case. 
While valid by convention, these names were consistent with the original 

3. How would you integrate static analysis tools into your workflow?
I would integrate tools like Pylint, Flake8, and Bandit into both local development and CI pipelines. 
Developers can run them before committing changes, and automated checks can run in CI to catch security or style issues early before deployment.

4. What improvements did you observe after applying fixes?
After the fixes, the code became cleaner, more secure, and easier to maintain. 
Logging replaced prints, specific exceptions improved error handling, and input validation prevented crashes. 
Overall readability and robustness improved noticeably.
