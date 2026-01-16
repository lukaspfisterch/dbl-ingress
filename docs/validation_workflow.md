# Validation against dbl-reference

Goal: validate invariants and replay equivalence for streams that include
ingress-admitted inputs.

## Inputs

Export the gateway event stream (JSONL) produced from ingress-admitted requests:
- One JSON object per line.
- Required keys: `event_id`, `kind`, `correlation_id`, `payload`.

## Validate invariants

```bash
cat events.jsonl | dbl-reference --mode validate
```

- Exit code 0: OK.
- Non-zero: invariant or replay failure (see stderr).

## Normative digest

```bash
cat events.jsonl | dbl-reference --mode replay --digest
```

Compare digests across systems to assert normative equivalence.
