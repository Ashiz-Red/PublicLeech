#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) PublicLeech Author(s)
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from tobrot.get_cfg import get_config


class Commandi:
    LEECH = get_config(
        "COMMANDI_LEECH",
        "leech@Barbara_Ann_Minerva_bot"
    )
    PURGE = get_config(
        "COMMANDI_PURGE",
        "purge@Barbara_Ann_Minerva_bot"
    )
    YTDL = get_config(
        "COMMANDI_YTDL",
        "ytdl@Barbara_Ann_Minerva_bot"
    )
    STATUS = get_config(
        "COMMANDI_STATUS",
        "status@Barbara_Ann_Minerva_bot"
    )
    CANCEL = get_config(
        "COMMANDI_CANCEL",
        "cancel@Barbara_Ann_Minerva_bot"
    )
    EXEC = get_config(
        "COMMANDI_EXEC",
        "exec@Barbara_Ann_Minerva_bot"
    )
    EVAL = get_config(
        "COMMANDI_EVAL",
        "eval@Barbara_Ann_Minerva_bot"
    )
    RENAME = get_config(
        "COMMANDI_RENAME",
        "rename@Barbara_Ann_Minerva_bot"
    )
    UPLOAD = get_config(
        "COMMANDI_UPLOAD",
        "upload@Barbara_Ann_Minerva_bot"
    )
    HELP = get_config(
        "COMMANDI_HELP",
        "help@Barbara_Ann_Minerva_bot"
    )
    SAVETHUMBNAIL = get_config(
        "COMMANDI_SAVETHUMBNAIL",
        "savethumbnail@Barbara_Ann_Minerva_bot"
    )
    CLEARTHUMBNAIL = get_config(
        "COMMANDI_CLEARTHUMBNAIL",
        "clearthumbnail@Barbara_Ann_Minerva_bot"
    )
    GET_RCLONE_CONF_URI = get_config(
        "COMMANDI_GET_RCLONE_CONF_URI",
        "getrcloneconfuri@Barbara_Ann_Minerva_bot"
    )
    UPLOAD_LOG_FILE = get_config(
        "COMMANDI_UPLOAD_LOG_FILE",
        "log@Barbara_Ann_Minerva_bot"
    )
