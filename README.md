# Spotify-time-machine
__*“Music is the closest thing we have to a time machine”*__

Want to go back in time and listen to popular songs of that time? With a bit of web scraping, it is possible search/create a playlist of top songs in spotify with any given date in the last 20 years.

### Where does the idea come from?

This is one of the projects in the 100 days of python challenge - here is the [link](https://100daysofpython.dev/).

### How does it work?


This script would scrap for top 100 billboard songs on user's input date. Then it would create a spotify playlist with following title format "hot-100-'input-date'"

To set it up please follow "getting started" in this [git repo](https://github.com/tduong10101/spotify-time-machine). Here is an overview flow:

![Overview](/img/spotify-time-machine.jpg)


### Requirements

- Python 3
- Spotify account

### Getting Started

1. Clone this repo:

```
git clone https://github.com/tduong10101/spotify-time-machine
```
2. Navigate to the cloned folder and install the requirement modules:
```
pip install -r requirements.txt
```
3. Create Spotify following this [link](https://developer.spotify.com/documentation/general/guides/app-settings/) with redirect URIs set as: https://blog.tdinvoke.net/

4. Put your spotify app client id, client secret and user id to default-cred.json

```
{
    "CLIENT_ID":"<your-spotify-client-id>",
    "CLIENT_SECRET":"<your-spotify-client-secret>",
    "USER_ID":"<your-spotify-user-id>"
}
```

5. Once the above is set, run main.py
```
python main.py
```
6. Input the date you'd like to get the 100 songs on. If everything is set correctly, a spotify approve page will pop up as below screenshoot:

![Approve App](/img/spotify_approve.JPG)

7. Hit 'Agree', it would take you to the redirect site which is https://blog.tdinvoke.net/. Copy the whole URL as below:

![URL copy](/img/url_copy.JPG)

8. Paste the link to the running terminal:

![URL paste](/img/paste_url.JPG)

Note: Step 6-8 only need to be done once. The script will create a token.txt for authenticate after first run.

9. Enjoy the playlist! 🎧