import files
import pandas as pd

xlsx_files = files.ChronicityFileInfo.list('tmp')
rows = 0
# Open dataset_csv in UTF-8 encoding

dataset_csv = open('dataset.csv', 'w', encoding='utf-8')
dataset_columns = ",".join([
    "filename",
    "sheet",
    "column",
    "reference",
    'reference_type',
    'age_range',
    'sex',
    'year',
    'pathology',
    'risk',
    'indicator',
    'value'
]) + '\n'
dataset_csv.write(dataset_columns)

for xlsx_file in xlsx_files:
    print("File: {}".format(xlsx_file.path))
    total_rows = 0
    for sheet_name in xlsx_file.get_sheet_names():
        data = pd.read_excel(xlsx_file.path, sheet_name=sheet_name)
        column_names = list(data.columns)
        csv_rows = []
        for index, row in data.iterrows():
            string = row['STRINGA']
            # Type is first part of exploded string by ' - '
            reference_type = string.split(' - ')[0]
            reference_type = reference_type[0]

            # Name is the entire string if it doesn't contain ' - ' else it's the second part
            args = string.split(' - ')
            if len(args) > 1:
                reference = ' - '.join(args[1:])
            else:
                reference = string
            for column in column_names:
                if column == 'STRINGA':
                    continue

                # check if row contains a column named column
                if column not in row:
                    continue

                value = row[column]
                if pd.isna(value):
                    continue

                # Year is the last part of exploded column_name
                year = str(column.split('_')[-1])
                # Indicator is the rest of exploded column_name
                indicator = str('_'.join(column.split('_')[:-1]))
                pathology = str(sheet_name.split('_')[0])
                # Risk is the rest of exploded sheet_name
                risk = str(' '.join(sheet_name.split('_')[1:]))
                # If risk is empty set it to sheet_name
                if risk == '':
                    risk = sheet_name

                indicator = indicator.replace("_{}".format(pathology), '')
                risk = risk.replace(pathology, 'Tutte')
                csv_line: list[str] = [
                    xlsx_file.name,
                    sheet_name,
                    column,
                    reference,
                    reference_type,
                    xlsx_file.age_range,
                    xlsx_file.sex,
                    year,
                    pathology,
                    str(risk),
                    str(indicator),
                    str(value)
                ]
                csv_line = ','.join(csv_line) + '\n'
                csv_rows.append(csv_line)

        dataset_csv.writelines(csv_rows)

dataset_csv.close()
exit()
