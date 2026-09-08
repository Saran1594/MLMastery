#zone = {"zone_id": "A1", "Shift": "1st", "PPH": 145, "Target_PPH": 160}
import csv
def report_generator():
    with open("C:\\Users\\JW60\\OneDrive - Nordstrom\\Panda.csv", "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        zones = list(reader)
        all_reports = ""
        for zone in zones:
            zone["PPH"] = int(zone["PPH"])
            zone["Target_PPH"] = int(zone["Target_PPH"])
            if zone['PPH'] > zone['Target_PPH']:
                    status = "Exceeded_Target"
            elif zone['PPH'] < zone['Target_PPH']:
                    status = "Below_Target"
            else:
                    status = "Check_Shift_Schedule"
            report = f"""
            zone: {zone['zone_id']}
            shift: {zone['Shift']}
            PPH: {zone['PPH']}
            Target: {zone['Target_PPH']}
            Status: {status}
            """
            all_reports += report
        return all_reports
output = report_generator()
print(output)
