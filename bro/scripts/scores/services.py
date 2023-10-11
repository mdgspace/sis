import yaml


# Function to initialize user scores data from a YAML file
def initialize_user_scores_from_file(filename):
    with open(filename, "r") as file:
        data = yaml.safe_load(file)
    return data


def save_user_scores_to_file(data, filename):
    with open(filename, "w") as file:
        yaml.dump(data, file)


def extract_user_and_operator(message):
    parts = message.split()
    if len(parts) == 2 and parts[1] in ("++", "--"):
        return parts[0], parts[1]
    return None, None