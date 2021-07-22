# This script is intended to prepare PDFs (and hopefully other file formats) into the recommended JSONL format
# for Google Cloud's AutoML, etc.

# myList is a list of GCP bucket URI's.
# Example: ['gs://data/pdf_folder/example.pdf']
# You need to follow this template for referencing PDFs.
# https://cloud.google.com/natural-language/automl/docs/prepare?_ga=2.242251782.-501459144.1569194771
import os

# If you want to reference a gs://... link in your bucket and are not sure of the format, it is generally
# gs://name-of-bucket/name-of-folder/name-of-file
mylist = []
template = '{"document": {"input_config": {"gcs_source": {"input_uris": [ "%s" ]}}}}'


def getName(filepath):
    # helper function to get the file name without the .pdf part and the folder path
    index = filepath.rfind('/')
    return filepath[index:-4]


if not os.path.exists('jsonl'):
    os.mkdir('jsonl')  # should make folder titled 'jsonl' inside the same directory this script is launched in
    print("Folder jsonl created.")
else:
    print("Folder 'jsonl' already exists.")

index = 0
for filepath in mylist:
    todump = template % filepath
    # this will put all your JSONL files in a folder "JSONL" and the file names will be
    with open("jsonl" + getName(filepath) + '.jsonl', 'w', encoding='utf-8') as f:
        f.write(todump + '\n')
    index += 1
print(("wrote {} JSONL documents to " + os.getcwd() + " !").format(index))
