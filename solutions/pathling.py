# Übung 1

conditions = data.extract(
    "Condition",
    columns=[
        exp("Condition.id", "condition_resource_id"),
        exp(
            "Condition.subject.reference",
            "subject_reference",
        ),
        exp(
            "Condition.clinicalStatus.coding.where(system='http://terminology.hl7.org/CodeSystem/condition-clinical').first().code",
            "clinical_status",
        ),
        exp(
            "Condition.code.coding.where(system='http://snomed.info/sct').code",
            "code_coding_code",
        ),
        exp(
            "Condition.code.coding.where(system='http://snomed.info/sct').display",
            "code_coding_display",
        ),
    ],
    filters=[
        "Condition.clinicalStatus.coding.where(system='http://terminology.hl7.org/CodeSystem/condition-clinical').first().code = 'active'",
    ],
)

conditions.show(truncate=False, n=100)

# Übung 2

conditions = data.extract(
    "Condition",
    columns=[
        exp("Condition.id", "condition_resource_id"),
        exp(
            "Condition.subject.reference",
            "subject_reference",
        ),
        exp(
            "Condition.clinicalStatus.coding.where(system='http://terminology.hl7.org/CodeSystem/condition-clinical').first().code",
            "clinical_status",
        ),
        exp(
            "Condition.code.coding.where(system='http://snomed.info/sct').code",
            "code_coding_code",
        ),
        exp(
            "Condition.code.coding.where(system='http://snomed.info/sct').display",
            "code_coding_display",
        ),
        exp(
            "Condition.subject.resolve().ofType(Patient).gender",
            "patient_gender",
        ),
    ],
    filters=[
        "Condition.clinicalStatus.coding.where(system='http://terminology.hl7.org/CodeSystem/condition-clinical').first().code = 'active'",
    ],
)

conditions.show(truncate=False, n=100)
