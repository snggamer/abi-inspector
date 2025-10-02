ABI Inspector
Validate and analyze Ethereum ABI files. Prints a summary table (functions/events), basic stats (duplicate selectors), and exits with non‑zero code on errors.

Features
Validate ABI JSON structure and list functions/events.

Show duplicate function signatures/selectors.

Simple CLI with two commands: validate and stats.

Installation
Requires Python 3.10+.

Option A — pipx (recommended):
pipx install .
Option B — pip (editable dev install):
pip install -e .
Usage
Validate ABI and print a summary table:
abi-inspector validate path/to/abi.json
Show basic stats (duplicates, totals):
abi-inspector stats path/to/abi.json
Examples
Input format: standard Solidity ABI JSON (as exported by compilers/block explorers).
Outputs: a Rich table in the terminal and JSON snippets for quick inspection.

Roadmap
Generate Solidity interface from ABI (to-interface).

More checks: events indexing, payable/nonpayable counts, tuple formatting.

Output formats: JSON/CSV.

Contributing
Issues and PRs are welcome. Good first issues:

Add new checks (e.g., overloaded functions report).

Add output formats (CSV/JSON) and flags.

Add tests and GitHub Actions workflow.

License
MIT
