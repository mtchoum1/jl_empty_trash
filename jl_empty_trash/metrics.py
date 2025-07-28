import os
from pathlib import Path

import psutil
from jupyter_server.serverapp import ServerApp

class TrashMetricsLoader:
    def __init__(self, jsapp: ServerApp):
        self.config = jsapp.web_app.settings["jl_empty_trash_config"]
        self.jsapp = jsapp