SELECT
    code_coding.display,
    code_coding.code,
    code_coding.system AS code_system,
    COUNT(*) AS num_observations
FROM fhir.default.observation, UNNEST(code.coding) AS code_coding
GROUP BY
    code_coding.code,
    code_coding.system,
    code_coding.display
ORDER BY COUNT(*) DESC;
