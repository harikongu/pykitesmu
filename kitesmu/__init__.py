from six import StringIO, PY2
import ssl
import csv
import time
import json
import struct
import hashlib
import logging
import requests
import threading

import websocket

# Initialize logger
logger = logging.getLogger(__name__)


class KiteSimulator(object):
	"""
	The API client class. In simulation, you may initialise
	a single instance of this class per `api_key`.
	"""

