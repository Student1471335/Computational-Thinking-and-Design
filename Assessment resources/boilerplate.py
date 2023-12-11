import pandas as pd
import json
contents = pd.read_csv('C:/Users/Matt/Documents/Uni handin/Final assessment/Assessment resources/dataset/10books.csv')
books = json.loads(contents.to_json(orient='records'))
print(books[0])




