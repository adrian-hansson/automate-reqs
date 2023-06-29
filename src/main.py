import pandas as pd
import nltk
import os
import datetime
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from shutil import copyfile

REQUIREMENT_NUMBER: str = 'Title'
REQUIREMENT_TITLE: str = 'RequirementTitle'

# ensure NLTK data is available
nltk.download('punkt')
nltk.download('stopwords')

# Define the source and target Excel file paths
src_file = "data/input/data.xlsx"
tgt_file = f"data/output/data_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.xlsx"
copyfile(src_file, tgt_file)  # make a copy of the source file

# Read data from the source Excel file
xls = pd.ExcelFile(tgt_file)

# Load the sheets into dataframes
requirements_df = pd.read_excel(xls, 'requirements')
integrations_df = pd.read_excel(xls, 'integrations')
systems_df = pd.read_excel(xls, 'systems')

# Filter out cancelled requirements
requirements_df = requirements_df[~requirements_df['Status'].str.contains('Cancelled')]

# Define keywords for identifying integrations and systems
integration_keywords = [
    'communicate',
    'exchange data',
    "exchange",
    "expose",
    "api",
    "integrate",
    "integration",
    "interface",
    "interfacing",
    "interoperability",
    "interoperable",
    "interoperating",
    "interoperates",
    "interoperating",
    "interoperated",
    "interoperates",
    "http",
    "call",
    "non-functional",
    "nonfunctional"
]
system_keywords = systems_df['id'].tolist() + systems_df['name'].tolist()

# Define a function to check if a sentence contains any of the specified keywords
def contains_keywords(sentence, keywords):
    sentence_words = set(word_tokenize(sentence))
    return any(keyword in sentence_words for keyword in keywords)

# Analyze requirements to identify integrations and systems
for i, requirement in requirements_df.iterrows():
    if contains_keywords(requirement[REQUIREMENT_TITLE], integration_keywords):
        # If integration keywords are found, add a new row to the integrations dataframe
        integrations_df = integrations_df.append({'source': '', 'target': '', 'method': '', 'trigger': '', 'action': '', 'requirement': requirement[REQUIREMENT_NUMBER]}, ignore_index=True)
    if contains_keywords(requirement[REQUIREMENT_TITLE], system_keywords):
        # If system keywords are found, add a new row to the systems dataframe
        systems_df = systems_df.append({'id': '', 'name': '', 'parent': '', 'requirement': requirement[REQUIREMENT_NUMBER]}, ignore_index=True)

# Write the dataframes back to the Excel file
with pd.ExcelWriter(tgt_file, engine='openpyxl', mode='a') as writer:
    requirements_df.to_excel(writer, sheet_name='requirements', index=False)
    integrations_df.to_excel(writer, sheet_name='integrations', index=False)
    systems_df.to_excel(writer, sheet_name='systems', index=False)