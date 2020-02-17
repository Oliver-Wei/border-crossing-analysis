# Border Crossing Analysis

## Table of Contents
1. [Problem](README.md#problem)
1. [Input Dataset](README.md#input-dataset)
1. [Output](README.md#output)
1. [Approach](README.md#approach)
1. [Instructions](README.md#instructions)
1. [Questions?](README.md#questions?)

## Problem

The Bureau of Transportation Statistics regularly makes available data on the number of vehicles, equipment, passengers and pedestrians crossing into the United States by land.

**I calculate the total number of times vehicles, equipment, passengers and pedestrians cross the U.S.-Canadian and U.S.-Mexican borders each month. I also calculate the running monthly average of total number of crossings for that type of crossing and border.**

## Input Dataset

The input file, `Border_Crossing_Entry_Data.csv`, is in the top-most `input` directory of your repository.

The file contains data of the form:

```
Port Name,State,Port Code,Border,Date,Measure,Value,Location
Derby Line,Vermont,209,US-Canada Border,03/01/2019 12:00:00 AM,Truck Containers Full,6483,POINT (-72.09944 45.005)
Norton,Vermont,211,US-Canada Border,03/01/2019 12:00:00 AM,Trains,19,POINT (-71.79528000000002 45.01)
Calexico,California,2503,US-Mexico Border,03/01/2019 12:00:00 AM,Pedestrians,346158,POINT (-115.49806000000001 32.67889)
Hidalgo,Texas,2305,US-Mexico Border,02/01/2019 12:00:00 AM,Pedestrians,156891,POINT (-98.26278 26.1)
Frontier,Washington,3020,US-Canada Border,02/01/2019 12:00:00 AM,Truck Containers Empty,1319,POINT (-117.78134000000001 48.910160000000005)
Presidio,Texas,2403,US-Mexico Border,02/01/2019 12:00:00 AM,Pedestrians,15272,POINT (-104.37167 29.56056)
Eagle Pass,Texas,2303,US-Mexico Border,01/01/2019 12:00:00 AM,Pedestrians,56810,POINT (-100.49917 28.70889)
```

## Output

Using the input file, I write a program to 

* Sum the total number of crossings (`Value`) of each type of vehicle or equipment, or passengers or pedestrians, that crossed the border that month, regardless of what port was used. 
* Calculate the running monthly average of total crossings, rounded to the nearest whole number, for that combination of `Border` and `Measure`, or means of crossing.

I write the requested output data to a file named `report.csv` in the top-most `output` directory of my repository.

For example, given the above input file, the correct output file I write, `report.csv`  is:

```
Border,Date,Measure,Value,Average
US-Mexico Border,03/01/2019 12:00:00 AM,Pedestrians,346158,114487
US-Canada Border,03/01/2019 12:00:00 AM,Truck Containers Full,6483,0
US-Canada Border,03/01/2019 12:00:00 AM,Trains,19,0
US-Mexico Border,02/01/2019 12:00:00 AM,Pedestrians,172163,56810
US-Canada Border,02/01/2019 12:00:00 AM,Truck Containers Empty,1319,0
US-Mexico Border,01/01/2019 12:00:00 AM,Pedestrians,56810,0
```

The lines are sorted in descending order by 
* `Date`
* `Value` (or number of crossings)
* `Measure`
* `Border`

The column, `Average`, is for the running monthly average of total crossings for that border and means of crossing in all previous months. In this example, to calculate the `Average` for the first line (i.e., running monthly average of total pedestrians crossing the US-Mexico Border in all of the months preceding March), I take the average sum of total number of US-Mexico pedestrian crossings in February `156,891 + 15,272 = 172,163` and January `56,810`, and round it to the nearest whole number `round(228,973/2) = 114,487`

## Approach

`Python` program is used to solve the problem. `Dictionary` and `List` are mainly used to handle `input` and `output`.

Firstly, the program would read the input file `Border_Crossing_Entry_Data.csv` in the top-most `input` directory of my repository, and save all requested information to a nested dictionary `bm_to_dv`, where the key of the dictionary' top-most level is `Border and Measure` and the value is `Year`; the key of the dictionary' second level is `Year` and the value is `Month`; and the key of the dictionary' bottom level is `Month` and the value is `total Value of crossings that month`.

Secondly, the program would calculate the running monthly average of total crossings for that border and means of crossing in all previous months of this year, and save the results `Average` together with original information in the nested dictionary `bm_to_dv`.

Finally, the program would use information in the nested dictionary `bm_to_dv`, to write all requested output data in specified order to a csv file named `report.csv` in the top-most `output` directory of my repository.

### Time complexity

Define the number of lines in the input dataset as n. Although there are many `nested for loops` in my program, the time complexity of it is `O(n)`. Details of the time and space analysis can be found in the comments of the program `border_analytics.py`

### Limitations

This program can only work for input dataset of limited scale. If the input dataset is too big, then the program should be modified a little bit. For example, the program need to read, calculate and write by using `mini-batch` methods. But the main algorithms are the same.

## Instructions

### Repo directory structure

The directory structure for my repo looks like this:

    ├── README.md
    ├── run.sh
    ├── src
    │   └── border_analytics.py
    ├── input
    │   └── Border_Crossing_Entry_Data.csv
    ├── output
    |   └── report.csv
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
            |   ├── input
            |   │   └── Border_Crossing_Entry_Data.csv
            |   |__ output
            |   │   └── report.csv
            ├── my-own-test_1
                ├── input
                │   └── Border_Crossing_Entry_Data.csv
                |── output
                    └── report.csv

### Run

To run my script and produce the specified results in the specified folder, run the `run.sh` file in the project root directory.


# Questions?
Email me at oliverwei24@gmail.com
