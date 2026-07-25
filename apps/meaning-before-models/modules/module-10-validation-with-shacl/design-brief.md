# Module 10 Design Brief: Validation with SHACL

Status: approved for production under standing owner authorization

## Learning decision

The learner must interpret a SHACL validation report, repair the data or route an exception, rerun
validation, and state what conformance does not prove.

## Experience architecture

This is a validation clinic. A plausible pump record arrives with missing and malformed fields. The
shape appears as a declared contract. Each result points to a focus node, path, constraint, severity,
and message. Repairs change the data graph and the report is rerun.

## Visual Arsenal selection

| Idea | Shape | Visual | Conclusion |
| --- | --- | --- | --- |
| Shape and record differ | side-by-side anatomy | Shape-to-data comparison | Validation evaluates declared expectations |
| Results need exact location | diagnostic report | Focus-path-result card | Each failure is traceable |
| Repair changes conformance | before-after loop | Repair and rerun cycle | Validation is executable and repeatable |
| Conformance has limits | boundary frame | Conformance versus truth | Passing a shape does not prove reality |

## Signature mechanism

The SHACL Validation Clinic validates Pump, Sample, Work Order, Customer Exposure, and Outfall
records. The learner repairs missing identifiers, units, dates, roles, and controlled values, then
reruns the report.

## Work product

The Utility SHACL Contract records target class, property paths, constraints, severity, messages,
owner, exception policy, remediation route, test cases, and truth boundary.

## Evidence boundary

SHACL conformance is relative to the declared shapes, data graph, and validation run. It does not
establish completeness, truth, safety, or fitness for every use.
