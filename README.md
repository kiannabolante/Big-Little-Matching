# Big-Little-Matching
Big/Little Matching algorithm for UW ACM

Installation
  - Install Python3
      https://www.python.org/downloads/
  - Install Pip
      https://pip.pypa.io/en/stable/installing/
  - Please read through this documentation on GSpread (the library we are going to be using): https://docs.gspread.org/en/latest/
  - Install GSpread
      pip install gspread

Set Up
  - Create copies of the little sign-up sheet and the big sign-up sheet
  - Create a new document to store the matches
  - Share created documents with "client-email" from client_secret.json
  - Change "little_sheet", "big_sheet", and "matches" with the names of the created documents
  
Running the program
  - python3 spreadsheet.py

Current TODOS:
  - In the Google Form (collab with social event coordinators)
      - For class standing, please ask for "current class standing" and 5 options (Freshman, Sophomore, Junior, Senior, BS/MS) or "year in the Allen School". 
      - For interests, try to figure out a way to make it more uniform because the matching script will be matching on interests 
        (ex: always using ATLA vs. Avatar The Last Airbender)
  - Currently, the script gives 13 possible bigs for each little so it "semi-matches". The goal is to run the program and automatically match the bigs and littles.
