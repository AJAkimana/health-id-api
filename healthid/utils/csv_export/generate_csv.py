import csv


def generate_csv_response(response, filename, model, include=[], name=None):
    """Generate an empty CSV file.

    The CSV file header is generated from the model fields and
    an include list is needed to explicitly state the field to
    be used

    Args:
        response (obj): The HttpResponse object.
        filename (str): The name of the csv file.
        model (cls): The name of the model to generate CSV for
        include (list): The fields for the CSV column titles

    Returns:
        response (obj): The HttpResponse object.
    """

    response = response(content_type='text/csv')
    response['Content-Disposition'] = \
        'attachment; filename=' + filename

    if name == 'batch':
        model_fields = [field.name for field in model._meta.get_fields()]
        header_row = [field.replace('_', ' ').title()
                      for field in include
                      if field in model_fields]
        header_row.insert(5, 'Quantity Received')
    else:
        header_row = [field.name.replace('_', ' ').title()
                      for field in model._meta.get_fields()
                      if field.name in include]

    writer = csv.DictWriter(
        response,
        fieldnames=header_row,
        extrasaction='ignore')
    writer.writeheader()

    return response
