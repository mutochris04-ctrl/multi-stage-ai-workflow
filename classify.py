import csv


def classify_child(muac_mm, oedema):
    # Oedema takes priority over the MUAC measurement.
    if oedema.strip().lower() == "yes":
        return "Severe (SAM)"
    elif int(muac_mm) < 115:
        return "Severe (SAM)"
    elif int(muac_mm) < 125:
        return "Moderate (MAM)"
    else:
        return "Normal"


# Read each child, classify them, print the result, and keep the output rows.
results = []
severe_count = 0
moderate_count = 0
normal_count = 0

with open("children.csv", newline="", encoding="utf-8") as input_file:
    children = csv.DictReader(input_file)

    for child in children:
        status = classify_child(child["muac_mm"], child["oedema"])
        results.append([
            child["child_id"],
            child["name"],
            child["muac_mm"],
            child["oedema"],
            status,
        ])

        print(child["name"], child["muac_mm"], child["oedema"], status, sep=", ")

        if status == "Severe (SAM)":
            severe_count += 1
        elif status == "Moderate (MAM)":
            moderate_count += 1
        else:
            normal_count += 1

# Write the classified children to a new CSV file.
with open("results.csv", "w", newline="", encoding="utf-8") as output_file:
    writer = csv.writer(output_file)
    writer.writerow(["child_id", "name", "muac_mm", "oedema", "status"])
    writer.writerows(results)

# Print the total number of children in each nutrition group.
print("Severe:", severe_count)
print("Moderate:", moderate_count)
print("Normal:", normal_count)
