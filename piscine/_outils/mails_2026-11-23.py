import sys, json; sys.path.insert(0, '/home/claude/goualart/piscine/_outils')
from mail_templates import signature_html, signature_text
OUT = '/tmp/claude-0/-home-claude-goualart/ac8b6b28-613b-59f6-a94a-e37e4f72386e/scratchpad/mails.json'
RAW = 'https://raw.githubusercontent.com/mane458957-maker/goualart/main/'
M = [
 ('rak-aqua-pools','Aqua Pools','info@aquapools.ae','Sharjah',"One thing I noticed on your current site: the homepage description still calls Aqua Pools \"A Trusted interior Design Company In Dubai\", and the same paragraph says both \"over 10 years\" and \"over 80 years\"."),
 ('aqua-safe-pool','Aqua Safe','info@aqua-safepool.com','Sharjah',"One thing I noticed on your current site: the footer still shows 2024, the reviews heading reads \"Testmonials\" and the first paragraph repeats itself. Small things, but clients notice them."),
 ('gardenland-landscapes','GardenLand Landscapes','info@gardenland.ae','Al Ain',"One thing I noticed on your current site: the social icons still point to Odoo's placeholder \"your-page\" links and the footer phone dials a +1 555 demo number, so some visitors can't reach you."),
 ('swimming-pool-experts','Swimming Pool Experts','swimmingpoolexperts.ae@gmail.com','Dubai',"One thing I noticed on your current Google Sites page: there is no contact form, so a homeowner who finds you late at night has no simple way to ask for a quote."),
 ('naser-hayat-landscape','Naser Hayat Landscape','naserhayatlandscapellcspc@gmail.com','Abu Dhabi',"One thing I noticed on your current site: the \"Call for help\" button uses a broken \"tel:tel:\" link, and the map link on the contact page opens Melbourne, Australia instead of Mussafah."),
 ('ecoflow-pools','EcoFlow Pools','info@ecoflowpools.com','Abu Dhabi',"One thing I noticed on your current site: the \"Services\" and \"Features\" menu items are swapped, and the gallery photos have no captions (only file names like \"5_Image58\")."),
 ('acacia-landscaping-pools','Acacia Landscaping and Swimming Pools','info@acacialandscapingandpools.ae','Dubai',"One thing I noticed on your current site: the footer stops at © 2019-2024 and the \"Request a quote\" button leads nowhere, which is a pity with 20 years of projects like yours."),
 ('waves-pools','WAVES Pools','info@wavespools.com','Dubai',"One thing I noticed on your current site: the reviews section still shows the theme's demo testimonials (\"Daniel Mark, Envato\") and the clients block shows placeholders like \"client-6\"."),
 ('al-qamar-pools','Al Qamar Pools','support@alqamargroup.com','Ras Al Khaimah',"One thing I noticed on your current site: the \"0%\" loader text stays in the page and several buttons (\"Contact Tech\", \"Report Issue\") lead nowhere."),
]
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
