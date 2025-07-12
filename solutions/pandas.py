# Merge

merged = patients.merge(
    conditions_snomed,
    left_on="id_as_reference",
    right_on="subject_reference",
    how="left",
)
merged

# Plot

import matplotlib.pyplot as plt

code_counts = (
    merged.groupby(["code_coding_display", "gender"])["subject_reference"]
    .nunique()
    .reset_index()
    .rename(columns={"subject_reference": "patient_count"})
    .sort_values(by="patient_count", ascending=False)
)

# Pivot um von 1 Zeile pro Code und Geschlecht zu einer Zeile pro Code und Spalten pro Geschlecht zu kommen
# Vereinfacht plotten
pivot = code_counts.pivot(
    index="code_coding_display", columns="gender", values="patient_count"
).fillna(0)

# top codes via Summer über alle Geschlechter
top_codes = pivot.sum(axis=1).sort_values(ascending=False).head(25).index
pivot_top = pivot.loc[top_codes]

pivot_top.plot(kind="bar", figsize=(12, 6))
plt.xlabel("Diagnose")
plt.ylabel("Anzahl Patienten")
plt.title("Histogramm: Anzahl Patienten pro Diagnose-Code")
plt.xticks(rotation=75)
plt.tight_layout()
plt.show()
