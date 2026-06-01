"""Commit-msg hook: print a notice when an LLM is listed as a co-author.

Exits 0 (does not block the commit) but prints a visible reminder to
review and understand all AI-generated content before pushing.
"""

import re
import sys

# Patterns covering common LLM co-author signatures
LLM_PATTERNS = [
    r"co-authored-by:.*noreply@anthropic\.com",
    r"co-authored-by:.*claude",
    r"co-authored-by:.*openai\.com",
    r"co-authored-by:.*copilot",
    r"co-authored-by:.*gemini",
]

NOTICE = """
------------------------------------------------------------
LLM CO-AUTHOR NOTICE
------------------------------------------------------------
An AI assistant is listed as a co-author in this commit.

Before pushing, please check:
  1. You have reviewed and understood all AI-generated content.
  2. Any AI-suggested code or text has been tested or verified.
  3. The commit message clearly describes what the AI contributed.

For guidance, see: docs/tracks/07-llm-practices/index.md
------------------------------------------------------------
"""


def main() -> None:
    commit_msg_file = sys.argv[1]
    with open(commit_msg_file) as f:
        msg = f.read()

    for pattern in LLM_PATTERNS:
        if re.search(pattern, msg, re.IGNORECASE):
            print(NOTICE)
            break


if __name__ == "__main__":
    main()
