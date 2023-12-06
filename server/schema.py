import yaml
from jsonschema import validate

def validate_tags(tags_file_path, schema_file_path):
    # Load YAML schema
    with open(schema_file_path, 'r') as schema_file:
        schema = yaml.safe_load(schema_file)

    # Load YAML data
    with open(tags_file_path, 'r') as tags_file:
        tags_data = yaml.safe_load(tags_file)

    # Validate the data against the schema
    try:
        validate(tags_data, schema)
        print("YAML document is valid against the schema.")
    except Exception as e:
        print(f"Validation error: {e}")

# Paths to your YAML files
tags_yaml_path = "tags.yaml"
tags_schema_yaml_path = "tags_schema.yaml"

# Validate the YAML data against the schema
validate_tags(tags_yaml_path, tags_schema_yaml_path)
