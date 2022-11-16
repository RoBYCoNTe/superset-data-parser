# list files contained in xlsx directory
# merge all files into one csv file
# save csv file in csv directory

import os
import pandas as pd


def list_files(directory, extension) -> list[str]:
    files = (f for f in os.listdir(directory) if f.endswith('.' + extension))
    files = (os.path.join(directory, f) for f in files)
    return files


# list files contained in xlsx directory
files = list_files('xlsx', 'xlsx')
rows = 0
# create csv with these columns: 'comune', 'età', 'anno', 'indicatore', 'valore'
df = pd.DataFrame(columns=[
    'municipality',
    'age_range',
    'sex',
    'year',
    'indicator',
    'value'])

for file in files:
    print("Processing: {}".format(file))

    bad_words = ['xlsx/', ' - Femmine', ' - Maschi', ' - All', '.xlsx']
    age_range = file
    for word in bad_words:
        age_range = age_range.replace(word, '')
    sex = "All"
    if "Femmine" in file:
        sex = "F"
    elif "Maschi" in file:
        sex = "M"

    print("File: {} - Sex: {}, Age Range: {}".format(file, sex, age_range))

    excel_file = pd.ExcelFile(file)
    sheet_names = excel_file.sheet_names
    # for sheet_name in sheet_names:

    #     print("Processing: {}".format(sheet_name))
    #     df = pd.read_excel(file, sheet_name=sheet_name)
    #     # Count rows
    #     rows += df.shape[0]


print("Total rows: {}".format(rows))
