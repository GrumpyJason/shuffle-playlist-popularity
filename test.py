import os
from googleapiclient.discovery import build
import sys

yt_api_key = os.environ["YT_API_KEY"]
youtube = build("youtube", "v3", developerKey=yt_api_key)
sys.stdout.reconfigure(encoding="utf-8")

pl_req = youtube.playlistItems().list(
        part="contentDetails",
        playlistId="OLAK5uy_mLUweaxxD1iTEVCs_I-V2k5qmSHjQgVns",
    )
pl_res = pl_req.execute()

vid_ids = []
for vid in pl_res["items"]:
    vid_ids.append(vid["contentDetails"]["videoId"])

vid_req = youtube.videos().list(
    part="snippet",
    id=",".join(vid_ids)
)
vid_res = vid_req.execute()
print(vid_res)