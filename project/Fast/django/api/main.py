def apply_filters(Model, filters: dict, values: dict):
    filter_query = {}
    for value in values.keys():
        try:
            filter_query.update({filters[value]: values[value]})
        except KeyError:
            return {
                'status': 'error',
                'error': 'KeyError',
                'invalid_key': value
            } 

    return {
        'status': 'success',
        'model': Model.objects.filter(**filter_query).order_by('id'),
    } 
    