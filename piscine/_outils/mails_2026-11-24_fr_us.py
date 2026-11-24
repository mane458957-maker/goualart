import sys, json; sys.path.insert(0, '/home/claude/goualart/piscine/_outils')
from mail_templates import signature_html, signature_text
OUT = '/tmp/claude-0/-home-claude-goualart/33fb3296-e6b3-5239-a9e4-f16b79d9931e/scratchpad/mails.json'
RAW = 'https://raw.githubusercontent.com/mane458957-maker/goualart/main/'
M = [
 ('fr', 'mth-piscines', 'M.T.H Piscines', 'mth-piscines@wanadoo.fr', 'Bonjour,',
  "Sur votre site actuel, une phrase de l'accueil est restée incomplète (« Depuis plus années ») et le site ne montre encore aucune photo de vos piscines : la démo met en avant votre savoir-faire familial dans le centre Var."),
 ('us', 'yandles-splash-time-pools', "Yandle's Splash Time Pools", 'info@yandlessplashtimepools.net', 'Hi there,',
  "One thing I noticed on your current site: some raw code text (\"meta-viewport…\") and a leftover \"Close Panel\" label show in the page, and the contact form has no message box or submit button, so leads can't actually reach you through it."),
 ('us', 'blue-marlin-pools', 'Blue Marlin Pools', 'cfoster@bluemarlinpools.com', 'Hi Chris,',
  "One thing I noticed on your current site: a few typos on the homepage (\"the samke amount\", \"efficent\"), some equipment descriptions are duplicated, and there's no phone number on the homepage. Your pools deserve a gallery front and center."),
 ('us', 'aaa-pools', 'AAA Pools', 'bonnie1974aaa@gmail.com', 'Hi Bonnie,',
  "One thing I noticed on your current site: the homepage mentions \"spillover saps\", the Maintenance menu link goes nowhere and the YouTube icon opens Facebook. Small things, but homeowners notice them."),
 ('us', 'trademark-pool-spa', 'TradeMark Pool &amp; Spa', 'Pool4U@sbcglobal.net', 'Hi Mark,',
  "One thing I noticed on your current site: several photos in your gallery are labeled \"Printer Cartridges\", \"Cable Ties\" or \"Staplers\" (leftovers from a website template), and the \"Service Areas\" link goes nowhere."),
 ('us', 'monster-pool-company', 'Monster Pool Company', 'MonsterPoolCo@gmail.com', 'Hi there,',
  "One thing I noticed on your current site: the \"Pavers\" gallery button opens the Plants &amp; Landscape gallery and \"Outdoor Kitchens\" opens the BBQ one. After 24 years, your builds deserve a site made for a pool builder, not a store template."),
 ('us', 'e-and-e-pool-construction', 'E and E Pools', 'eandepools0@gmail.com', 'Hi there,',
  "One thing I noticed on your current site: the footer still shows \"2024 &amp;copy\", the address reads \"Suit 100\", and the Services, Gallery, Yelp and LinkedIn links point nowhere. With 130 reviews, your site should match your reputation."),
]
B = 'font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:1.6;color:#0b1620'
out = []
for lang, slug, co, to, hi, weak in M:
    url = f'https://studio.goual.fr/piscine/{slug}/'
    if lang == 'fr':
        subj = f'{co} : une vitrine premium pour vos piscines'
        p1 = f"Je me suis permis de refaire votre site, pour vous montrer ce que {co} pourrait présenter à ses clients :"
        feats = ["le client choisit son carrelage et son modèle de piscine", "il passe du jour à la nuit et allume les projecteurs", "il voit le résultat directement dans une villa"]
        btn = f'Voir la démo {co}'
        offer = "<b>Offre du moment : 500 € TTC</b>, retouches selon vos préférences incluses, connexion de votre nom de domaine et de votre mail ; options à discuter."
        offer_t = "Offre du moment : 500 € TTC, retouches selon vos préférences incluses, connexion de votre nom de domaine et de votre mail ; options à discuter."
        end = "Je reste disponible pour en parler par téléphone ou WhatsApp.<br><br>Bien cordialement,<br>Mohammed Goual"
        end_t = "Je reste disponible pour en parler par téléphone ou WhatsApp.\n\nBien cordialement,\nMohammed Goual"
        sig, sigt = signature_html('fr'), signature_text('fr')
    else:
        subj = f'{co}: your new website is ready'
        p1 = f"I took the liberty of redesigning your website, to show what {co} could offer its clients:"
        feats = ["homeowners pick their pool model and tile finish", "they switch from day to night and turn on the pool lights", "they see the result right away in a real backyard setting"]
        btn = f'Open the {co} demo'
        offer = "<b>Current offer: $500, all included</b> (domain connection, professional email, small adjustments)."
        offer_t = "Current offer: $500, all included (domain connection, professional email, small adjustments)."
        end = "Happy to walk you through it on a quick call.<br><br>Best regards,<br>Mohammed Goual"
        end_t = "Happy to walk you through it on a quick call.\n\nBest regards,\nMohammed Goual"
        sig, sigt = signature_html('us'), signature_text('us')
    li = ''.join(f'<li>{f}</li>' for f in feats)
    html = (f'<div style="{B};max-width:620px">'
            f'<p>{hi}</p><p>{p1}</p><ul style="padding-left:20px;margin:0 0 14px">{li}</ul>'
            f'<p style="margin:18px 0"><a href="{url}"><img src="cid:apercu" alt="{btn}" width="560" style="width:100%;max-width:560px;border-radius:12px;border:1px solid #e3e8ee;display:block"></a></p>'
            f'<p style="margin:18px 0"><a href="{url}" style="background:#2bb3c0;color:#fff;text-decoration:none;padding:12px 22px;border-radius:999px;font-weight:bold;display:inline-block">{btn}</a></p>'
            f'<p>{weak}</p><p>{offer}</p><p>{end}</p>{sig}</div>')
    text = f"{hi}\n\n{p1}\n" + ''.join(f"- {f}\n" for f in feats) + f"\n{btn} : {url}\n\n{weak}\n\n{offer_t}\n\n{end_t}\n\n{sigt}\n"
    out.append(dict(slug=slug, to=to, subject=subj, html=html, text=text,
                    attachments=[{"filename": "apercu.jpg", "url": RAW + f"piscine/{slug}/apercu.jpg", "contentId": "apercu"},
                                 {"filename": "goual-studio-logo.png", "url": RAW + "img/goual-studio-logo.png", "contentId": "logo"}]))
json.dump(out, open(OUT, 'w'), ensure_ascii=False, indent=0)
print(len(out))
