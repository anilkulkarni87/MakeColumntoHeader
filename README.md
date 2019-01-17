# MakeColumntoHeader
Conversion a two column csv file.

## Input:
Name,Kamath
Age,23
Sex,Male
Company,ACC
Vehicle,Car
Name,Ram
Age,32
Sex,Male
Company,CCA
Vehicle,Bike
Name,Reena
Age,26
Sex,Female
Company,BARC
Vehicle,Cycle

## OUTPUT:
Name,Age,Sex,Company,Vehicle
Kamath,23,Male,ACC,Car
Ram,32,Male,CCA,Bike
Reena,26,Female,BARC,Cycle

## usage: convertcsv.py [-h] [-n N] [-i INPUTFILE] [-d DELIMITER] [-o OUTPUTFILE]

optional arguments:
  -h, --help            show this help message and exit
  -n N                  Number of rows to be grouped
  -i INPUTFILE, --inputfile INPUTFILE
                        Provide the path of the input file
  -d DELIMITER, --delimiter DELIMITER
                        Provide the delimiter
  -o OUTPUTFILE, --outputfile OUTPUTFILE
                        Provide the path of the output file
