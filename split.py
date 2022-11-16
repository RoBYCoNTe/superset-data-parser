dataset_columns = ",".join([
    "group",
    'type',
    'name',
    'age_range',
    'sex',
    'year',
    'pathology',
    'risk',
    'indicator',
    'value'
]) + '\n'

# Open dataset csv and split in chunks of 1 milion rows
dataset_csv = open('dataset.csv', 'r')
dataset_csv.readline()
dataset_csv_rows = dataset_csv.readlines()
dataset_csv.close()
dataset_csv_chunks = [dataset_csv_rows[i:i + 1000000]
                      for i in range(0, len(dataset_csv_rows), 1000000)]
for i, chunk in enumerate(dataset_csv_chunks):
    dataset_csv = open('split/dataset_{}.csv'.format(i), 'w')
    dataset_csv.writelines([dataset_columns] + chunk)
    dataset_csv.close()
