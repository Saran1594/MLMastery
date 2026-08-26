# Prettfying strings
messy_names = ["  zone a1", "ZONE_A2  ", "Zone-a3", "zone   a4"]
messy_names_fixed = []
def cleaning(messy_names):
    for item in messy_names:
        step1 = item.upper()
        step2 = step1.strip()
        step3 = step2.replace("-", "_")
        step3 = step3.split()
        step4 = " ".join(step3)
        step5 = step4.replace(" ", "_")
        messy_names_fixed.append(step5)
    result = messy_names_fixed
    return result
output = cleaning(messy_names)
print(output)

