# Workspace Agent Rules

## Git Push Protocol
- **CRITICAL MANDATORY RULE**: NEVER execute `git push` or push changes to any remote Git repository (GitHub/GitLab/etc.) without explicit, unambiguous user instructions in the conversation (e.g., the user explicitly typing "push to git", "push to github", "run git push").
- You may build, format, test, and commit changes locally if requested, but **NEVER run `git push` autonomously**.
- Always wait for exclusive user instructions before running any git push operation.
