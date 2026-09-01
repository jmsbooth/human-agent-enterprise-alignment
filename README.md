# Cross-Layer Alignment in the Human-Agent Enterprise

This repository accompanies a conceptual synthesis and perspective paper on how enterprise meaning, actor responsibility, process behavior, strategic intent, architecture, and governance constraints interact around delegated agent actions.

> Status: structured interdisciplinary conceptual synthesis with exploratory mismatch tooling. This repository does not present a validated mathematical model, universal alignment score, synthetic research result, or production safety assessment.

## Research position

The paper's claim is intentionally bounded:

> Cross-layer alignment is a useful problem boundary for asking whether the representations relevant to a bounded delegated action agree, conflict, or remain unknown across semantic, structural, process, strategic, and governance concerns.

The paper explicitly credits adjacent work. Agentic Business Process Management already connects process-aware agents, goals, normative frames, adaptation, and governance. Semantic BPM, enterprise ontology, Human--AI and Human--Autonomy Teaming, process mining, enterprise architecture, governance, and Digital Twins of Organizations each supply important partial representations. The remaining question is whether their cross-layer relations are useful to compare and how that usefulness should be tested empirically.

The framework keeps four dimensions distinct:

- Semantic foundation: what entities, actions, states, constraints, and commitments mean.
- Actor topology: who participates, who is responsible, who is authorized, who interacts, and where boundaries lie.
- Process representation: how work is prescribed, observed, handed off, varied, and escalated.
- Strategic intent and architecture: why the work matters, what capabilities support it, who owns them, and how dependencies are arranged.

Governance is treated as a cross-cutting constraint plane covering identity, permission, prohibition, obligation, delegation, approval, separation of duties, monitoring, attribution, audit, revocation, interruptibility, and autonomy boundaries.

## Repository map

| Path | Purpose |
| --- | --- |
| paper/main.tex | The manuscript, including the synthesis method, related work, framework, mismatch catalog, propositions, optional DTO substrate, and research agenda. |
| experimental/mismatch_exploration.py | Standard-library exploratory catalog of cross-layer mismatch cases. It is not a validator, score, statistical model, or source of empirical evidence. |
| tests/test_mismatch_exploration.py | Regression tests for catalog coverage, status distinctions, validation, filtering, and JSON serialization. |
| research/revision-evidence.md | Internal evidence, novelty, construct, proposition, and citation audit supporting the revision. |
| Makefile | Reproducible checks, exploratory export, and Tectonic compilation targets. |

The old scalar alignment implementation was removed because its filename, equations, and synthetic outputs conflicted with the revised paper's conceptual scope. The experimental directory is the canonical location for the retained tooling because it makes the non-validating status explicit. A future empirical package should be introduced only after real, versioned, de-identified evidence and a preregistered study design exist.

## Quick start

Requirements:

- Python 3.8 or newer
- Tectonic, or another compatible LaTeX engine exposed through the TECTONIC Make variable

The Makefile points at the bundled Tectonic runtime available in this workspace; override TECTONIC when running elsewhere.

Run the checks and export the qualitative catalog:

~~~sh
make check
~~~

Compile the paper:

~~~sh
make paper
~~~

The PDF is written to build/paper/main.pdf. The exploratory JSON export is written to build/mismatch-exploration.json.

To run the catalog directly:

~~~sh
python3 -m experimental.mismatch_exploration --output build/mismatch-exploration.json
~~~

## Exploratory mismatch tooling

The companion module serializes eleven qualitative mismatch patterns:

- semantic and process representation
- structural and governance representation
- process and actor topology
- strategic intent and process
- semantic and governance representation
- observed and prescribed work
- authorized and observed topology
- process and governance
- semantic and structural representation
- architecture and organizational ownership
- strategic intent and granted autonomy

Every default catalog entry is marked unknown because the repository contains no organization-specific evidence. The status vocabulary is deliberately explicit:

- alignment: evidence indicates compatible representations for the bounded task
- misalignment: evidence indicates conflict, omitted constraints, or incompatible authorization and enactment
- unknown: evidence is too incomplete, stale, ambiguous, or contradictory to determine agreement

Poor observability is not automatically misalignment. The tooling therefore does not infer a result from missing evidence and does not assign a composite score.

## Illustrative use cases

The mismatch catalog is intended to support future case analysis in bounded settings such as:

- claims intake: entity meaning, ownership, exceptions, and approvals
- customer support: service ownership, delegation, handoffs, and escalation
- compliance triage: policy versioning, semantic precision, provenance, and human approval
- incident response: identity, revocation, interruptibility, action traceability, and responsibility

These are research contexts, not observed case studies or claims of measured business impact.

## Optional DTO substrate

The paper discusses a Digital Twin of an Organization as an optional substrate for linking partial, versioned, observable representations. A DTO-like implementation could link semantic entities and provenance, actor identities and authority, prescribed and observed process, enterprise architecture and ownership, policy decisions, and agent action traces.

The framework does not require a DTO. A substrate must not be treated as a complete model of the enterprise, an inference engine for tacit knowledge, or a substitute for identity, access control, privacy, causal study, or domain governance.

## Literature and evidence

The manuscript uses foundational sources, standards, peer-reviewed work, practitioner and governance documents, and recent preprints. Evidence labels are descriptive categories rather than confidence levels, meta-analysis grades, or systematic-review scores. The revision audit records the search date, domains, search terms, inclusion and exclusion logic, source classes, citation chaining, novelty challenges, construct definitions, proposition boundaries, and bibliography corrections.

Important current anchors include [Agentic Business Process Management: A Research Manifesto](https://doi.org/10.1016/j.is.2026.102738), [Agent Miner](https://doi.org/10.1007/978-3-031-41620-0_17), [organizational mining for agent-system discovery](https://doi.org/10.1016/j.is.2025.102669), [the Human--Agent Teaming review](https://aisel.aisnet.org/pacis2025/hci/hci/20/), [organization-design DTO work](https://doi.org/10.1007/s41469-023-00151-z), and the [NIST agent identity and authorization concept paper](https://www.nccoe.nist.gov/sites/default/files/2026-02/accelerating-the-adoption-of-software-and-ai-agent-identity-and-authorization-concept-paper.pdf).

## Research agenda

The next stage is empirical, not another score revision:

1. Test whether the vocabulary improves diagnosis compared with isolated local reviews.
2. Assess inter-rater reliability for alignment, misalignment, and unknown classifications.
3. Identify observable indicators for each dimension from bounded, versioned evidence.
4. Test associations with task correctness, exception resolution, responsibility clarity, calibrated reliance, unauthorized action, auditability, rollback time, or incident scope.
5. Test interaction effects without assuming a predetermined equation.
6. Study boundary conditions, tacit knowledge, adversarial input, stale policies, identity substitution, tool failure, and negative cases.

## Reproducibility and guardrails

- No secrets, credentials, production data, or personal data are required.
- The exploratory export contains conceptual templates only.
- Missing evidence is represented as unknown rather than converted to a negative finding.
- Claims about governance remain bounded by identity, authorization, monitoring, attribution, revocation, and interruption controls.
- New empirical work should use de-identified fixtures, representation versions, provenance, preregistered comparisons, and domain review.

## Showcase artifacts

Build the paper and open the generated PDF from build/paper/main.pdf. The manuscript is designed to stand on its own as the showcase artifact; the Python module exists only to make the mismatch vocabulary inspectable and testable as repository scaffolding.

For the internal revision record, see research/revision-evidence.md.
