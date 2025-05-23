json_type = "GOOD Files (*.json)"

yaml_type = "YAML Files (*.yaml)"


def verify_accuracy(data: float, base: float, perc: float = 5.0):
    return abs((base - data) * 100 / base) <= perc
