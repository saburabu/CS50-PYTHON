from pathlib import Path
import sys

father_folder = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(father_folder))

from folder_a.calculator import add

def generate_report():
    print("Report generated")

print(add(100, 200))