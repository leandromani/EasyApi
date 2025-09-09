import sqlite3
import yaml

def init_database():
    with open("easyApi.config.yaml", "r") as f:
        config = yaml.safe_load(f)

    connection = sqlite3.connect(config["database"]["name"])
    cursor = connection.cursor()
    
    print(config["database"]["name"])     
    
    