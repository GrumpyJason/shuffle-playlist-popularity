from googleapiclient.discovery import build
import os
import sys

yt_api_key = os.environ["YT_API_KEY"]
youtube = build("youtube", "v3", developerKey=yt_api_key)
sys.stdout.reconfigure(encoding="utf-8")


def sort_yt_playlist(pl_id):
    nextPageToken = None
    videos = []

    while True:
        #pl_req finds yt playlist based on playlist id and return content
        pl_req = youtube.playlistItems().list(
                part="contentDetails",
                playlistId=pl_id,
                maxResults=50,
                pageToken=nextPageToken
            )
        pl_res = pl_req.execute()

        vid_ids = []
        for vid in pl_res["items"]:
            vid_ids.append(vid["contentDetails"]["videoId"])

        vid_req = youtube.videos().list(
            part="statistics, snippet",
            id=",".join(vid_ids)
        )
        vid_res = vid_req.execute()

        for vid in vid_res["items"]:
            videos.append([vid["snippet"]["title"], int(vid["statistics"]["viewCount"])])
            
        nextPageToken = pl_res.get("nextPageToken")
        if not nextPageToken:
            break

    videos = sorted(videos, key=lambda x: (x[1], x[0]), reverse=True)
    return videos


#print(sort_yt_playlist("OLAK5uy_mLUweaxxD1iTEVCs_I-V2k5qmSHjQgVns"))