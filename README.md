# rewiser-gpt

A github action to manage your daily devlogs and help you revise them regularly.

## How it works?

1. Hook this github-action to your devlog repository
2. Mention the directory and file type where all the devlogs are stored
3. The action will figure out the order of the files and will use anki style algorithm to create your daily roster.
4. It will send the daily roster via email, for emails to work, it will require smtp hostname and credentials.
5. Each roster is powered by ai (for the following to work openAI key will be required and each of the following will be provided as parameter):
  1. To ease up memorization, the roster will be summarized by some memory technique like a limerick or a story or a visualisation.
  2. At the end of each roster, there will be a quiz and link for additional resources to learn.
