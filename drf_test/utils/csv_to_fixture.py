import csv
import codecs
import json
import os


def convert_csv_to_fixture(
        encoding: str,
        csv_delimiter: str,
        path_to_in_file: str,
        path_to_out_file: str
) -> None:
    if not os.path.exists(path_to_out_file):
        os.mkdir(path_to_out_file)

    for input_name in os.listdir(path_to_in_file):
        if '.csv' in input_name:
            model_name = f'app.{input_name.lower()[:-4]}'

            # Compute file paths and names
            in_file = path_to_in_file + input_name
            output_name = input_name.replace('.csv', '.json')
            out_file = path_to_out_file + output_name

            # Convert
            with codecs.open(in_file, 'r', encoding=encoding) as f:

                reader = csv.reader(f, delimiter=csv_delimiter)

                header_row = []
                entries = []

                for row_id, row in enumerate(reader):

                    if not header_row:
                        header_row = row
                        continue

                    pk = row_id
                    fields = {}
                    products_path = 'drf_test/app/fixtures/Products.json'

                    if (
                            os.path.exists(products_path) and
                            model_name == 'app.reviews'
                    ):
                        with open(products_path) as file:
                            products_data = json.load(file)

                            for data_dict in products_data:
                                if row[0] in data_dict['fields'].values():
                                    row[0] = data_dict['pk']

                    for index in range(len(row)):
                        active_field = row[index]
                        fields[header_row[index].lower()] = active_field

                    row_dict = {
                        'pk': int(pk),
                        'model': model_name,
                        'fields': fields
                    }
                    entries.append(row_dict)

            with open(out_file, 'w') as fo:
                fo.write(f'{json.dumps(entries, indent=4)}')


if __name__ == '__main__':
    convert_csv_to_fixture(
        encoding='UTF-8',
        csv_delimiter=',',
        path_to_in_file='data/files_for_fixture/',
        path_to_out_file='drf_test/app/fixtures/'
    )
