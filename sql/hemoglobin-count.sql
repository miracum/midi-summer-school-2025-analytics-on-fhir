SELECT COUNT(DISTINCT patient.id)
FROM fhir.default.observation
LEFT JOIN fhir.default.patient AS patient ON observation.subject.reference = CONCAT('Patient/', patient.id)
LEFT JOIN UNNEST(observation.code.coding) AS observation_code_coding ON TRUE
WHERE
    observation_code_coding.system = 'http://loinc.org'
    AND valuequantity.system = 'http://unitsofmeasure.org'
    AND (
        observation_code_coding.code = '718-7'
        AND valuequantity.code = 'g/dL'
        AND valuequantity.value > 25.0
    )
    OR (
        observation_code_coding.code IN ('17856-6', '4548-4', '4549-2')
        AND valuequantity.code = '%'
        AND valuequantity.value > 5
    );
