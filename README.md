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
  - Highly recommend using Jupyter's Notebook. However, you can use Visual Studio Code or other IDEs 

Set Up
  - Create copies of the little sign-up sheet and the big sign-up sheet
  - Create a new document to store the rankings of bigs (i.e. potential matches) and another to store the actual matchess
  - Share created documents with "client-email" from client_secret.json
  - Change the Bigs Respsonse Form to "big_sheet" and Littles Responses Form to "little_sheet" so the client can find the correct sheets
  - Name the new sheet called "matches" (i.e. rankings of bigs against each little) and name the other sheet "Big / Little Pairing" to get each Littles paired to each Big
  - Look through the "Big_Little_Matching.ipynb" or the "Big_Little_Matching.py" code and familarize with yourself with the code
    - Use the ipynb file if you are using Jupyter Notebook and py file if you are using VSCode or other IDE
    - The PDF is just for simple viewing!
  - If you run into an import error for oauth2client.service_account for pyparsing, call "pip install -U httplib2" in command line
  - There may be other bugs due to dependencies -- always use google and get answers from github, stackoverflow, or other forums

IMPORTANT: Make sure to check the code again to avoid any bugs
- If you changed the question format and its order in the Google Forms, this is especially important to make sure all the questions between the bigs and littles line up. Be wary of 0 indexing for lists! 
- For example, if you parsing through each littles and bigs (i.e. each row in the spreadsheet), make sure to check that the rows match up. For example, the question about technical interests for littles might be on column 15 but the same question for bigs might be on column 16. The column index can shift if you were to add another question before that technical interest questions. 
- After checking, go through the point system to see which questions should be prioritized. Historically, we gave *a lot* of points for demographics (i.e. gender, LGBTQ, race, background) question since participants are specifically asking to be matched to those demographics. 
  
Running the program
  - Run on Jupyter's Notebook preferably so you have the most control executing each cell (i.e. snippets of code) rather than the whole script
 
Post-Script Checks
- Make sure your script did what you wanted. The automated matching part (latter half of the script) is not the best as it favors those who signed up first. Might be better doing some form of Gale-Shapley Algorithm in the future
- Since this is all automated, check like 5-10 pairings to see if they were paired fairly well. I would specifically check people who opted in to be paired with specific demographics. 
- Personally, I like to check the demographics in particularly and move some people around. It doesn't have to be perfect since that's nearly impossible (as we match on so many criterias). But refer to the matching rankings and move people around. 

If you have any question, please send an email to hjung10@cs.washington.edu or the current Vice Chair
