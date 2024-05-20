import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import csv

#Get an YouTube Data API key from Google Cloud Console (google it!)
api_key = input('Get an YouTube Data API key from Google Cloud Console (google it!): ')
playlist_id = input('Enter in your playlist ID (get it from url): ')

youtube = build('youtube', 'v3', developerKey=api_key)
video_links = []

next_page_token = None

while True:
    request = youtube.playlistItems().list(
        part='snippet',
        maxResults=50,  # You can adjust this as needed, but the max is 50 per request
        playlistId=playlist_id,
        pageToken=next_page_token  
    )

    response = request.execute()

    for item in response['items']:
        video_links.append(f'https://www.youtube.com/watch?v={item["snippet"]["resourceId"]["videoId"]}')

    next_page_token = response.get('nextPageToken')

    if not next_page_token:
        break

#name the .txt file to your liking
with open('v_links.txt', 'w', newline='') as file:
    writer = csv.writer(file)
    for link in video_links:
        writer.writerow([link])
