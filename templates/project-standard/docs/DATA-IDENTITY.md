# Data Identity and Duplicate Prevention

The project must have one canonical identity for each real entity that needs to survive edits, imports, retries, merges, routing, or integration with external systems.

## Rules

1. Use stable internal IDs. Do not use display names, titles, email bodies, timestamps, or mutable URLs as the primary identity of durable records.
2. Separate canonical identity from source identity. One canonical record may map to several external/source IDs.
3. Cross-routing should normally use tags, relationships, or views rather than cloning the underlying record.
4. Deduplication decisions must be explainable and auditable.
5. Merges must preserve provenance and redirects/mappings from retired IDs when consumers may still reference them.
6. Retryable write operations should use idempotency keys or equivalent protections when duplicates would be harmful.

## Entity registry

| Entity | Internal stable ID format | Canonical uniqueness rule | Source mapping | Merge behavior | Idempotency/dedupe key |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## Source mappings

When several feeds refer to the same real item, prefer:

```text
canonical_entity
  id: stable internal ID

source_mappings
  canonical_id
  source_system
  source_record_id
  source_url/fingerprint when useful
  first_seen_at
  last_seen_at
```

The exact schema may differ, but the identity boundary should remain explicit.

## Duplicate review

Record:

- exact-match keys;
- normalized-match keys;
- fuzzy-match thresholds if used;
- merge authority;
- false-positive handling;
- audit trail;
- UI for human review when automation is uncertain.

Do not hide a duplicate-generation defect solely by suppressing duplicates in the UI.
