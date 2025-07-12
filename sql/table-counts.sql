SELECT
    'Patient' AS resource_type,
    COUNT(*) AS resource_count
FROM fhir.default.patient
UNION
SELECT
    'Condition' AS resource_type,
    COUNT(*) AS resource_count
FROM fhir.default.condition
UNION
SELECT
    'Observation' AS resource_type,
    COUNT(*) AS resource_count
FROM fhir.default.observation;
