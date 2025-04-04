import yaml

# try:
#     with open("file-stage.yml", "r") as file:
#         config = yaml.safe_load(file)
# except FileNotFoundError:
#     print("File not Found")

# try: 
#     print(config)
# except NameError:
#     print("Config Not Defined")

# # Nested Data structure

# print(config['name'])

# # Chaining the key or indices
# print(config['name'][0]['name'])

# # Error Handling

try:
    with open('file-stage.yml', 'r') as file:
        data = yaml.safe_load(file)
except FileNotFoundError:
    print("File not Found")
except yaml.YAMLError as error:
    print("Error Parsing YAML file:", error)
