import sys, json; sys.path.insert(0, '/home/claude/goualart/piscine/_outils')
from mail_templates import signature_html, signature_text
OUT = '/tmp/claude-0/-home-claude-goualart/257c98d2-9208-5366-a222-6cf9ae275c3a/scratchpad/mails.json'
RAW = 'https://raw.githubusercontent.com/mane458957-maker/goualart/main/'
M = [
 ('yardman-landscaping-pools','Yardman','info@yardmandubai.com','Dubai','One thing I noticed on your current site: the design section on the homepage ends with "Our design stage includes." and the list that should follow never appears, and the headline reads "Yardman Create Arts in you Yard!".'),
 ('khawar-hanif-contracting','Khawar Hanif','info@khawarhanif.com','Dubai','One thing I noticed on your current site: the "Follow Us" icons in the contact section, and top menu items like Swimming Pool and Projects, link to "#" so they lead nowhere.'),
 ('infinite-leisure-pools','Infinite Leisure Pools','info@ilpools.ae','Dubai','One thing I noticed on your current site: the "Services" item in the main menu points to "http://Services", which is not a valid address, so visitors who click it land on an error.'),
 ('panamera-landscapes','Panamera','info@panameralandscape.com','Dubai','One thing I noticed on your current site: a leftover template line, "Enter your text here", is still visible on the pages, and the Services and Build menu items link to "#".'),
 ('star-swimming-pool','Star Swimming Pool','info@starswimmingpool.com','Sharjah',"One thing I noticed on your current site: the 'Our Projects' section on the homepage is empty, and the news block still features articles from 2017, so visitors can't see any of the pools you've actually built."),
 ('amwaj-almoheet','Amwaj Almoheet','sales@amwajalmoheet.com','Dubai',"One thing I noticed on your current site: the Facebook, Twitter and Instagram icons link to the accounts of the theme developer (Codevz) instead of Amwaj Almoheet's own pages, and the Skype icon goes nowhere."),
 ('axon-swimming-pools','Axon Pools','info@axonpools.com','Abu Dhabi','One thing I noticed on your current site: several of your projects are still titled "project 1" to "project 8", and the page title and logo text just read "Swimming Pool" instead of the Axon name.'),
 ('aqua-vision-pools','Aqua Vision Pools','info@avp-uae.com','Abu Dhabi','One thing I noticed on your current site: the four "View Detail" buttons on the home page don\'t open anything, and the phone and email are shown only as images, so visitors on a phone can\'t tap to call you.'),
 ('ahli-pools','Ahli Pools','ahlipgl@gmail.com','Dubai',"One thing I noticed on your current site: the Projects page lists 25 projects, including pool works at City Walk and Al Barsha, but none of them shows a single photo, so visitors can't see what you've built."),
 ('raf-pools','RAF Pools','info@rafpools.com','Dubai','One thing I noticed on your current site: all four counters on the homepage (technicians, years of experience, satisfaction rate, pools transformed) currently display 0.'),
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
