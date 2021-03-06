import csv
from rest_framework.exceptions import ValidationError

from healthid.utils.app_utils.validators import validate_mobile
from healthid.utils.messages.common_responses import ERROR_RESPONSES


def validate_suppliers_csv_upload(io_string):
    """
        Validate suppliers info from an appropriately formatted CSV file.

        arguments:
            io_string(obj): 'io.StringIO' object containing a list
                            of suppliers in CSV format

        returns:
            array: a list of suppliers
        """
    [row_count, csv_columns, suppliers, csv_errors] = [0, [], [], {}]
    valid_columns = {
        'name': 'required',
        'email': 'required',
        'mobile number': 'required',
        'address line 1': 'not required',
        'address line 2': 'not required',
        'lga': 'not required',
        'city': 'required',
        'tier': 'not required',
        'country': 'required',
        'logo': 'not required',
        'commentary': 'not required',
        'payment terms': 'required',
        'credit days': 'not required',
    }
    for row in csv.reader(io_string):
        csv_columns = list(map(lambda column: column.lower().strip(), row))
        break

    for column in csv_columns:
        csv_errors = {
            **csv_errors,
            'columns': [
                *(csv_errors.get('column') or []),
                ERROR_RESPONSES['not_allowed_field'].format(column)
            ]
        } if column.lower().strip() not in valid_columns else csv_errors

    for row in csv.reader(io_string):
        row_count += 1
        [i, supplier, row_errors] = [0, {}, {}]
        while i < len(row):
            if valid_columns.get(csv_columns[i]) == 'required' and not row[i]:
                row_errors = {
                    **row_errors,
                    csv_columns[i]: ERROR_RESPONSES['required_field'].format(
                        csv_columns[i])
                }
            # validate phone number
            if csv_columns[i] == 'mobile number':
                is_mobile_number_validate = validate_mobile(row[i])
                row_errors = row_errors if is_mobile_number_validate else {
                    **row_errors,
                    csv_columns[i]: (ERROR_RESPONSES['invalid_mobile_number'].
                                     format(row[i]))
                }

            supplier = {
                **supplier,
                csv_columns[i]: row[i]
            } if csv_columns[i] else supplier

            i += 1

        csv_errors = {
            **csv_errors,
            'rows': [
                *(csv_errors.get('rows') or {}),
                {f'{row_count}': row_errors}
            ]
        } if len(row_errors) else csv_errors

        suppliers = [*suppliers, supplier]

    if len(csv_columns) < 13 or len(csv_columns) > 13:
        message = {
            'error': ERROR_RESPONSES['csv_missing_field']
            if len(csv_columns) < 13 else ERROR_RESPONSES['csv_many_field']
        }
        raise ValidationError(message)

    if len(csv_errors):
        raise ValidationError(csv_errors)

    return suppliers
