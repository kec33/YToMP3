# YToMP3
Youtube links (playlist) to .mp3 automated script with python

- Requirements:
  - Python3+
    - Libraries: google-api-python-client, pytube, (os, csv)

- Initial steps:
  - Go to Google Cloud Console and get yourself an Youtube (data) API key
  - Get the playlist ID that is located in the url of the playlist after the parameter '*&list='
  - Now you can deploy the scripts in the following order: 'list.py' -> 'YToMP3.py'
 
- Script deployment outcomes:
  - 'list.py' creates a text document that is filled with downloaded URL's from the wanted playlist
  - 'YToMP3.py' creates a new folder (on C: drive, default option is inside the current folder) with the downloaded .mp3 files
  - Any error's or exceptions are seen in chosen console and are self explanatory
