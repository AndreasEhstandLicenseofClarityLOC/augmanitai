<!--
Thanks for contributing to AUGMANITAI! Please fill out this template so reviewers can evaluate your PR efficiently.
If this PR introduces a new TERM, please ensure you have first opened a Term Proposal issue using the "Term Proposal" template, and link it below.
-->

## Summary

<!-- One or two sentences: what does this PR do? -->

## Type of Change

<!-- Check all that apply -->

- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Documentation only (no code or data change)
- [ ] Terminology addition (new term)
- [ ] Terminology modification (edit to an existing term — requires MAJOR/MINOR analysis)
- [ ] Terminology deprecation (mark a term as deprecated)
- [ ] Tooling / infrastructure change
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)

## Related Issues

<!-- Closes #123, Addresses #456 -->

## Version Impact

<!-- Per VERSIONING.md, is this a PATCH, MINOR, or MAJOR change? -->

- [ ] PATCH (no semantic change)
- [ ] MINOR (additive, backward-compatible)
- [ ] MAJOR (breaking change — requires MIGRATION.md update)

## Checklist

- [ ] I have read `CONTRIBUTING.md`
- [ ] I have signed off my commits with DCO (`git commit -s`) OR have a signed ICLA on file
- [ ] My code follows the project's style guide (black + ruff for Python; prettier + eslint for JS/TS)
- [ ] I have added tests that prove my fix is effective or my feature works
- [ ] New and existing tests pass locally with my changes
- [ ] I have updated the documentation
- [ ] I have updated `CHANGELOG.md` under the `[Unreleased]` section
- [ ] For terminology changes: I have regenerated all derived exports (TTL, JSON-LD, TBX, SKOS-XL)
- [ ] For terminology changes: SHACL validation passes
- [ ] For breaking changes: I have updated `MIGRATION.md` with a copy-pasteable migration path

## Terminology PRs only

<!-- Only fill this section if this PR changes terminology data -->

- [ ] Links to the Term Proposal issue: #
- [ ] Genus and differentia are clearly documented
- [ ] At least 3 ISO 704 characteristics provided
- [ ] At least 2 examples provided
- [ ] Attestation source cited
- [ ] Cross-references to related terms added
- [ ] German translation provided (or explicitly noted as a follow-up)

## Testing

<!-- How did you test this? What commands did you run? -->

```bash
# Example
pytest augmanitai-python/tests/
```

## Screenshots / Output

<!-- Optional: screenshots for UI changes, before/after outputs for CLI changes -->

## Additional Context

<!-- Anything else reviewers should know -->
