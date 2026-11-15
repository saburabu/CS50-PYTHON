from folder_a.calculator import add
from pathlib import Path

print(add(20, 30))

PROJECT_ROOT = Path(__file__).resolve().parent

print(PROJECT_ROOT)