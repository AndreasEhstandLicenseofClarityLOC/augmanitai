# AUGMANITAI Governance Model

This document describes the governance structure, decision-making processes, roles, and conflict resolution mechanisms for the AUGMANITAI project.

## Vision

AUGMANITAI is a community-driven, open-source terminology database designed to serve the global academic community. Our governance model balances the need for clear direction and accountability with inclusive, transparent decision-making that respects the contributions of our community.

## Governance Structure

### 1. Project Lead (BDFL)

**Current Lead**: Andreas Ehstand (ORCID 0009-0006-3773-7796)

The Project Lead serves as Benevolent Dictator For Life (BDFL) and holds the following responsibilities:

- **Direction Setting**: Sets the strategic direction and long-term vision of the project
- **Final Authority**: Makes final decisions when consensus cannot be reached
- **Dispute Resolution**: Resolves conflicts and disputes within the community
- **Release Authority**: Approves and oversees releases
- **Maintainer Management**: Appoints and manages core maintainers
- **Community Welfare**: Ensures the project remains healthy, inclusive, and serves its community

The Project Lead commits to:
- Acting in the best interest of the project and community
- Soliciting input from maintainers and community members before major decisions
- Providing transparent reasoning for decisions
- Being open to feedback and willing to change course when evidence warrants

### 2. Core Maintainers

Core maintainers are responsible for:
- **Code/Data Review**: Reviewing and merging pull requests and proposals
- **Quality Assurance**: Ensuring contributions meet project standards
- **Issue Triage**: Categorizing, prioritizing, and responding to issues
- **Community Support**: Helping contributors and answering questions
- **Documentation**: Maintaining and improving project documentation

Current maintainers are listed in [MAINTAINERS.md](MAINTAINERS.md).

**Becoming a Maintainer**:
- Demonstrated history of quality contributions (typically 10+ substantial contributions)
- Nomination by existing maintainer or Project Lead
- Approval by Project Lead
- Commitment to community standards and responsibilities

**Maintainer Responsibilities**:
- Review contributions in a timely manner (within 1-2 weeks)
- Provide constructive, substantive feedback
- Escalate conflicts or complex decisions appropriately
- Mentor newer contributors
- Attend quarterly maintainer meetings (when established)
- Recuse themselves from decisions involving their own contributions

### 3. Steering Committee (Future)

Upon the project reaching greater maturity (targeted for v2.0), a Steering Committee will be established to:
- Provide governance oversight
- Advise on strategic decisions
- Represent different stakeholder groups (academia, industry, community)
- Serve as an appeals body for governance disputes
- Help resolve conflicts the Project Lead cannot

The Steering Committee structure will be defined in a future governance amendment.

### 4. Community

The broader community includes:
- Contributors (those who have submitted contributions)
- Users
- Domain experts who provide feedback
- All people participating in discussions and issues

Community members are encouraged to:
- Provide feedback on proposals and decisions
- Participate in discussions
- Propose new features and improvements
- Help review contributions (even non-maintainers can comment on issues)

## Decision-Making

### Decision Types

Decisions in AUGMANITAI fall into three categories:

#### Type A: Operational Decisions (Low Risk)
- Routine bug fixes
- Documentation improvements
- Minor terminology clarifications
- CI/CD improvements
- **Authority**: Core Maintainers
- **Process**: Direct approval or lazy consensus among maintainers
- **Timeline**: 1-3 days

#### Type B: Substantive Decisions (Medium Risk)
- New major features or functionality
- Significant changes to core terminology structures
- Release versioning and timing
- Addition of new domains or expansion of scope
- **Authority**: Project Lead with input from Core Maintainers
- **Process**: Lazy consensus with 1-week decision window (see below)
- **Timeline**: 1-2 weeks
- **Notification**: Must be announced in project channels

#### Type C: Governance Decisions (High Risk)
- Changes to governance structure
- Changes to licensing
- Fundamental shifts in project direction
- Removal of core maintainers
- Significant policy changes
- **Authority**: Project Lead
- **Process**: Formal consultation with all stakeholders, 2-week decision window
- **Timeline**: 2-4 weeks
- **Notification**: Public announcement with clear rationale

### Lazy Consensus

AUGMANITAI uses a **lazy consensus** decision-making model:

**How It Works**:
1. A proposal is made (usually via GitHub issue or discussion)
2. The proposal is announced to relevant stakeholders (maintainers, community)
3. A decision window is set (typically 7 days for Type B, 14 days for Type C)
4. Anyone can raise objections during this window
5. If no substantive objections are raised, the proposal is approved
6. If objections are raised, discussion continues until consensus is reached or escalation occurs

**Guidelines**:
- Silence is not consent; absence is consent (lazy consensus)
- An objection must be substantive (not "I don't like it" but "because...")
- "Veto" objections must be rare and justified
- Objections should include proposed alternatives
- The Project Lead may override lazy consensus if necessary, but must explain why

### Vote-Based Decisions (When Consensus Fails)

If lazy consensus fails and a decision is still needed:

1. **Formal Vote**: Called by Project Lead
2. **Voters**: Core Maintainers (one vote each)
3. **Threshold**: Simple majority (50% + 1) approves
4. **Appeal**: Project Lead may override vote, but must document reasoning

## Roles and Responsibilities

### Maintainers

**Weekly Responsibilities**:
- Monitor issues and pull requests
- Respond to new contributions within 1-2 business days
- Provide constructive, timely feedback

**Monthly Responsibilities**:
- Contribute to at least one substantive review or discussion
- Assist in triaging and categorizing issues
- Mentor contributors as needed

**As Needed**:
- Participate in governance discussions
- Attend maintainer meetings
- Help resolve conflicts

### Contributors

**Expectations**:
- Follow the Code of Conduct
- Follow contribution guidelines in CONTRIBUTING.md
- Be responsive to maintainer feedback
- Assume good faith in feedback
- Respect project decisions

**Commitments**:
- Provide sufficient context for all proposals
- Respond to feedback within 2 weeks
- Update contributions based on feedback
- Use courteous, professional language

## Decision Timeline Examples

### Example 1: Term Proposal (Type B)

1. **Day 1**: Contributor submits term proposal via GitHub issue with all required information
2. **Day 2-3**: Maintainers triage and verify completeness
3. **Day 3-7**: Domain expert review begins; community feedback invited
4. **Day 7-10**: Discussion period (lazy consensus window opens)
5. **Day 14**: Decision window closes; proposal is approved if no substantive objections
6. **Day 15**: Approved proposal added to queue for next release
7. **Next Release**: Term included in version update

### Example 2: Major Feature Addition (Type B)

1. **Day 1**: Proposal created in GitHub discussions with detailed specification
2. **Day 2-3**: Announcements to community and maintainers
3. **Day 4-7**: Initial discussion and feedback from maintainers
4. **Day 8-14**: Lazy consensus window; objections considered and addressed
5. **Day 15**: Decision made; if approved, implementation planning begins

## Conflict Resolution

### Levels of Conflict Resolution

#### Level 1: Good-Faith Discussion
- Occurs in the relevant GitHub issue or discussion
- All parties participate directly
- Goal: Reach mutual understanding and consensus
- Timeline: 1-2 weeks

#### Level 2: Maintainer Mediation
- If discussion does not resolve the conflict
- A neutral core maintainer (or Project Lead) facilitates discussion
- Focus on finding common ground and compromise
- Timeline: 1-2 weeks

#### Level 3: Project Lead Arbitration
- If mediation fails
- Project Lead reviews all arguments and makes a decision
- Decision is final, but Project Lead provides clear rationale
- Parties have right to appeal (Level 4)
- Timeline: 1 week decision, then implementation

#### Level 4: Appeals Process (Future - Steering Committee)
- Available after v2.0 when Steering Committee is established
- Appeal must be submitted within 2 weeks of Level 3 decision
- Steering Committee reviews and makes final decision
- Decision is binding

### Conflict Types and Resolution

**Disagreement on Term Definition**:
- Resolved by domain expert consensus
- If experts disagree, Project Lead makes final call
- Decision is documented with rationale

**Disagreement on Project Direction**:
- Resolved through governance discussion (Type B or C decision)
- Community input is solicited
- Project Lead makes final decision if consensus cannot be reached

**Interpersonal Conflict or Code of Conduct Violations**:
- Handled confidentially
- Project Lead investigates
- Resolutions may include warnings, temporary suspension, or removal
- See Code of Conduct for details

**Disagreement on Governance Process**:
- Escalated directly to Project Lead
- Project Lead clarifies intent and may modify process
- Can be appealed via future Steering Committee

## Emeritus Status

Contributors and maintainers may transition to **emeritus status** when:
- They can no longer actively participate
- They wish to step down from formal responsibilities
- They remain valued members but cannot commit time

**Benefits of Emeritus Status**:
- Recognition of past contributions
- Continued mention in contributors list
- Consultation on relevant decisions (optional)
- No ongoing responsibilities

**Transitioning Back**:
- Emeritus members can resume active roles
- No formal re-appointment needed
- Just resume participation and responsibilities

## Amendments to This Document

Changes to governance require Type C decisions (see above). Proposed changes should:
- Include rationale for the change
- Include impact analysis
- Be announced 3 weeks before the decision window
- Go through standard lazy consensus process

## Transparency and Accountability

### Record Keeping
- All major decisions are documented with rationale in GitHub issues or discussions
- Maintainer meetings (when established) will have public minutes
- Governance changes will be announced and documented

### Public Visibility
- This governance document is public and version-controlled
- Discussions and decisions are conducted publicly (except confidential matters)
- Conflict resolution processes are transparent unless privacy is required

### Accountability
- Project Lead is accountable to the community and will explain major decisions
- Maintainers are accountable for fair, timely review and decision-making
- Community feedback is solicited regularly
- Annual review of governance effectiveness (when Steering Committee is established)

## Related Documents

- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) — Community standards and enforcement
- [CONTRIBUTING.md](CONTRIBUTING.md) — How to contribute
- [MAINTAINERS.md](MAINTAINERS.md) — Current maintainers and how to become one
- [ROADMAP.md](ROADMAP.md) — Project roadmap and future direction
- [SECURITY.md](SECURITY.md) — Reporting security issues

## Questions?

If you have questions about governance, decision-making, or your role in the project:
- Start a discussion in GitHub Discussions
- Ask in a relevant issue
- Contact the Project Lead directly

---

Last Updated: April 2026  
AUGMANITAI Project Lead: Andreas Ehstand


---

*Bound by the **Ethical Disclaimer §1–§20** ([`DISCLAIMER.md`](../DISCLAIMER.md)) and the repository licenses ([`LICENSE`](../LICENSE)). Contact and provider: [`IMPRESSUM.md`](../IMPRESSUM.md).*
