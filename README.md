# dbl-ingress

[![CI](https://github.com/lukaspfisterch/dbl-ingress/actions/workflows/ci.yml/badge.svg)](https://github.com/lukaspfisterch/dbl-ingress/actions/workflows/ci.yml)
[![PyPI version](https://img.shields.io/pypi/v/dbl-ingress.svg)](https://pypi.org/project/dbl-ingress/)
[![Python 3.11 | 3.12](https://img.shields.io/badge/python-3.11%20%7C%203.12-blue.svg)](https://www.python.org/downloads/)

`dbl-ingress` provides the admission and input-shaping layer for DBL-based systems. Its role is to ensure that all external inputs entering a DBL boundary are well-formed, typed, and deterministic before they reach the core event logic.

## Scope

- **Admission**: validation of incoming data payloads.
- **Shaping**: conversion of raw inputs into typed, immutable records.
- **Invariants**: early enforcement of deterministic constraints (e.g. rejecting floats in deterministic fields).

## Non-Goals

- Execution logic or side effects.
- Policy decisions or complex business rules.
- Network transport or service runtime concerns.
- CLI tools.
- Any form of semantic interpretation beyond structural validation.

## Relation to dbl-core

`dbl-ingress` operates strictly before `dbl-core`. While `dbl-core` is responsible for deterministic event logging and state reconstruction, `dbl-ingress` ensures that all inputs entering the core are structurally valid and safe for deterministic processing.

## Validation against ensdg

See `docs/validation_workflow.md` (ensdg was previously developed under the name "dbl-reference").

## Status

Early-stage, API-stable for current DBL usage. Breaking changes may occur as invariants are refined.
