# Repository workflow

- After each install, commit the resulting repository changes locally and push the commit to the configured GitHub remote before finishing.
- If an install produces no repository changes, report that there is nothing to commit; do not create an empty commit.
- Keep secrets, local user data, and ignored build artifacts out of commits. If a push fails, report the failure and retain the local commit.
