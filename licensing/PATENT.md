# AUGMANITAI Patent Policy

## Patent Grant

All code contributions to AUGMANITAI are licensed under Apache License 2.0, which includes an **express patent grant** (Section 3 of the Apache 2.0 license). This means:

1. Every contributor who commits code to AUGMANITAI automatically grants a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable patent license covering any patent claims they own that are necessarily infringed by their contribution.

2. This patent license extends to all users and redistributors of AUGMANITAI.

3. If any entity initiates patent litigation against AUGMANITAI or any of its contributors alleging that the software constitutes direct or contributory patent infringement, the patent licenses granted to that entity under Apache 2.0 terminate as of the date of filing. This is a defensive termination clause designed to discourage patent attacks on the project.

## Patent Non-Assertion by the Maintainer

Andreas Ehstand, as the lead maintainer and primary copyright holder, hereby declares:

> I hold no patents relevant to the AUGMANITAI project as of the v1.0 release. Should I or any future corporate entity I am associated with be granted patents that read on AUGMANITAI code or data, I commit to:
>
> 1. Not asserting such patents against any user, redistributor, or contributor of AUGMANITAI, provided they comply with the project's license terms.
> 2. Licensing such patents under the same terms as the Apache 2.0 patent grant for the purpose of AUGMANITAI use.
> 3. Publishing any such patents in the project's `PATENT-DISCLOSURE.md` (to be created if the situation arises).

This declaration is a **unilateral non-assertion commitment**, binding upon the maintainer and his successors in interest with respect to AUGMANITAI.

## Scope

This patent policy applies to:

- The AUGMANITAI Python package
- The AUGMANITAI NPM package
- The MCP/A2A/ANP/AG-UI protocol servers
- The API mock
- The SPARQL/SHACL/TBX/JSON-LD generators and validators
- The GraphRAG integration scripts
- All deployment configurations
- Any future code shipped under the AUGMANITAI name

It does NOT apply to:

- Third-party dependencies (which have their own patent policies)
- Derived works that combine AUGMANITAI with other patented technology (where the derived work's patent status depends on the combiner, not AUGMANITAI)
- Use of AUGMANITAI terminology *concepts* in ways that are independent of the code (the terminology data is governed by CC BY-NC-ND 4.0, not Apache 2.0, and the data license does not include a patent grant)

## What This Means for Downstream Users

If you use AUGMANITAI code in your own project (commercial or non-commercial), you are protected by:

1. The Apache 2.0 patent grant from all contributors
2. The unilateral non-assertion from the lead maintainer
3. The defensive termination clause against anyone who sues the project

This is the same protection profile as other major Apache-licensed projects (Kubernetes, Kafka, Spark, etc.).

## What This Means for Contributors

By contributing code under the project's CLA or DCO, you confirm:

1. You have the right to grant the Apache 2.0 patent license for your contribution.
2. Your employer (if applicable) has authorized you to make patent-granting contributions, OR you are contributing on your own time outside any employer claims.
3. You are not aware of any patent claims by third parties that your contribution would infringe. If you become aware of such claims later, you agree to notify the maintainer.

If you discover that your employer holds a patent that reads on your contribution, please raise this with the project maintainer BEFORE submitting — do not contribute code that would create a patent risk for downstream users.

## Patent Disclosures

If any contributor or maintainer becomes aware of a third-party patent that reads on AUGMANITAI, they should:

1. Not publicly discuss the patent until the project has had a chance to review.
2. Contact the maintainer privately via the channel in `../governance/SECURITY.md`.
3. Provide:
   - The patent number and jurisdiction
   - The specific claims they believe read on AUGMANITAI
   - Any prior art they are aware of
   - Their assessment of whether the claim is avoidable

The maintainer will:

1. Evaluate the disclosure with legal counsel if needed
2. Determine whether to modify the code to avoid the claim
3. Seek a license or design-around if modification is not feasible
4. Publicly disclose the patent in `PATENT-DISCLOSURE.md` once a mitigation plan is in place

## Contact

For patent-related questions, see the private contact channel in `../governance/SECURITY.md`. Do NOT use public issue trackers for patent disclosures.


---

*Bound by the **Ethical Disclaimer §1–§20** ([`DISCLAIMER.md`](../DISCLAIMER.md)) and the repository licenses ([`LICENSE`](../LICENSE)). Contact and provider: [`IMPRESSUM.md`](../IMPRESSUM.md).*
