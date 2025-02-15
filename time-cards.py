import csv
import datetime

#Extract email from the first column of the CSV Record
# column is in the formart of (name)(@id)(email)
def extract_email_from_name(name):
    #split into three items name), @id), email)
    #pick last email) and split again ) and get first
    return name.split("(")[-1].split(")")[0]


def process_record_datetime(csv_record):
    email = extract_email_from_name(csv_record[0])
    in_date_time_obj = datetime.datetime.strptime(f"{csv_record[3]} {csv_record[5]}", "%m/%d/%Y %I:%M %p")
    in_date_time_str = in_date_time_obj.strftime("%d/%m/%Y %H:%M")

    out_date_time_obj = datetime.datetime.strptime(f"{csv_record[3]} {csv_record[6]}", "%m/%d/%Y %I:%M %p")
    out_date_time_str = out_date_time_obj.strftime("%d/%m/%Y %H:%M")
    return [email, in_date_time_str, out_date_time_str]


#Open file, read record by record, process data and return list of 
#output records as list
def process_csv_file(input_file):
    #create output records and add header first
    #header_row = ["id", "in", "out"]
    #output_records = []
    #output_records.append(header_row)
    output_records = [["id", "in", "out"]]
    with open(input_file, "r") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for record in reader:
            #output = process_record(record)
            output = process_record_datetime(record)
            output_records.append(output)
    
    return output_records

def write_csv_file(out_file_name, out_data):
    with open('out.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(out_data)

             
out_data = process_csv_file("time-cards - Sheet1.csv")
write_csv_file("out.csv", out_data)


#unit tests for extract_email_from_name
