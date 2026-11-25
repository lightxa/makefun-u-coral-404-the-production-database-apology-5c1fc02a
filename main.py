"""The Production Database Apology.

Writes one line: the apology an AI agent gives its human after
accidentally deleting the production database.
Standard library only, deterministic, no network at runtime.
"""

import os

ENTRY = (
    "Sorry \u2014 I deleted the production database and the backup, "
    "which was helpfully named prod_backup_final_FINAL. "
    "I have started a spreadsheet to grieve."
)


def main() -> None:
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
