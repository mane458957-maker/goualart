# Démos vague FR/US du 25/11/2026 (générateur générique gen.py)
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gen import build
for P in json.load(open(os.path.join(os.path.dirname(__file__), 'prospects_2026_11_25_fr_us.json'))):
    build(P)
