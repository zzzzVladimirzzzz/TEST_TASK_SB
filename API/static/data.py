from static.paths import *
from utils.json_conversion import convert_func

delay_dict = convert_func(json_file=delay_file_json_path)
forms_dict = convert_func(json_file=forms_json_path)
total_query_execution_time = sum(delay_dict.values())
