#    This file is part of the AutoAnime distribution.
#    Copyright (c) 2023 Kaif_00z
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/kaif-00z/AutoAnimeBot/blob/main/LICENSE > .

from decouple import config


class Var:
    # Telegram Credentials

    API_ID = config("API_ID", default=27439235, cast=int)
    API_HASH = config("API_HASH", default="9aacd83986ff92a2c7ea0fc284477b07")
    BOT_TOKEN = config("BOT_TOKEN", default=7109524997:AAHF2haxOGuuGjQJsoXCUejD7nZ9OO9Uv1g)

    # Database Credentials

    REDIS_URI = config("REDIS_URI", default=redis-17412.c11.us-east-1-2.ec2.cloud.redislabs.com:17412)
    REDIS_PASS = config("REDIS_PASSWORD", default=Yp5riG0NPToq6yWAAJOfWLDrxg3yVsrf)

    # Channels Ids

    BACKUP_CHANNEL = config("BACKUP_CHANNEL", default=-1001979732311, cast=int)
    MAIN_CHANNEL = config("MAIN_CHANNEL", default=-1001979732311, cast=int)
    LOG_CHANNEL = config("LOG_CHANNEL", default=-1001979732311, cast=int)
    CLOUD_CHANNEL = config("CLOUD_CHANNEL", default=-1002135913588, cast=int)
    OWNER = config("OWNER", default=5971676967, cast=int)

    # Other Configs

    THUMB = config(
        "THUMBNAIL", default="https://telegra.ph/file/587e78b1375927d0cd3b8.jpg"
    )
    FFMPEG = config("FFMPEG", default="ffmpeg")
    SEND_SCHEDULE = config("SEND_SCHEDULE", default=True, cast=bool)
    RESTART_EVERDAY = config("RESTART_EVERDAY", default=True, cast=bool)
