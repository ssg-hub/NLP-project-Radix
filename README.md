<div align = "center">

<h3>Becode AI training

group assignment: PDF parsing and data extraction with NLP</h3>


<img width = "200" src = /assets/BeCode_Logo.png>
</div>

# NLP-project-Radix
Radix offered a usecase, for which we extract relevant data from resumes using NLP.
Further down the road, these data can be used to match the right resumes with job offers.

## Table of contents
[Description](#Description)  
[Installation](#Installation)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Idea](#Idea)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Used libraries](#Used-libraries)  
[Usage](#Usage)  
[Output](#Output)  
[How it works](#How-it-works)  
[Examples](#Examples)  
[Authors](#Authors)


## Description
The client - Radix - wants to be able to parse free-form PDFs that they get from their own resources.
From those PDFs, they want to extract the most important data.  

Personal details:  
- name of the applicant
- phone number and e-mailaddress
- date of birth
- languages spoken
  
Professional details:  
- Skills and education
- Experience and the most recent job title  

The goal is to be able to arrange the resumes into classes or clusters, compare the professional details
to those of other candidates, and most of all: link them to the right job offers.

<div align = "center">
<img width = "200" src = /assets/logo_radix.png>
</div>

## Installation
On this level we can be short: the only thing you can do for now with the code as a program
on itself, is parsing a random number of application files (PDF format) and pooring the information
into three dataframes (dfs, using Pickle). A general df, one that contains the personal info,
and a third one with the professional background.

To run this function, clone the repository main branch, and run the main.py file.
```
git clone [name_repo]
cd [path/to/repo/NLP-project-Radix/utils]
python main.py
```

Next to that, we also have a function ready that allows you to access one of the three 
dataframes and select a skill, education of work experience. To run this, enter in the command line:
```
cd [path/to/repo/NLP-project-Radix/utils]
python modeling.py
```

### &nbsp;&nbsp;&nbsp;&nbsp;Idea
For further development, the following steps should be rather easy to take. 

To start with, parts of the program could be used in order to parse job offers and put those into a df.
An application can be developed that allows customers to upload either their resume or a job offer,
which is then added to the dataframe. 

That way it should be fairly easy to link the requirements from the job offers to the skills, experience
and education of applicants. When the job vacancy has been filled or the applicant found a job, they can
click a button to take their file out of the running for being matched.

### &nbsp;&nbsp;&nbsp;&nbsp;Used libraries
For this project we made extensive use of the libraries nltk, pandas, fitz, requests, regex, spacy and
fuzzywuzzy.

## Usage
Due to the restricted time available to finish this project (two weeks), we have been focussing
on extracting the data themselves from the resumes and putting those in dataframes (dfs).
The parsing of PDFs in itself has proven to be a challenge, so most of the time went to that.
That resulted in three easily accessible dataframes with the content of 250 resumes. There is
a general df, one that stores the personal details, and one specifically for the professional ones.

We also already developed a function that makes it possible to give a dataframe.pkl and a skill,
education, or experience as input. The function then runs through the database and gives back 
the resumes that contain the requested skill, education or experience. It's also possible to see
the content of the column of the matching resumes, which makes it even easier to select and handpick
the ones you want full access to, in order to retrieve e.g. personal contact information.

## Output
The output of the programs is quite straightforward. The main module creates the dataframes out of
an undefined number of seperate resumes (PDF), that are immediately converted into .pkl files
in order to store them. These dfs contain contact information and professional background features.
The result in the terminal looks like this:

<img width = "400" src = /assets/email.png>


<img width = "400" src = /assets/hobbies.png>



The modeling module makes it possible to access those .pkl and with your query of one skill,
language, educational level, ... you get a list of resumes back that at least *contain* this query.
You can ask for more information (i.e.: the whole content of the column in which the query was found),
a W-score and the index in the df. The result - in the terminal - looks like this:

<img width = "600" src = /assets/Image_modeling.png>

## How it works
The PDFs are dropped in a folder that is then pulle through a process in which they are parsed. The parsed
parts are then tokenized per word or per string, depending on its purpose. The tokens are cleaned up (by use
of libraries, lists and API), and then linked to the correct column in the dataframe.

The dataframe can then be accessed with fuzzywuzzy in order to get the queries out of the requested database.

## Authors
Shilpa Singhal - PM - dev/doc  
Pauwel De Wilde - dev/doc