import sys
from pathlib import Path

def add_tool_path():
    tool_path = Path(__file__).resolve().parents[1] / 'tools'
    sys.path.append(str(tool_path))
