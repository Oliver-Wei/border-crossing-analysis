import sys
import csv
from datetime import datetime
from datetime import time

def get_info(row):
    """ 
    Get date, value, measure and border information from each record of crossing
    """

    date = datetime.strptime(row["Date"], "%m/%d/%Y %H:%M:%S %p")
    value = int(row["Value"])
    measure = row["Measure"]
    border = row['Border']

    return (date,value,measure,border)

def read_input(input_file_name):
    """
    Read the input file and save all requested information to a nested dictionary "bm_to_dv"
    The key of the dictionary' top-most level is "border and measure" and the value is "year"
    The key of the dictionary' second level is "year" and the value is "month".
    The key of the dictionary' bottom level is "month" and the value is "total value of crossings that month".

    bm respresents border and measure 
    dv represents date and value
    """

    with open(input_file_name,newline='') as input_file:
        reader = csv.DictReader(input_file)
        bm_to_dv = {}       # Nested dictionary saves all information from input
        for row in reader:
            date,value,measure,border = get_info(row)
            month = date.month
            year = date.year
            bm = str([border,measure])      # Convert border and measure back later by eval()  

            if (bm in bm_to_dv.keys()):
                if (year not in bm_to_dv[bm].keys()):
                    bm_to_dv[bm][year] = {}     
                bm_to_dv[bm][year][month] = bm_to_dv[bm][year].get(month,0)+value
                
            else:
                bm_to_dv[bm] = {}       # Use "border and measure" as key of bm_to_dv
                bm_to_dv[bm][year] = {}     # Use "year" as key of year_to_month dictionary
                bm_to_dv[bm][year][month] = value   # Use "month" as key of month_to_value dictionary
    
    # Calculate monthly average of total crossings for certain border and measures 
    # of crossing in all previous months.
    for bm in bm_to_dv.keys():
        for year in bm_to_dv[bm].keys():
            bm_to_dv[bm][year] = get_values(bm_to_dv[bm][year])

    return bm_to_dv 

def get_values(month_to_value):
    """
    Convert the dictionary "month_to_value" to a new dictionary "month_to_values",
    where values is represented by a tuple: 

    values = (# crossing of this month, # average crossing of previous months, 
    # total crossings including this month)

    # total crossings including this month is saved to calculate # average crossing for next month
    """

    month_to_values = {}
    
    for month in sorted(month_to_value):
        if (month-1 not in month_to_value):
            month_to_values[month] = (month_to_value[month],0,month_to_value[month])
        else:
            month_to_values[month] = (month_to_value[month],round(month_to_values[month-1][2]/(month-1)),month_to_values[month-1][2]+month_to_value[month]) 
    
    return month_to_values

def write_output(bm_to_dv,output_file_name):
    """
    Output a csv file from the nested dictionary "bm_to_dv"
    """

    records = []
    t = time(12, 0, 0)      # Set up time 12:00:00 AM


    for bm,year_to_month in bm_to_dv.items():
        for year,month_to_values in year_to_month.items():
            for month,values in month_to_values.items():
                d = datetime(year, month, 1)        # Set up date mm/01/yyyy
                dt = datetime.combine(d, t)         # Combine date and time to "mm/01/yyyy 12:00:00 AM"
                record = eval(bm)+[dt.strftime("%m/%d/%Y %H:%M:%S AM"),values[0],values[1],year,month]
                # Use a list to record all required information
                # [0:border,1:measure,2:date,3:value,4:average,5:year,6:month]
                records.append(record)
    
    # Sort records in descending order by date(year and month), value, measure, border
    records.sort(key=lambda l: (l[5],l[6],l[3],l[1],l[0]),reverse=True)     

    # Write required information of all records to output file
    with open(output_file_name, 'w', newline='') as output_file:
        fieldnames = ['Border', 'Date','Measure','Value','Average']
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        for record in records:
            writer.writerow({'Border': record[0], 'Date': record[2],'Measure': record[1],'Value': record[3],'Average': record[4]})
        
if __name__ == "__main__":
    input_file_name,output_file_name = sys.argv[1],sys.argv[2]
    bm_to_dv = read_input(input_file_name)
    write_output(bm_to_dv,output_file_name)
