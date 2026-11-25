import sys, json; sys.path.insert(0, '/home/claude/goualart/piscine/_outils')
from mail_templates import signature_html, signature_text
OUT = '/tmp/claude-0/-home-claude-goualart/b0b889aa-c26f-5072-a767-0b5a6fe05228/scratchpad/mails.json'
RAW = 'https://raw.githubusercontent.com/mane458957-maker/goualart/main/'
import json as _j
_N={'al-farhan-landscape':'Al-Farhan Landscape','green-heaven-landscape':'Green Heaven Landscape','ceri-jo-landscaping':'Ceri Jo Landscaping','uh-pools-and-gardens':'UH Pools and Gardens','green-image-landscaping':'Green Image Landscaping'}
M = [(p['slug'], _N.get(p['slug'],p['name']), p['email'], p['city'], p['weak_point']) for p in _j.load(open('/home/claude/goualart/piscine/_outils/prospects_2026_11_25.json')) if p.get('send')]
B = 'font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:1.6;color:#0b1620'
out = []
for slug, co, to, city, weak in M:
    url = f'https://studio.goual.fr/piscine/{slug}/'
    subj = f'{co}: your new website is ready'
    p1 = f"I took the liberty of redesigning your website, to show what {co} could offer its clients:"
    feats = ["homeowners pick their pool model and tile finish", "they switch from day to night and turn on the pool lights", "they see the result right away in a real villa"]
    btn = f'Open the {co} demo'
    offer = "<b>Current offer: AED 2,500, all included</b> (domain connection, professional email, small adjustments)."
    offer_t = "Current offer: AED 2,500, all included (domain connection, professional email, small adjustments)."
    end = f"I'm based in Dubai and happy to meet you in person in {city}, or to walk you through it on a call or on WhatsApp.<br><br>Best regards,<br>Mohammed Goual"
    end_t = end.replace('<br>', '\n')
    li = ''.join(f'<li>{f}</li>' for f in feats)
    html = (f'<div style="{B};max-width:620px"><p>Hello,</p><p>{p1}</p><ul style="padding-left:20px;margin:0 0 14px">{li}</ul>'
            f'<p style="margin:18px 0"><a href="{url}"><img src="cid:apercu" alt="{btn}" width="560" style="width:100%;max-width:560px;border-radius:12px;border:1px solid #e3e8ee;display:block"></a></p>'
            f'<p style="margin:18px 0"><a href="{url}" style="background:#2bb3c0;color:#fff;text-decoration:none;padding:12px 22px;border-radius:999px;font-weight:bold;display:inline-block">{btn}</a></p>'
            f'<p>{weak}</p><p>{offer}</p><p>{end}</p>{signature_html("en")}</div>')
    text = f"Hello,\n\n{p1}\n" + ''.join(f"- {f}\n" for f in feats) + f"\n{btn}: {url}\n\n{weak}\n\n{offer_t}\n\n{end_t}\n\n{signature_text('en')}\n"
    out.append(dict(slug=slug, to=to, subject=subj, html=html, text=text,
        attachments=[{"filename":"apercu.jpg","url":RAW+f"piscine/{slug}/apercu.jpg","contentId":"apercu"},
                     {"filename":"goual-studio-logo.png","url":RAW+"img/goual-studio-logo.png","contentId":"logo"}]))
json.dump(out, open(OUT,'w'), ensure_ascii=False, indent=0)
print(len(out))
