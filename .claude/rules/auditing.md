# Auditing After Significant Changes

After any significant code change — including refactors, feature additions, API changes, architectural shifts, or removal of functionality — always run both auditor agents without waiting to be asked:

- `docs-auditor` — checks documentation for accuracy and completeness
- `ci-rules-auditor` — checks CI configuration when build rules or build files change

Minor changes (typos, small bug fixes, test-only changes) do not require either auditor.
