import pandas as pd
# import yaml
import ruamel.yaml
# convert csv reading file to yaml file

csv_path = "data/raw/reading.csv"
yaml_path = "data/processed/reading.yaml"

df = pd.read_csv(csv_path)

col_dict = {"Title": "title", 
            "Authors": "authors", 
            "Read Status": "status", 
            "Last Date Read": "last_date_read", 
            "Review": "review", 
            "Tags": "categories"}

cols_to_keep = list(col_dict.keys())
df = df[cols_to_keep]
df.rename(columns=col_dict, inplace=True)



d = df.to_dict(orient="records")
for book in d:
    book["authors"] = [author.strip() for author in book["authors"].split(",")]
    book["status"] = "read" if book["status"] == "read" else book["status"]
    book["status"] = "reading" if book["status"] == "currently-reading" else book["status"]
    book["categories"] = [tag.strip() for tag in book["categories"].split(",")] if pd.notnull(book["categories"]) else []
    
    book["is_fiction"] = True if book["categories"] and "fiction" in book["categories"] else False
    book["categories"] = [tag for tag in book["categories"] if tag != "fiction" and tag != "nonfiction"]
    
    

# filter d to contain only books that are either "read" or "reading"
d = [book for book in d if book["status"] in ["read", "reading"]]



yaml = ruamel.yaml.YAML()
yaml.preserve_quotes = True



# save as yaml file
with open(yaml_path, "w") as f:
    yaml.dump(d, f)



