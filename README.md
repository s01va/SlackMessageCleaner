# SlackMessageCleaner

## How to use
1. Create new App in [here](https://api.slack.com/apps)
2. Settings > OAuth & Permissions


    Scopes
    > Bot Token Scopes:
    > > channels:history, chat:write
    
    > User Token Scopes:
    > > channels:history, chat:write

    and get your "User OAuth Token"


3. Return this project, Input your "User OAuth Token" in .env
4. Input channel ID to delete messages in channels_info.csv