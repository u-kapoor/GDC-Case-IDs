# Key functions and imported libraries
from docx import Document
import pandas as pd
import re
import os
import requests
import json

csv_filepath = r'C:\Users\utska\OneDrive\Med School\Research\Genomics\RNA Seq'
csv_filename = r'UUID List.csv'
UUID_list = pd.read_csv(csv_filepath + chr(92) + csv_filename)
Entity_ID_list = []
for i in range(len(UUID_list)):
    # Download data from GDC API
    files_endpt = 'https://api.gdc.cancer.gov/files/' + UUID_list.UUID[i] 
    params = {'fields':'cases.submitter_id,file_id,file_name,file_size'}
    response = requests.get(files_endpt, params = params)
    json_request = json.dumps(response.json(), indent=2)
    
    # Find the ENTITY_ID and append to the list
    Entity_ID_list.append(json_request[json_request.find('"submitter_id": "') + len('"submitter_id": "'):json_request.find('"\n')]) 

# Display Entity_ID_list
UUID_list['Entity_ID'] = Entity_ID_list
UUID_list.tail(5)

# Convert back to CSV
UUID_list.to_csv(csv_filename, index=False)
