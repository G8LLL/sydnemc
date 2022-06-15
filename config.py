## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgBnfR37w0DGJwQk9onaFS2qUDmbA2VwC4MjNRz56UTiyFQwd79-wxQ73HdtJ3v3U4LtwwsCrhNJsHMvfbnVy_WW23a7ggcgWLELZ9SF17ARFswN9OnDc_elwo2LWg1Tf42JbT9pDxOG5cJf9kuxK1JLpvFKXyQGLkp-iEhwuMjUlNw3pgvs1odDqHPUfrdkDkk9JIt3oiXNjIZ1G088X_k1V0uAoMOYFxozWshWBrnd60hl5F_EFx5TXECoQxYoY6KVlwY7TZ4p-yACMCoNN6dRIyX3anb1Ueau6EBcL5i2yKDCAolMKcSQ5G8aqg7GGmNYmUMZtut3eeKbymReGlKXQZJQowA")
BOT_TOKEN = getenv("BOT_TOKEN", "5485049160:AAF_3gmebNs1mmAH2cghp23haCQrb6o3NcY")
BOT_NAME = getenv("BOT_NAME", "song")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "RoD")
OWNER_USERNAME = getenv("OWNER_USERNAME", "G8LLL")
ALIVE_NAME = getenv("ALIVE_NAME", "RoD")
BOT_USERNAME = getenv("BOT_USERNAME", "sydnemcbot")
OWNER_ID = getenv("OWNER_ID", "1100107939")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "G8LLL")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "zzzz5r")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "zzzz5r")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1100107939").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
