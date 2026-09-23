# zcode-cli-dispatch

- `bin/` holds the executable wrapper; keep its name `zcode-edit`.
- `skills/zcode-cli-dispatch/` holds the Codex skill and its UI metadata.
- `tests/` holds focused standard-library tests for the wrapper.
- Keep credentials, ZCode provider files, session databases, caches, and generated output out of this repository.
- After changes, run `python3 -m unittest discover -s tests -v` and validate the skill.
