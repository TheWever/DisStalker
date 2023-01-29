# General
- Make sure that you have an open direct message with the user you want to receive notifications from

# Installation
- Download [python 3.10](https://www.python.org/downloads/release/python-3109/)
- Add python and pip to your path
- Install requirements by running `pip install -r requirements.txt`
- Get your bot's token by opening discord in your browser, opening the dev console (ctrl+shift+i) and then running following command in your console `(webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()`
- Copy the result, remove the leading and trailing apostrophe and paste it into token.txt
- Put all the users you want to receive notifications for into users.txt and split them using newlines
- Now start the bot by running following command in your terminal `python main.py`
- Wait for the bot to initialize. `Ready!` will be printed to your console as soon as the bot has done so!

# Configurations
- If you have discord installed set `ApplicationMode=true` else `ApplicationMode=false`