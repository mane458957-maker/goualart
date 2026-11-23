# Vague FR/US du 23/11/2026 : 4 France + 4 USA (mails) + 1 France à envoyer à la main (Berchoux)
import sys, json; sys.path.insert(0, '/home/claude/goualart/piscine/_outils')
from gen import build
SP = '/tmp/claude-0/-home-claude-goualart/4a7e4217-fc5f-5d89-bdac-ebfcb9aadca3/scratchpad/'
P = json.load(open('/home/claude/goualart/piscine/_outils/prospects_2026_11_23_fr_us.json'))
for p in P: build(p)
