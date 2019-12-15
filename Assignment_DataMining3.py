"""
Data Mining Assignment
Google stock prices from Jan 2004 to Oct 2019
1- Calculate best and worst six months
2- Calculate best and worst six years for Google

Stefanie Cruz - D19124788
2019
"""

import csv


def read_csv(csv_file):
    """
    Function to read CSVs
    :param csv_file: The file to be read
    :return: Data list
    """
    try:
        with open(csv_file) as file:
            csv_reader = csv.reader(file, delimiter=",")

            data_list = []

            for row in csv_reader:
                date = row[0]
                open_price = row[1]
                high_price = row[2]
                low_price = row[3]
                close_price = row[4]
                adjclose_price = row[5]
                volume_sold = row[6]
                data_list.append([date, open_price, high_price, low_price, close_price, adjclose_price,volume_sold])

            return data_list
    except Exception as e:
        print(f"Could not read {csv_file}, please try again. {e}")


# Extract necessary data to perform calculations: 'Year', 'Year + Month', 'Day Average (Adj Close * Volume)', 'Volume'

my_file = read_csv('GOOGL.csv')

csv_file_list = []

for row in my_file:
    if "Date" != row[0]:
        year = row[0][:4]
        year_month = row[0][:7]
        adjclose = float(row[5])
        volume = int(row[6])
        day_avg = adjclose * volume
        csv_file_list.append([year, year_month, day_avg, volume])

# Yearly average: create dictionaries with adjclose and volume sums for each year

year_adjclose_sum = {}
year_volume_sum = {}

for row in csv_file_list:
    year = row[0]
    adjclose = row[2]
    volume = row[3]
    if year not in year_adjclose_sum:
        year_adjclose_sum[year] = 0
        year_volume_sum[year] = 0

    year_adjclose_sum[year] = year_adjclose_sum[year] + float(adjclose)
    year_volume_sum[year] = year_volume_sum[year] + int(volume)

# Final list with yearly averages

yearly_avg_list = []

for year in year_adjclose_sum: # Iterate through the dictionaries, dividing cumulative adjclose by volume
    yearly_avg = year_adjclose_sum[year] / year_volume_sum[year]
    yearly_avg_list.append([yearly_avg, year])

# Sort yearly average list
yearly_avg_list.sort()

# Monthly average: create dictionaries with adjclose and volume sums for each month

month_adjclose_sum = {}
month_volume_sum = {}

for row in csv_file_list:
    month = row[1]
    adjclose = row[2]
    volume = row[3]
    if month not in month_adjclose_sum:
        month_adjclose_sum[month] = 0
        month_volume_sum[month] = 0

    month_adjclose_sum[month] = month_adjclose_sum[month] + float(adjclose)
    month_volume_sum[month] = month_volume_sum[month] + int(volume)

# Final list with monthly averages

monthly_avg_list = []

for month in month_adjclose_sum: # Iterate through the dictionaries, dividing cumulative adjclose by volume
    monthly_avg = month_adjclose_sum[month] / month_volume_sum[month]
    monthly_avg_list.append([monthly_avg, month])

# Sort monthly average list
monthly_avg_list.sort()

# Print out worst/best share prices by year

print("Worst six years")

for year in yearly_avg_list[:6]:
    print(f"{year[1]}: {year[0]:<.2f}")

print(" ")
print("Best six years")

for year in yearly_avg_list[-1:-7:-1]:
    print(f"{year[1]}: {year[0]:<.2f}")

print(" ")
print("-" * 50)
print(" ")

# Print out worst/best share prices by month

print("Worst_six_months")

for month in monthly_avg_list[:6]:
    print(f"{month[1]}: {month[0]:<.2f}")

print(" ")
print("Best_six_months")

for month in monthly_avg_list[-1:-7:-1]:
    print(f"{month[1]}: {month[0]:<.2f}")

print(" ")
print("-" * 50)

