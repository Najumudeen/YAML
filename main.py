import yaml

def main():
  # read the yaml file
    try:
        with open("config.yml", "r") as file:
            yaml_data = yaml.safe_load(file)
            
        # Print the data
        print(f"Name: {yaml_data['name']}")
        print(f"Age: {yaml_data['age']}")
        print(f"occupation: {yaml_data['occupation']}")
        print(f"Skills: {yaml_data['skills']}")
        
        for skill in yaml_data['skills']:
            print(f" - {skill}")
        
        print(f"is_employed: {yaml_data['is_employed']}")
        print(f"favourite_number: {yaml_data['favorite_number']}, {type(yaml_data['favorite_number'])}")
    except FileNotFoundError:
        print("File not Found")
    except PermissionError:
        print("Permission Denied")
    except yaml.YAMLError as exc:
        print(f"Error While Parsing Yaml:", exc)
    except KeyError as exc:
        print(f"Key not founf", exc)
    except Exception as exc:
        print(f"an error Occurred", exc)
    
    


if __name__ == "__main__":
    main()