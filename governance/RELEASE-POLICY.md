# AUGMANITAI Release Policy

This document describes how AUGMANITAI releases are planned, assembled, tested, and published.

## Release Cadence

- **PATCH:** as needed, when a bug or typo fix is ready
- **MINOR:** roughly quarterly, aligned with term-proposal review cycles
- **MAJOR:** roughly yearly or when breaking changes have accumulated

These are targets, not commitments. A MAJOR release will not be cut just because a year has passed if there is nothing worth breaking.

## Long-Term Support (LTS)

LTS status is aspirational for v1.0 since the project is young. Starting with v2.0, each MAJOR version will receive security and correctness patches for at least 12 months after the next MAJOR ships.

## Release Assembly

The release process is managed through a `RELEASE_CHECKLIST.md` template that is filed as a GitHub Issue at the start of every release. Key steps:

### Pre-release

1. **Freeze** — no new feature merges; only bug fixes and release-prep changes
2. **Changelog** — update `CHANGELOG.md` with all changes since the last release
3. **Version bump** — update version strings in:
   - `augmanitai-python/pyproject.toml`
   - `augmanitai-npm/package.json`
   - `augmanitai-ontology.ttl` (the `owl:versionInfo` literal)
   - `handbook/AUGMANITAI_HANDBOOK.md` header
   - `README.md` badges
4. **Regenerate** — run all export generators to refresh derived files:
   - JSON exports
   - TBX exports
   - SKOS-XL exports
   - JSON-LD
   - GraphRAG variants
   - llms.txt and llms-full.txt
5. **Validate** — run the full validation suite:
   - SHACL shapes on the ontology
   - JSON Schema on terms.json
   - Unit tests for Python and NPM packages
   - Integration tests for MCP/A2A/ANP/AG-UI bridges
   - Link checker on all README files
6. **Build** — build sdists, wheels, NPM tarballs, Docker images
7. **Sign** — GPG-sign the git tag; Sigstore-sign the artifacts
8. **Stage** — publish to a staging Zenodo deposit (private draft) and test PyPI (optional)

### Release

9. **Tag** — `git tag -s v1.2.3 -m "Release 1.2.3"` and push
10. **Publish** — upload to Zenodo, PyPI, NPM, Docker Hub (or GHCR), DockerHub
11. **GitHub Release** — create the release with the changelog section and signed artifacts
12. **Announce** — blog post, mailing list, social channels, academic mailing lists for MAJOR releases

### Post-release

13. **Bump to next dev version** — `1.2.4-dev` on main
14. **Watch** — monitor issues for regressions
15. **Retrospective** — for MAJOR releases, write a retrospective

## Hotfix Process

If a critical bug is discovered in a released version:

1. Create a `hotfix/v1.2.x` branch from the v1.2.3 tag
2. Apply the minimal fix
3. Bump to v1.2.4
4. Follow the normal release process, skipping feature freeze
5. Backport to main if the same bug exists there

## Release Approver

Until a Steering Committee is formed, the Lead Maintainer (Andreas Ehstand) is the sole release approver. Once a Steering Committee exists, releases require approval from at least two members.

## Reproducibility

Every release must be reproducible:

- The git commit and tag are the single source of truth for what is in a release
- All derived files are regenerated from source at release time and the generator commands are documented
- Build environments (Docker, GitHub Actions) are pinned to specific versions
- Dependencies are pinned via lockfiles (`poetry.lock`, `package-lock.json`)

## Withdrawal Policy

If a release is found to contain a severe error (incorrect terminology, security vulnerability, CLA violation, etc.) that cannot be fixed by a patch release within a reasonable time, the release may be **withdrawn**:

- PyPI/NPM packages are yanked (but not deleted) to prevent new installs
- The Zenodo record is marked with a retraction notice (Zenodo records cannot be deleted, but they can be annotated)
- A replacement release is prepared

Withdrawal is a last resort and requires a public post-mortem.

## Security Releases

Security releases follow a **coordinated disclosure** pattern — see `SECURITY.md`. The fix is developed in private, tested, and released simultaneously with the disclosure advisory.


---

*Bound by the **Ethical Disclaimer §1–§20** ([`DISCLAIMER.md`](../DISCLAIMER.md)) and the repository licenses ([`LICENSE`](../LICENSE)). Contact and provider: [`IMPRESSUM.md`](../IMPRESSUM.md).*
