# AUGMANITAI Licensing

This directory contains all licensing-related files for the AUGMANITAI project. AUGMANITAI uses a **dual-license** model: terminology data under CC BY-NC-ND 4.0, code under Apache 2.0.

## Quick Reference

**Data license:** `CC-BY-NC-ND-4.0` → see `LICENSE-data`
**Code license:** `Apache-2.0` → see `LICENSE-code-apache`
**Alternative code license:** `MIT` (for selected utility files) → see `LICENSE-code-mit`
**Combined SPDX expression:** `CC-BY-NC-ND-4.0 AND Apache-2.0`

For the full explanation of why dual-licensing, what is allowed, and how to attribute, read `LICENSE-summary.md`.

## File Index

| File | Purpose |
| --- | --- |
| `LICENSE-data` | Summary and application of CC BY-NC-ND 4.0 to AUGMANITAI terminology data |
| `LICENSE-code-apache` | Summary and application of Apache 2.0 to AUGMANITAI code |
| `LICENSE-code-mit` | Alternative MIT license for utility files |
| `LICENSE-summary.md` | Substantive dual-license explanation and commercial-licensing contact |
| `SPDX.yml` | SPDX 2.3 document describing the whole project |
| `PATENT.md` | Patent policy and non-assertion commitment |
| `TRADEMARK.md` | AUGMANITAI trademark usage policy |
| `NOTICE` | Combined NOTICE file for redistribution |
| `fetch_licenses.sh` | Helper script to download canonical license texts |

## Canonical License Texts

The files `LICENSE-data`, `LICENSE-code-apache`, and `LICENSE-code-mit` in this directory contain the **application of** each license to AUGMANITAI, along with a summary of your rights. The **legally binding canonical text** of each license is maintained by its publisher and should be fetched from the official source:

- CC BY-NC-ND 4.0: https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode
- Apache 2.0: https://www.apache.org/licenses/LICENSE-2.0.txt
- MIT: https://opensource.org/license/mit

Run `./fetch_licenses.sh` to download these and save them as:
- `LICENSE-data-canonical.txt`
- `LICENSE-code-apache-canonical.txt`
- `LICENSE-code-mit-canonical.txt`

These canonical files should be committed alongside the summary files when preparing a release.

## How the Dual-License Works in Practice

### If you are a user
- Read `LICENSE-summary.md` first. It explains what you can and cannot do.
- If you use AUGMANITAI in research or an open-source tool, you are almost certainly fine under the existing licenses.
- If you want to use AUGMANITAI in a commercial product, contact the maintainer for a commercial license.

### If you are a contributor
- Read `../governance/CLA.md` or `../governance/DCO.md`.
- Your code contributions are licensed under Apache 2.0.
- Your terminology contributions are licensed under CC BY-NC-ND 4.0.
- You retain copyright; the CLA grants a license to the project.

### If you are packaging AUGMANITAI for redistribution
- Include `NOTICE`, `LICENSE-data`, `LICENSE-code-apache`, and canonical license texts in your package.
- Preserve the copyright and attribution headers in source files.
- If you modify code, mark your changes and keep the original notices.

## Commercial Licensing

See the "Commercial Licensing" section of `LICENSE-summary.md` for how to contact the maintainer about a commercial license.

## Questions

- Public questions: open a GitHub Issue with the `licensing` label
- Private or commercial inquiries: use the contact channel in `../governance/SECURITY.md`


---

*Bound by the **Ethical Disclaimer §1–§20** ([`DISCLAIMER.md`](../DISCLAIMER.md)) and the repository licenses ([`LICENSE`](../LICENSE)). Contact and provider: [`IMPRESSUM.md`](../IMPRESSUM.md).*
