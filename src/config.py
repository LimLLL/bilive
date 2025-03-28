# Copyright (c) 2024 bilive.

import os
from pathlib import Path
from datetime import datetime
import configparser
from db.conn import create_table

# ============================ Your configuration ============================
GPU_EXIST=True
# Can be pipeline, append, merge
MODEL_TYPE = "append"
Inference_Model = "small"
# ============================ The video slice configuration ==================
AUTO_SLICE = False
SLICE_DURATION = 30
# The minimum video size to be sliced (MB)
MIN_VIDEO_SIZE = 200
# Apply for your own GLM-4v-Plus API key at https://www.bigmodel.cn/invite?icode=shBtZUfNE6FfdMH1R6NybGczbXFgPRGIalpycrEwJ28%3D
Your_API_KEY = ""
# ============================ Basic configuration ============================
SRC_DIR = str(Path(os.path.abspath(__file__)).parent)
BILIVE_DIR = str(Path(SRC_DIR).parent)
LOG_DIR = os.path.join(BILIVE_DIR, 'logs')
VIDEOS_DIR = os.path.join(BILIVE_DIR, 'Videos')
DanmakuFactory_bin = os.path.join('utils', 'DanmakuFactory')
DanmakuFactory_PATH = os.path.join(SRC_DIR, DanmakuFactory_bin)
# Prevent create a new BV number after streamer changes the streaming title in thesame day
IGNORE_ROOM_TITLE = False


if not os.path.exists(SRC_DIR + '/db/data.db'):
    print("初始化数据库")
    create_table()

if not os.path.exists(VIDEOS_DIR):
    os.makedirs(VIDEOS_DIR)
if not os.path.exists(VIDEOS_DIR + '/upload_conf'):
    os.makedirs(VIDEOS_DIR + '/upload_conf')

def get_model_path():
    SRC_DIR = str(Path(os.path.abspath(__file__)).parent)
    model_dir = os.path.join(SRC_DIR, 'subtitle', 'models')
    model_path = os.path.join(model_dir, f'{Inference_Model}.pt')
    return model_path

def get_interface_config():
    interface_config = configparser.ConfigParser()
    interface_dir = os.path.join(SRC_DIR, 'subtitle')
    interface_file = os.path.join(interface_dir, "en.ini")
    interface_config.read(interface_file, encoding='utf-8')
    return interface_config