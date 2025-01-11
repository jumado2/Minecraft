import unittest
from unittest.mock import MagicMock, call
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from MyAdventures.OracleBot import run
import mcpi.block as block