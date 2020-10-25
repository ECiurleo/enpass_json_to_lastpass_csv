from main.base.fields.enpass_field import EnpassField
from main.base.fields.name_field import NameField
from test.fixture.base_test_fixture import row_with_all_fields
from main.base.fields import url_field, user_name_field, password_field


def get_enpass_field_interpreter(enpass_field_data) -> EnpassField:
    for field in EnpassField.subclasses:
        if field.is_applicable(enpass_field_data):
            return field


def get_row_meta_data(input_enpass_json_row):
    row_data = {NameField.get_lastpass_field_name(): NameField.get_parsed_value(input_enpass_json_row)}
    return row_data


def parse(input_enpass_json_row) -> {}:
    row_data = get_row_meta_data(input_enpass_json_row)

    enpass_fields_data = input_enpass_json_row["fields"]
    for enpass_field_data in enpass_fields_data:
        enpass_field = get_enpass_field_interpreter(enpass_field_data)
        row_data[enpass_field.get_lastpass_field_name()] = enpass_field.get_parsed_value(enpass_field_data)

    return row_data


if __name__ == "__main__":
    print(parse(row_with_all_fields))