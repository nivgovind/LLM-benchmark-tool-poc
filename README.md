
# Assignment1

  
  

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



# Ref


# Deliverables

1. GitHub Repo Link with
# About

## Architecture

## UI 

## Visualizations




b. [Codelabs Document](https://docs.google.com/document/d/12x51PlTxUmD6F9uAui8ZyoWTlUt4VTFP3YCYAvrLZq4/edit?usp=sharing)

c. Video of the submission (5 minutes)

d. Link to working application

e. GitHub project

  

2. Checklist

1. Required attestation and contribution declaration on the GitHub page:

```

WE ATTEST THAT WE HAVEN’T USED ANY OTHER STUDENTS’ WORK IN OUR

ASSIGNMENT AND ABIDE BY THE POLICIES LISTED IN THE STUDENT HANDBOOK

Contribution:

a. member1: 33%

b. member2: 33%

c. member3: 33%

```

2. Make sure you do not push anything to your GitHub after submission date

3. Create a Code lab document describing everything you did. In your GitHub you

should have a readme.md files which would tell what all things are there in this

GitHub repository.

4. Keep your repository private until the deadlines. In case of any plagiarism cases

both the teams which be equally held responsible

  
  

### DO NOT PUSH TO THE MAIN BRANCH

### Procedure to push code

- (first time) create a branch with your name with "main" as base

- (Every time) Pull code from main branch before making changes to your branch

- (Every time) make changes

- (Every time) commit the changes

- (Every time) push the code to "your branch"

- (Every time) Create a PR to main with the changes

  

# Detailed git instructions of above

- `git checkout "name"`

- [ ] Created "origin/deepak" for deepak

- [ ] created "origin/aish" for aish

- [ ] created "origin/niv" for niv

- [ ] created "origin/backup" for backup

- `git pull origin main`

- ALWAYS run this BEFORE YOU START WORKING ON CHANGESSSS!!!

- Note: Work on changes in your local system

- `git add .`

- `git commit -m "What changes desc"`

- Note: Good practice is frequent commit so that if you fuck up, you can go back to your last save/commit

- Resource: https://www.freecodecamp.org/news/git-reverting-to-previous-commit-how-to-revert-to-last-commit/

- `git push origin <branch name>`

- branch name is "deepak" for deepak

- branch name is "aish" for aish

- branch name is "niv" for niv

  

- Raise a PR to main and let me know :). We will merge once we talk through the changes

- LETS GOOO!

  

# Quickstart ref

1. https://docs.streamlit.io/develop/tutorials/databases/aws-s3

2. https://docs.streamlit.io/develop/tutorials/multipage

3. https://docs.streamlit.io/develop/api-reference/charts/st.plotly_chart