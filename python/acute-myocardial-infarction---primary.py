# Nawaraj Bhattarai, Judith Charlton, Caroline Rudisill, Martin C Gulliford, 2024.

import sys, csv, re

codes = [{"code":"G30B.00","system":"readv2"},{"code":"G30..00","system":"readv2"},{"code":"G300.00","system":"readv2"},{"code":"G309.00","system":"readv2"},{"code":"G301000","system":"readv2"},{"code":"G30z.00","system":"readv2"},{"code":"G302.00","system":"readv2"},{"code":"G307.00","system":"readv2"},{"code":"G307000","system":"readv2"},{"code":"G30..15","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('myocardial-infarction-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["acute-myocardial-infarction---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["acute-myocardial-infarction---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["acute-myocardial-infarction---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
