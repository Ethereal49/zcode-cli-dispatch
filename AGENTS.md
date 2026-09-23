# zcode-cli-dispatch

- `skills/zcode-cli-dispatch/` holds the self-contained Codex skill, UI metadata, and executable `scripts/zcode-edit`.
- `tests/` holds focused standard-library tests for the wrapper.
- Keep credentials, ZCode provider files, session databases, caches, and generated output out of this repository.
- After changes, run `python3 -m unittest discover -s tests -v` and validate the skill.
