# Spotipy Challenge

This is a simple Python program that uses the Spotify Web API to search for tracks by keyword and print the results to the console.

**Check the original repository: https://github.com/spotipy-dev/spotipy**


## Getting Started
To use this program, you'll need to have Python 3 installed on your computer, as well as a Spotify developer account with a client ID and client secret. You can sign up for a free account and create a new app on the Spotify Developer Dashboard.

Once you have your client ID and client secret, you'll need to create a file called credentials.txt in the same directory as search.py, and paste your client ID and client secret into the file, one per line. It's important to keep this file secure and not share your credentials with anyone else. To prevent accidentally pushing your credentials to Git, it's recommended to add credentials.txt to your .gitignore file.

```python
your_client_id
your_client_secret
```

## Usage
To run the program, simply open a terminal or command prompt and navigate to the directory containing search.py, then type:

```python
python search.py
```

You'll be prompted to enter a search query, such as a track name or artist name. The program will then search the Spotify API for tracks matching your query, and print the results to the console.

