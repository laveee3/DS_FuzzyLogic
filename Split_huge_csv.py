import os
import csv

def split(filehandler, delimiter=',', row_limit=2200, output_name_template='output_%s.csv', output_path='.', keep_headers=True):


    reader = csv.reader(filehandler, delimiter=delimiter)
    current_piece = 1
    current_out_path = os.path.join(
        output_path,
        output_name_template % current_piece
    )
    #current_out_writer = csv.writer(open(current_out_path, 'wb'), delimiter=delimiter)
    current_out_writer = csv.writer(open(current_out_path, 'w', newline='',encoding='utf-8'), delimiter=delimiter)
    current_limit = row_limit
    if keep_headers:
        headers = next(reader)
        current_out_writer.writerow(headers)
    for i, row in enumerate(reader):
        if i + 1 > current_limit:
            current_piece += 1
            current_limit = row_limit * current_piece
            current_out_path = os.path.join(
                output_path,
                output_name_template % current_piece
            )
            current_out_writer = csv.writer(open(current_out_path, 'w', newline='',encoding='utf-8'), delimiter=delimiter)
            if keep_headers:
                current_out_writer.writerow(headers)
        current_out_writer.writerow(row)
#split(open('TexasExes.csv','r',encoding='utf-8'))
split(open('TexasExes.csv','r'))