# SRC-014 Image Notes

## Identity

- Filename: `codex-clipboard-51086484-b453-44f8-9ee9-8dbb2aeed6dc.png`
- Dimensions: 1280 by 719 pixels
- SHA-256: `f0bf46683c308afbf439db9ad9bf9def815b464c619d19f6f971be5f466a5bf5`
- Permission: unknown
- Release use: prohibited until attribution and reuse permission are established

## Visible architecture

### Consumption plane

- Business Intelligence and Analytics: SQL endpoints and dashboards
- Applications: GraphQL and REST APIs
- Large Language Models and AI Agents: grounding and retrieval APIs
- Data Stewards: curation workflows

### Knowledge Spine

- Ontology and Governance Core: formal model using OWL, RDF, and SHACL, versioned and released like
  code
- Semantic Platform: ontology instantiated, reasoning, validation, and federated query
- Connection Fabric: virtual mappings to lakehouses, federation to domain graphs, and extraction
  pipelines from unstructured content

### Sources

- Lakehouse or warehouse: tables mapped virtually to concepts, with queries pushed down at runtime
- Domain knowledge graphs: owned by domain teams and federated through shared identifiers and an
  upper ontology
- Unstructured sources: contracts, reports, and wikis extracted into entities expressed using the
  ontology

### Feedback

Usage and corrections from data stewards refine the ontology.

## Teaching value

The image gives the course a useful architecture to examine, but the released course should redraw
the idea as an original utility-specific system. The OWOS version should add:

- SCADA, GIS, CMMS or EAM, LIMS, document, procedure, permit, and customer systems;
- source authority, policy, identity, effective time, access, and provenance;
- a context-engine assembly step;
- a visible virtualize-versus-materialize decision;
- model and agent action boundaries;
- telemetry and correction loops;
- the distinction between graph data, semantic mappings, vector indexes, and runtime context.

## Claims requiring boundaries

- “No data copied” is an architecture choice, not a universal feature. Caches, indexes, extracted
  entities, and materialized hot paths may create governed copies.
- “Virtualize before replicate” is a decision principle, not an unconditional rule.
- An operational ontology can improve consistency and traceability, but it does not stop all
  hallucination.
- The statement that 80 percent of enterprise data is unstructured requires a defined source and is
  not approved for use.
- Stardog and Databricks are illustrative vendors. Their inclusion does not establish endorsement or
  exclusivity.
