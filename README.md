
# Assignment1
# About
## Links
1. [Diagrams](#diagrams)
2. [Codelabs Document](https://docs.google.com/document/d/12x51PlTxUmD6F9uAui8ZyoWTlUt4VTFP3YCYAvrLZq4/edit?usp=sharing)
3. Video of the submission (5 minutes)
4. [Working app](https://partyyy.streamlit.app/)

e. GitHub project

## Diagrams

### Architecture
![arch](images/architecture.jpeg)

### UI

#### Login page
![Login page](images/login.png)

#### Sign up page
![Sign up page](images/signup.png)

#### User chat Interface
![chat](images/chat.png)


### Visualizations

#### Response trend
![vis1](images/vis1.png)

#### Response distribution by difficulty level
![vis2](images/vis2.png)

#### Response distribution by difficulty level
![vis3](images/vis3.png)


# Setup instructions

## Pre-reqs

Poetry, ODBC driver for sql server (msodbcsql17), tesseract

## Steps

1. clone repo

```

git clone git@github.com:BigData-Fall2024-TeamA3/Assignment1.git

```

  

2. Install dependencies

```

poetry install

```

3. Create .streamlit/secrets.toml file for following

```

OPENAI_API_KEY = ""

s3_file_key_path = "path/to/your/files/"

bucket_name = ''

s3_file_key = 'path/to/your/metadata.jsonl'

s3_file_url = ''

aws_access_key_id = ''

aws_secret_access_key = ''

  

# Azure Connection details

server = ''

database = ''

username = ''

password = ''

driver = ''

  

```

  

4. Run streamlit app

```

poetry run streamlit run app.py

```

# Declaration

1. Required attestation and contribution declaration on the GitHub page:


WE ATTEST THAT WE HAVEN’T USED ANY OTHER STUDENTS’ WORK IN OUR

ASSIGNMENT AND ABIDE BY THE POLICIES LISTED IN THE STUDENT HANDBOOK

Contribution:

a. member1: 33%

b. member2: 33%

c. Nivedhithaa govindaraj: 33%


# References

1. https://docs.streamlit.io/develop
    1. https://docs.streamlit.io/develop/tutorials/multipage
    2. https://docs.streamlit.io/develop/api-reference/charts/st.plotly_chart
    3. https://docs.streamlit.io/develop/tutorials/databases/aws-s3 
2. https://learn.microsoft.com/en-us/azure/azure-sql/?view=azuresql
3. https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-examples.html
4. https://github.com/openai/openai-python