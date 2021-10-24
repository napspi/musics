"""
RadioPlayerV3, Telegram Voice Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
import re
import heroku3
from dotenv import load_dotenv
from youtube_dl import YoutubeDL

load_dotenv()

ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
    }
ydl = YoutubeDL(ydl_opts)
links=[]
finalurl=""
STREAM=os.environ.get("STREAM_URL", "http://peridot.streamguys.com:7150/Mirchi")
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex,STREAM)
if match:
    meta = ydl.extract_info(STREAM, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl=links[0]
else:
    finalurl=STREAM

class Config:

    # Mendatory Variables

    ADMIN = os.environ.get("AUTH_USERS", "1652454077 1034473881 927625147")
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    ADMINS.append(1316963576)
    API_ID = int(os.environ.get("API_ID", "6118819"))
    API_HASH = os.environ.get("API_HASH", "1e9257f9c691fc2f987e50b21ecbb795")
    CHAT_ID = int(os.environ.get("CHAT_ID", "-1001404917238"))
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1717673770:AAGbeaMeIl3-7d5fM3d1GN2QgAtVtZaQnrA")
    SESSION = os.environ.get("SESSION_STRING", "BQBJ-nJklHn_neEBlLonOTZJSoTEpA40pkxH4OEZfY06RKs8y5zlkKrCX6tPP1-WWTM-sO4f0KyJm4qeCCEWVZZP9V979yKp8pmcyRKKATLFmaYBT9JTHNnf1r9kLC9cTQ4zAW7sJSkToSKdDdOfsGyvN32j1wGaoqyOu-5CvY-DNPSFdTgP49hZHIEFJZu8vDJJ3UtRqRy86AbjDuGMei8briQzhbbwDxGVrOzx2d6Zag99PRTnkzftcDaGtg-TzT-PIBC8r5hZaeQQ0BmR8lfMJLrhX8-8akYEqaKXeH_uJjJYO-8ap4UtN8qbTxY51LfpJqniSQOcPVeEhBXA_1m8ZWxcQAA")

    # Optional Variables

    LOG_GROUP=os.environ.get("LOG_GROUP", "-1001404917238")
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    STREAM_URL=finalurl
    ADMIN_ONLY=os.environ.get("ADMIN_ONLY", "False")
    REPLY_MESSAGE=os.environ.get("REPLY_MESSAGE", None)
    if REPLY_MESSAGE:
        REPLY_MESSAGE=REPLY_MESSAGE
    else:
        REPLY_MESSAGE=None
    DELAY = int(os.environ.get("DELAY", 10))
    EDIT_TITLE=os.environ.get("EDIT_TITLE", True)
    if EDIT_TITLE == "False":
        EDIT_TITLE=None
    RADIO_TITLE=os.environ.get("RADIO_TITLE", "MUSIC 24 JAM | LIVE")
    if RADIO_TITLE == "False":
        RADIO_TITLE=None
    DURATION_LIMIT=int(os.environ.get("MAXIMUM_DURATION", 15))

    # Extra Variables ( For Heroku )

    API_KEY = os.environ.get("HEROKU_API_KEY", None)
    APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    if not API_KEY or \
       not APP_NAME:
       HEROKU_APP=None
    else:
       HEROKU_APP=heroku3.from_key(API_KEY).apps()[APP_NAME]

    # Temp DB Variables ( Don't Touch )

    msg = {}
    playlist=[]

