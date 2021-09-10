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


## <span style="color:blue"><em>Description</em></span>
The client - Radix - wants to be able to parse free-form PDFs that they get from their own resources. From those PDFs,
they want to extract the most important data.  

Personal details:  
- name of the applicant
- phone number and e-mailaddress
- date of birth
- languages spoken
  
Professional details:  
- Skills and education
- Experience and the most recent job title  

The goal is to be able to arrange the resumes into classes or clusters, compare the professional details to those
of other candidates, and most of all: link them to the right job offers.

<div align = "center">
<img width = "200" src = /assets/logo_radix.png>
</div>

## Installation
On this level we can be short: the only thing you can do for now with the code as a program on itself, is parsing
a random number of application files (PDF format) and pooring the information in a dataframe (Pickle).

To run this function, clone the repository main branch, and run the main.py file.
```
git clone [name_repo]
cd [path/to/repo]
python main.py
```
Due to the restricted time available to finish this project (two weeks), we have been focussing on extracting
the data from the resumes and putting those in dataframes (dfs). The parsing of PDFs in itself has proven to be a challenge in
itself, so most of the time went to that. That resulted in three easily accessible dataframes (df) with the content of 250
resumes. There is a general df, one that stores the personal details, and one specifically for the professional ones.

### Idea
For further development, the following steps should be rather easy to take. 

To start with, parts of the program could be used in order to parse job offers and put those into a df. An application can be developed
that allows customers to upload either their resume or a job offer, which is then added to the dataframe. That way it should be fairly
easy to link the requirements from the job offers to the skills, experience and education of applicants. When the job vacancy has been filled
or the applicant found a job, they can click a button to take their file out of the running for being matched.

### Used libraries


## Usage


## Output


## How it works

## Examples

## Authors