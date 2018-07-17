import csv
 
# open file
with open('AQI_20180717092554.csv', 'r', encoding='utf-8-sig') as f:
    reader =csv.reader(f)

    # read file row by row
    ini=int(100)
    for row in reader:
        if row[2]=='AQI':
            pass
        else:
            if int(row[2])<ini:
                ini=int(row[2])
                cou=row[1]
                sit=row[0]
    print(str(sit)+cou+'空氣最好，'+'AQI是'+str(ini))