"""Explore the paper's cross-layer mismatch catalog.

This module is deliberately not a validator, safety calculator, statistical
model, or source of empirical evidence. It serializes a small, reviewable
catalog so that the conceptual categories can be discussed, filtered, and
replaced by future data-backed analyses.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Optional, Tuple


MISMATCH_TYPES = (
    "semantic_process",
    "structural_governance",
    "process_topology",
    "strategic_process",
    "semantic_governance",
    "observed_prescribed",
    "authorized_observed_topology",
    "process_governance",
    "semantic_structural",
    "architecture_ownership",
    "strategic_granted_autonomy",
)

STATUSES = ("alignment", "misalignment", "unknown")

STATUS_DEFINITIONS = {
    "alignment": (
        "Evidence indicates that the relevant representations agree or are "
        "compatible for the bounded task."
    ),
    "misalignment": (
        "Evidence indicates that relevant representations conflict, omit a "
        "required constraint, or authorize and enact incompatible behavior."
    ),
    "unknown": (
        "Evidence is too incomplete, stale, ambiguous, or contradictory to "
        "determine whether the representations agree."
    ),
}


@dataclass(frozen=True)
class MismatchCase:
    """A qualitative case template for examining one mismatch relation."""

    case_id: str
    mismatch_type: str
    representations_compared: str
    disagreement: str
    possible_evidence: str
    potential_consequence: str
    caveat: str
    status: str = "unknown"

    def __post_init__(self) -> None:
        for field_name, value in asdict(self).items():
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{field_name} must be a non-empty string")
        if self.mismatch_type not in MISMATCH_TYPES:
            raise ValueError(f"unsupported mismatch_type: {self.mismatch_type}")
        if self.status not in STATUSES:
            raise ValueError(f"unsupported status: {self.status}")


def catalog() -> Tuple[MismatchCase, ...]:
    """Return the paper's qualitative mismatch catalog.

    The default status is unknown because the catalog contains no
    organization-specific evidence. Callers may construct status-labeled
    cases after supplying an explicit evidence basis.
    """

    return (
        MismatchCase(
            "MM-01",
            "semantic_process",
            "semantic foundation and process representation",
            "A resolved case has different meanings in the domain vocabulary and process state model.",
            "Mapping review, definitions, provenance, and state-transition traces.",
            "Wrong routing or invalid completion.",
            "A vocabulary difference may be a deliberate local variant; stale definitions require review.",
        ),
        MismatchCase(
            "MM-02",
            "structural_governance",
            "actor topology and governance plane",
            "A role is responsible for a decision, but permissions grant the action to another principal.",
            "Role, responsibility, identity, permission, and delegation records.",
            "Accountability gaps or unauthorized action.",
            "Shared-service design or temporary delegation may explain the difference.",
        ),
        MismatchCase(
            "MM-03",
            "process_topology",
            "process representation and actor topology",
            "A prescribed human review is enacted by an agent without recorded delegated authority.",
            "Event, identity, handoff, and authorization traces.",
            "Hidden responsibility transfer.",
            "Missing telemetry establishes an observability limitation, not necessarily a breach.",
        ),
        MismatchCase(
            "MM-04",
            "strategic_process",
            "strategic intent and process representation",
            "A local optimization removes an escalation step treated as mandatory by enterprise risk policy.",
            "Objective traceability, policy priorities, process variants, and change records.",
            "Strategic drift or risk exposure.",
            "Objectives can conflict or change over time.",
        ),
        MismatchCase(
            "MM-05",
            "semantic_governance",
            "semantic foundation and governance plane",
            "Sensitive customer data has different definitions in a data ontology and access policy.",
            "Term mappings, policy versions, classifications, and policy decisions.",
            "Improper access.",
            "A definition conflict may remain unresolved until the scope and versions are checked.",
        ),
        MismatchCase(
            "MM-06",
            "observed_prescribed",
            "effective work and prescribed process or topology",
            "Informal escalation is routine but absent from the process model or ownership record.",
            "Event and communication evidence, model comparison, and interviews.",
            "Hidden exception handling or process debt.",
            "The difference may be safe adaptation, tacit knowledge, or governance failure.",
        ),
        MismatchCase(
            "MM-07",
            "authorized_observed_topology",
            "authorized topology and observed topology",
            "A service account executes cross-boundary actions absent from the authorized delegation path.",
            "Runtime identities, delegation chains, interaction logs, and tool traces.",
            "Unauthorized edges or enlarged incident scope.",
            "Identity-correlation errors can leave the status unknown.",
        ),
        MismatchCase(
            "MM-08",
            "process_governance",
            "process representation and governance plane",
            "A process step permits an action that a current prohibition or approval rule disallows.",
            "Process versions, policy decisions, approval records, and enforcement points.",
            "Blocked work or prohibited execution.",
            "A stale process repository can explain the discrepancy.",
        ),
        MismatchCase(
            "MM-09",
            "semantic_structural",
            "semantic foundation and actor topology",
            "The case-owner concept maps to a service account rather than the accountable team role.",
            "Entity and role mappings, ownership records, and task assignments.",
            "Ownership ambiguity.",
            "Terminology variation alone is not misalignment.",
        ),
        MismatchCase(
            "MM-10",
            "architecture_ownership",
            "enterprise architecture and organizational ownership",
            "A system dependency is owned by a platform team while the operating model assigns the capability to a product team.",
            "Architecture repositories, service catalogs, capability maps, and operating-model records.",
            "Unowned changes or incident handoff failure.",
            "A transitional reorganization can be intentional.",
        ),
        MismatchCase(
            "MM-11",
            "strategic_granted_autonomy",
            "strategic intent and granted autonomy",
            "An agent receives broad write authority for work whose risk posture requires human approval and reversibility.",
            "Autonomy decisions, permissions, risk appetite, approval gates, and revocation tests.",
            "Inappropriate exposure.",
            "Technical capability is not evidence of strategic authorization.",
        ),
    )


def filter_cases(
    cases: Iterable[MismatchCase],
    mismatch_type: Optional[str] = None,
    status: Optional[str] = None,
) -> Tuple[MismatchCase, ...]:
    """Filter cases without assigning or inferring a research result."""

    if mismatch_type is not None and mismatch_type not in MISMATCH_TYPES:
        raise ValueError(f"unsupported mismatch_type: {mismatch_type}")
    if status is not None and status not in STATUSES:
        raise ValueError(f"unsupported status: {status}")
    return tuple(
        case
        for case in cases
        if (mismatch_type is None or case.mismatch_type == mismatch_type)
        and (status is None or case.status == status)
    )


def summarize(cases: Optional[Iterable[MismatchCase]] = None) -> dict:
    """Return a JSON-ready qualitative summary of the supplied cases."""

    selected = tuple(catalog() if cases is None else cases)
    counts = {status: 0 for status in STATUSES}
    for case in selected:
        if not isinstance(case, MismatchCase):
            raise TypeError("cases must contain MismatchCase instances")
        counts[case.status] += 1
    return {
        "tool_status": "exploratory research tooling",
        "evidence_note": (
            "Catalog entries are conceptual case templates, not empirical "
            "evidence, validation results, or a universal alignment score."
        ),
        "status_definitions": STATUS_DEFINITIONS,
        "counts_by_status": counts,
        "mismatch_cases": [asdict(case) for case in selected],
    }


def main(argv: Optional[Iterable[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Serialize the exploratory cross-layer mismatch catalog."
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("build/mismatch-exploration.json"),
        help="JSON output path (default: build/mismatch-exploration.json)",
    )
    args = parser.parse_args(list(argv) if argv is not None else None)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(summarize(), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"wrote exploratory mismatch catalog to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
