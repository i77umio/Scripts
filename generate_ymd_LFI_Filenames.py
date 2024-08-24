from datetime import datetime, timedelta

def generate_filenames():
    years = [2020, 2021]
    months_days = {
        "01": 31, "02": 29, "03": 31, "04": 30, "05": 31, "06": 30,
        "07": 31, "08": 31, "09": 30, "10": 31, "11": 30, "12": 31
    }

    filenames = []
    for year in years:
        for month, days in months_days.items():
            if year == 2021 and month == "02":
                days = 28  # 2021 is not a leap year
            for day in range(1, days + 1):
                filenames.append(f"{year}-{month}-{str(day).zfill(2)}-upload.pdf")
    return filenames

# Generate the list of filenames
filenames = generate_filenames()
#print(filenames)  # Display the total count and the first 10 filenames as an example
for filename in filenames:
        print(filename)
