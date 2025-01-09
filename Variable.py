import json
# Reading api_key
class Variable:
    @staticmethod
    def get_variable(var_name):
        try:
            with open("config.cfg") as file:
                file_content = json.loads(file.read())
                return file_content[var_name]
        except Exception as e:
            print(f"[Error]: {e}")