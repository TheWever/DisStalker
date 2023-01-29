from winotify import Notification
from typing import Optional, Dict
from pathlib import Path
import discum
import toml

# https://pypi.org/project/winotify/
# https://github.com/Merubokkusu/Discord-S.C.U.M/tree/master/docs

PATH = Path(__file__).parent.resolve()
print(f"Running from {PATH}!")

with open(f"{PATH}/users.txt") as f:
    USERS = f.read().splitlines()

with open(f"{PATH}/token.txt") as f:
    TOKEN = f.read()

with open(f"{PATH}/config.toml") as f:
    APPLICATON_MODE = toml.load(f)["ApplicationMode"]

bot = discum.Client(
    token=TOKEN,
    log={
        "console": False,
        "file": False
    }
)

def generate_open_profile_link(user_id):
    return f"{'discord://' if APPLICATON_MODE else ''}https://discordapp.com/users/{user_id}"

def send_notification(
        action,
        content,
        links: Optional[Dict] = None
):
    toast = Notification(
        app_id="DisStalker",
        title=f"DisStalker - {action}",
        msg=content,
        icon=f"{PATH}/icon.jpeg"
    )
    if links:
        for key, value in links.items():
            toast.add_actions(
                label=key,
                launch=value
            )

    toast.show()

def get_cached_user(cache, user_id):
    for obj in cache:
        if obj["id"] == str(user_id):
            return obj

def log(*args):
    print(f"[DEBUG]: {' '.join(args)}")

@bot.gateway.command
def listener(resp):
    if resp.event.ready_supplemental:
        print("Ready!")
    if resp.event.typing:
        log(f"Received Typing Event: {resp.raw}")
        user_id = resp.raw["d"]["user_id"]
        user = get_cached_user(bot.gateway.session.cachedUsers, user_id)
        log(f"Found User: {user}")
        username = f"{user['username']}#{user['discriminator']}"
        if username in USERS:
            send_notification(
                "User typing",
                f"{username} is sending you a message!",
                {
                    "Open Profile": generate_open_profile_link(user_id),
                }
            )

bot.gateway.run()
