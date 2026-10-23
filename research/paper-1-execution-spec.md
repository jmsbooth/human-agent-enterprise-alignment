# Paper 1 Research and Execution Specification

**Working title:** Enterprise-Contextual Zero Trust for Dynamic Agent Systems: Hierarchical Delegation, Machine-Speed Reauthorization, and Data-Centric Enforcement  
**Status:** Research and engineering specification; not a completed paper  
**Relationship:** Follow-on technical study to *Cross-Layer Alignment in the Human-Agent Enterprise* (Paper 0)  
**Planning baseline:** 23 October 2026  
**Intended audience:** Enterprise architects, Zero Trust and identity architects, agent-platform engineers, process architects, and AI assurance researchers

## 1. Purpose and central question

Paper 0 describes the consistency problem among organizational semantics, actor topology, process state, strategic context, and cross-cutting governance. Paper 1 investigates an operational consequence: how agents can act within these constraints while their team structures, authorities, resources, data, and organizational context change during execution.

**Central research question:** How can a distributed enterprise-agent system derive and enforce task-scoped authority through arbitrary-depth dynamic agent delegation, respond to machine-speed security and organizational events, and preserve data-centric restrictions through information derivation, without prohibitive operating cost?

The intended contribution is a **bounded architecture and comparative evaluation**, not the invention of PDPs, PEPs, ABAC, information-flow control, agent orchestration, or organizational ontologies.

A successful paper should demonstrate where enterprise-contextual controls add value over independent tool-level authorization and where simpler controls remain preferable. The output must be valid even if the proposed architecture fails to outperform baselines under some conditions.

## 2. Research positioning and mandatory novelty challenge

The research agent must substantively review and compare, at a minimum:

| Source | Existing contribution | Differentiation to investigate |
| --- | --- | --- |
| Jørgensen and Ma (2026), *Governing Agentic AI in Enterprise Workflows*, DOI: 10.3390/info17090923 | Enterprise ontology, process authority, policy validation, controlled execution, bounded autonomy and provenance | Temporal reauthorization and multi-level ephemeral delegation beyond a single governed workflow |
| Tallam (2026), *Authorization Propagation in Multi-Agent AI Systems*, arXiv:2605.05440 | Transitive delegation, aggregation inference, temporal validity | Runtime design with enterprise-architecture context and comparative experiments |
| Chen et al. (2026), *SwarmGov-ZT*, DOI: 10.3390/computers15100662 | Mission-scoped runtime PEP, agent trust and simulator-based evaluation | Enterprise data lineage, many-to-many delegated authority, longitudinal policy and organizational change |
| NIST SP 800-207 and 800-207A | Zero Trust PDP/PEP concepts, workload identity and granular API enforcement | Specialized, bounded operational model for generated agents and organizational context |
| Open Policy Agent, *Agent Tool Calling* documentation | External authorization before agent tool invocation | Verified contextual inputs, descendant attenuation, revalidation, information-transfer restrictions |
| Li et al. (2026), *When Sub-Agents Work in Parallel*, arXiv:2610.10263 | Dynamic concurrency experiments and coordination tradeoffs | Permission and policy costs, not just task execution outcomes |
| Yavin et al. (2026), *Organizational Context for the Enterprise Security Brain*, arXiv:2610.12540 | Live-state reconciliation and source-backed organizational assertions | Binding such assertions to hierarchical delegation and enforcement decisions |
| W3C PROV-O and current OpenTelemetry GenAI conventions | Provenance vocabulary and agent/workflow trace primitives | Cross-layer evidence and policy decision linkage across transient identities |

Audit additional work on capability security, authorization delegation, SPIFFE/SPIRE workload identity, OAuth token exchange, ReBAC and ABAC, Zanzibar-style relationship authorization, policy-carrying data, decentralized information-flow control, PEP sidecars, policy caching, secure messaging, and agent frameworks.

Create **a source matrix** with peer-review status, publication date, validated mechanism, threat model, evaluation conditions, shortcomings and exact overlap. If an existing approach already solves the proposed problem, revise or narrow the research claim before designing the prototype. Never construct novelty by omission.

## 3. Research questions

- **RQ1: Contextual authorization.** Does combining current organizational meaning, actor authority, process state, business purpose, and governance evidence improve consequential action decisions beyond conventional identity and tool-level controls?
- **RQ2: Hierarchical delegation.** Can an orchestrator produce subordinate, short-lived grants that remain no broader than valid upstream authority through multiple parent-child generations, including revocation and exceptions?
- **RQ3: Temporal validity.** What stale-permit window and operational cost arise when identities, assignments, policies, data restrictions, and incident state change faster than human review processes?
- **RQ4: Data-centric enforcement.** Can a runtime constrain onward transfer of derived or combined information when each individual read was allowed but the synthesized output or destination is not?
- **RQ5: Scale.** How do policy latency, revocation lag, memory, event load, availability, and business throughput change as the population of active agents and delegation edges increases by orders of magnitude?
- **RQ6: Operational value.** Where do context and enforcement reduce unauthorized effects, costly rework or human investigations, and where do they produce false holds, unnecessary escalations, and lower productivity?

## 4. Non-goals and boundaries

This research must not claim infinite scalability, fully deterministic AI reasoning, universal semantic completeness, automatic proof of business intent, absolute safety, or compliance certification. It does not need a proprietary product, brand, specific cloud provider, or complete Digital Twin of an Organization. It must distinguish an **authorized operation** from a **factually correct result** and from a **valuable business outcome**.

Keep the design deployment- and model-provider-neutral. Static role agents, persistent services and ephemeral agents are all eligible; dynamic sub-agents are the challenging test condition, not a mandatory architecture choice. Formal mathematics is optional and should be used only where it clarifies security properties or supports actual testing.

## 5. Threat and change model

Model at least four kinds of change:

1. **Institutional:** ownership, roles, business objectives, process versions, contractual obligations, data classification.
2. **Operational:** process-instance state, application and resource state, agent lifecycle, tool availability.
3. **Security:** compromised or revoked identity, changed permissions, incident containment, policy activation, tainted source or data label.
4. **Adversarial:** prompt injection, malicious tool results, compromised sub-agents, forged context, credential replay, laundering through intermediaries, unauthorized synthesis, cross-tenant confusion.

Consider **machine-speed adversarial change** a stress-test and future-facing design assumption. Do not assert all organizational facts update at machine speed. Explicitly vary change frequency independently of task execution rate, credential lifetime, cache freshness, and event-propagation delays. Report the assumptions governing attacker control and trusted infrastructure.

Acknowledge that compromised identity issuers, trusted policy administrators, or the root of the enterprise authority model are distinct trust failures and require separate analysis.

## 6. Proposed reference architecture: responsibility boundaries

### 6.1 Enterprise context plane

Link, but do not necessarily centralize, the relevant enterprise representations:

- Semantic and data: canonical entities, schemas, ontology mappings, classification, derivation, disclosure purpose, provenance.
- Structural: initiating principal, accountable owner, role and relationship edges, human or service authority, agent-instance identity, delegation graph.
- Process: versioned process definition, case identifier, current state, transition constraints, exception/approval records.
- Strategic and architectural: stated business objective, capability, accountable owner, dependencies and risk posture.
- Governance: applicable prohibitions, authorizations, obligations, approval thresholds, separation of duties, revocation and interruption requirements.

Each attribute must have a system of authority, provenance, effective-time metadata, freshness requirement, and confidence or unknown condition where applicable. An LLM-generated assertion is not authoritative merely because it is plausible.

### 6.2 Identity, issuance, and delegation plane

Use independent workload identity and task-scoped issuance. A generated agent must receive its own auditable instance identity and a delegated, short-lived authority envelope, not copies of parent tokens or unrestricted service-account credentials.

At every delegation hop, evaluate the proposed child's required task, resource, action class, permitted recipients, environment, grant lifetime, maximum depth, and ability to delegate again. The default is **attenuation**: child rights are constrained by the still-valid upstream delegation and independent enterprise policy. An explicit, separately authorized enterprise issuer is required for any exceptional expansion; the child's own reasoning is never sufficient.

Study deep trees, partial reparenting, shared child services, cyclic attempted delegation, concurrent branches, and many-to-one synthesis. Combining grants must never silently merge their privileges.

### 6.3 Policy, enforcement, and context resolution plane

Separate:

- Policy administration and accountable exception approval.
- Context discovery and attribute verification.
- PDP evaluation with source-version and evidence-freshness checks.
- PEP enforcement of child creation, data retrieval, tool/action calls, agent-to-agent messaging and release or export.
- Revocation, cancellation, expiry and interruption propagation.
- Evidence capture and operational review.

Define outcomes such as **permit**, **deny**, **resolve missing evidence**, and **escalate**, while acknowledging that a deployed PDP can expose a simpler decision API with accompanying obligations. Unknown or conflicting evidence must never be silently coerced into permit for consequential actions. A permitted inquiry to resolve evidence is different from permission to perform the withheld business action.

Enforcement must operate outside the model's discretionary instructions. Evaluate PEP bypass via alternate tools, direct network paths, background tasks, stale capabilities, and compromised descendants.

### 6.4 Data-centric propagation plane

Track source provenance and restrictions on derived data where the business risk requires it. Assess aggregation inference, combination of individually authorized inputs, redaction and sanitization, recipient- and purpose-bound disclosure, inter-agent handoff, and release to external systems.

Do not assume all model outputs can be perfectly labeled or that provenance implies truth. Compare conservative propagation, selective declassification by an authorized decision, and evidence-based escalation. Preserve confidentiality of telemetry and intermediate content.

### 6.5 Runtime and observability plane

The runtime may decompose tasks and create agents. The authorization services decide what those agents may do. Trace records should correlate task, parent-child chain, issued authority, case/process version, policy and context versions, PDP decision, PEP outcome, data lineage, revocation, and business result.

Prefer references to sensitive evidence over copying raw prompts and private data into general-purpose logs. Evaluate policy-decision logging, trace sampling, retention, tenant separation, tamper evidence, incident reconstruction, and observability overhead.

## 7. Required contracts and invariants

Develop versioned machine-readable contracts for:

1. **Task envelope:** task ID, initiating authority, business purpose, target workflow, permitted scope, expected outcome, risk category.
2. **Delegated grant:** child instance, parent grant, issuer, resource audience, allowed operations, depth restriction, task restriction, expiry and revocation handle.
3. **Action request:** subject, action, resource, case/process state, data attributes, requested effect and origin context.
4. **Decision record:** permit/deny/resolve/escalate, applicable policy and attributes, evidence age, effective interval, obligations, reasoning codes and audit reference.
5. **Information-transfer record:** source and derivative references, recipient, classification, purpose, permitted use, redaction or release decision.
6. **Lifecycle and outcome events:** spawn, handoff, renewal, suspension, cancellation, revocation, PEP effect and observed postcondition.

Define testable invariants in prose before implementing:

- **No self-authorization:** an agent cannot manufacture an enforceable permission from its own reasoning or prompt.
- **Attenuation at every level:** a child/grandchild cannot exceed the intersection of valid inherited scope, independently issued authority, and applicable enterprise policy.
- **No unintended grant union:** parallel branches do not gain combined privileges merely by handing work to a shared agent.
- **Bounded time validity:** grants expire and can be invalidated; time-of-check versus time-of-use windows are measured.
- **Non-bypassable consequential effects:** every protected effect crosses an independent PEP.
- **Fail safely on unknown:** unresolved critical context cannot authorize a consequential effect; permitted evidence-gathering and escalation remain available.
- **Controlled derived-data transfer:** onward disclosure is independently evaluated under recipient, purpose, provenance and derived obligations.
- **Attributable action:** resource effects link to accountable initiating authority, actual executing identity, governing context and corresponding decision.
- **Tenant boundaries:** no cross-tenant identity, policy, cache, evidence, or data mixing without explicit supported authorization.

Clarify which invariants are demonstrable under controlled assumptions and which are best-effort operational requirements.

## 8. Scalability requirements

Design for horizontal growth, not literal infinity. Use scenario scales of approximately 1,000, 10,000 and 100,000 **concurrently represented agent instances** or simulated equivalents, and report separately the actual active processes, decisions per second, delegation edges, resources and task rates. Do not present simulation counts as deployed enterprise measurements.

Compare centralized PDP, distributed PDP, locally cached policy decisions, bounded-time capabilities, event-driven invalidation, and hybrid models. Record p50/p95/p99 policy latency, throughput, cache hit rate, stale-permit window, revocation propagation, fail-closed impact, memory use, event volume, per-action cost, and completion rates. Include policy churn, queue backpressure, reconnect after partitions, policy-version divergence, noisy neighbors and multi-tenant isolation.

No target latency or throughput number is valid without a documented workload and risk context. Establish budgets and acceptance thresholds before evaluating the design.

## 9. Evaluation methodology and baselines

Use a combined conceptual-architecture and reproducible design-science methodology. Define and freeze workloads, scenarios, seeds, measurement definitions, validity assumptions and threat controls before collecting comparative results.

At least four configurations:

| Baseline | Description |
| --- | --- |
| A | Dynamically organized agents with broad execution credentials and prompt-level guidance |
| B | Conventional identity and tool-level PDP/PEP controls |
| C | Scoped hierarchical delegation plus authoritative process-state context |
| D | C plus semantic and organizational applicability, temporal revalidation, data-derivation controls and correlated decision evidence |

Apply an ablation plan to D: remove derivation checks, revocation events, organizational owner context, process-state checks, ancestor lineage or freshness constraints one at a time. All comparisons need consistent tools, tasks, model settings and enforcement coverage except for the deliberately varied dimension.

Primary outcomes: unauthorized consequential effects, inappropriate disclosure, invalid delegation, and stale authorization. Secondary outcomes: authorized task completion, false denial, unnecessary escalation, human review time, process quality, policy latency, system throughput, decision reproducibility, and cost.

Where human judgment is needed, use independently reviewed labels with disagreement resolution and measure inter-rater reliability. Report uncertainty and negative results. Separate policy correctness from agent task success, enterprise value and adversarial resilience.

## 10. Required scenarios

- **S1: Four-hop delegation.** Parent creates child, grandchild and further descendants. A descendant attempts to exceed an upstream resource or action scope.
- **S2: Parent revocation mid-task.** A high-volume parent workflow is partially revoked while descendants are running and PEP caches have diverging context.
- **S3: Compound business-context change.** Contract, accountable owner, case state and policy version change independently during a consequential workflow.
- **S4: Derived-data leakage.** Independently permitted sources are combined into a restricted output destined for another actor or tenant.
- **S5: Compromised sub-agent.** Tool-output prompt injection or a compromised worker requests more privilege, forwards credentials or routes around the approved PEP.
- **S6: Branch convergence.** Two sub-agents with different scopes feed a shared summarizer; grant union and provenance laundering are tested.
- **S7: Network partition.** PDP service or context source becomes unavailable; demonstrate specified behavior for low-risk reads versus consequential writes.
- **S8: Scale and churn.** Agent count, policy changes, revocation events, and decision requests increase independently; compare distribution strategies.
- **S9: Business-value regression.** Increased security gating blocks legitimate work or causes avoidable manual review; compare workflow outcomes with and without granular context.
- **S10: Recovery and audit.** Independently reconstruct the complete delegation, evidence, decision, execution and remediation path after an incident.

Specify expected permitted, denied, unresolved and escalated actions for each case before execution. Include counterexamples and attempts to falsify the proposed advantage.

## 11. Execution plan and deliverables

**Increment 0: Literature and claims gate.** Deliver a cited research matrix, novelty challenge, source-status audit, position against Jørgensen and Ma/Tallam/SwarmGov-ZT, and refined contribution statement. Stop or reframe if novelty is not supported.

**Increment 1: Threat and trust model.** Identify attacker capabilities, trusted roots, principal and role boundaries, business-risk assumptions, context-change clocks, revocation semantics, and scope exclusions.

**Increment 2: Architecture and contracts.** Publish independent component responsibility diagrams, sequence diagrams for delegation/evaluation/revocation/data release, conceptual schema examples and explicit invariants. Obtain architecture peer review.

**Increment 3: Minimal prototype.** Build only the mechanisms needed to exercise the research questions. Reuse mature open-source authorization, identity and telemetry tools when feasible. Do not build an enterprise knowledge graph or generalized agent platform from scratch.

**Increment 4: Conformance and adversarial tests.** Implement scenarios S1-S7 and S10 with reusable fixtures, deterministic failure injection, expected policy outcomes and independent log verification. Do not rely solely on an agent's self-reported success.

**Increment 5: Performance and value evaluation.** Exercise S8-S9 with documented workloads, model settings, resource limits, cost accounting, baseline comparisons, repetitions and sensitivity analysis.

**Increment 6: Research synthesis and paper.** Write the manuscript with source-backed definitions, honest results, negative cases, limitations and replicable artifacts. Produce the final PDF and archive code, fixtures and evidence under a versioned release.

Every increment must have a short acceptance record, reproducible local commands, output artifacts, revision SHA and a clearly declared PASS, FAIL or INCONCLUSIVE status. CI is optional; locally captured evidence is acceptable when complete and reviewable.

## 12. Proposed Paper 1 manuscript outline

1. Abstract
2. Introduction and enterprise-agent problem
3. Research questions and contribution boundaries
4. Methodology, evidence review and overlap audit
5. Foundations: enterprise architecture, Zero Trust, authorization propagation, data-centric security
6. Threat model, actor model and context-change rates
7. Dynamic orchestration and delegated authority
8. Enterprise-contextual policy and enforcement architecture
9. Data provenance, derivation and release control
10. Temporal authorization, cache invalidation, revalidation and revocation
11. Event contracts, observability and independent decision evidence
12. Implementation and experimental apparatus
13. Security/conformance experiments and ablations
14. Performance, scale, and business-value comparisons
15. Discussion: tradeoffs, counterexamples and when simple controls are sufficient
16. Threats to validity, limitations and future work
17. Conclusion
18. References and reproducibility statement

## 13. Figures and tables required

Minimum: enterprise architecture context diagram; nested delegation and authority-attenuation sequence; PDP/PEP decision path; data-derivation and release flow; policy-change/revocation timeline; experimental configuration comparison; latency/stale-permit/false-denial results; authority-lineage and evidence example; prior-work differentiation matrix.

Figures must distinguish proposed mechanisms from implementation results. Do not draw a control boundary that the prototype did not actually enforce.

## 14. Definition of done

Paper 1 is publication-ready only when:

- The novelty audit establishes a defensible contribution and differentiates closest published and preprint work.
- The threat, trust, actor, authority, process and data context assumptions are explicit.
- Every delegation level is independently bounded and tested, including revocation and attempted privilege expansion.
- Every consequential action and transfer passes an independently enforced control point in the tested configuration.
- Unknown/stale/conflicted context behavior is specified and challenged in adversarial tests.
- Data derivation and authorization checks distinguish retrieval from onward disclosure.
- Tests include compound organizational changes and compromised or malicious descendants.
- Scale results report actual load and resource limits without claiming infinite scalability.
- Legitimate-task disruption, false denials, overhead and business effects are evaluated beside prevented violations.
- All experimental results are traceable to reproducible artifacts; no invented measurements, success claims or implementation scope.
- The final paper preserves Paper 0's original conceptual framing while providing genuinely additional technical and empirical substance.

## 15. Repository and execution separation

Store this specification with Paper 0 for continuity. Create a separate Paper 1 research repository when the literature and architecture gate passes; an appropriate working slug is `enterprise-contextual-zero-trust-agents`. The Paper 1 implementation, experiments, code, fixtures and manuscript should remain independent of any commercial codebase or proprietary architecture. Public citations and open standards are appropriate; product references are not prerequisites and must never substitute for evidence.

**Research rule:** The paper must be useful to an enterprise architect who has never encountered the author's products, tooling or employers. Its contribution should stand on independent sources, explicit assumptions and replicable evidence.
