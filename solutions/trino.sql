SELECT
    condition_code_coding.display,
    patient.gender,
    COUNT(DISTINCT patient.id) AS num_patients
FROM fhir.default.condition
LEFT JOIN fhir.default.patient AS patient ON condition.subject.reference = CONCAT('Patient/', patient.id)
LEFT JOIN UNNEST(condition.code.coding) AS condition_code_coding ON TRUE
WHERE condition_code_coding.system = 'http://snomed.info/sct'
GROUP BY condition_code_coding.display, patient.gender
ORDER BY COUNT(DISTINCT patient.id) DESC
LIMIT 25;
