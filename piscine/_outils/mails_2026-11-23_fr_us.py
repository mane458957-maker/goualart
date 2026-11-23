import sys, json; sys.path.insert(0, '/home/claude/goualart/piscine/_outils')
from mail_templates import signature_html, signature_text
OUT = '/tmp/claude-0/-home-claude-goualart/4a7e4217-fc5f-5d89-bdac-ebfcb9aadca3/scratchpad/mails.json'
RAW = 'https://raw.githubusercontent.com/mane458957-maker/goualart/main/'
M = [
 ('fr', '3af-piscines', '3AF Piscines', 'contact@3afpiscines.fr', 'Bonjour,',
  "Sur votre site actuel, le menu principal contient encore un lien « Sample Page » qui ouvre la page d'exemple de WordPress (« This is an example page ») : un détail, mais vos visiteurs le voient."),
 ('fr', 'audigier-piscines', 'Audigier Piscines', 'audigierpiscines@orange.fr', 'Bonjour Monsieur Audigier,',
  "Sur votre site actuel, les photos de la page « Piscines traditionnelles » portent encore le nom brut de l'appareil (« GEDC0009.JPG »…) et une petite faute s'est glissée sur l'accueil (« optenue ») : la nouvelle version met vos 50 ans de savoir-faire en valeur."),
 ('fr', 'hydropur-piscines', 'Hydropur Piscines', 'hydropur.piscines@wanadoo.fr', 'Bonjour,',
  "Sur votre site actuel, la page Réalisations ne présente que trois chantiers, sans photo, et l'un d'eux a encore une adresse en « lorem-ipsum » : la démo met vos coques (Manua, Tahiti, Caraïbes…) en avant à leurs vraies dimensions."),
 ('fr', 'aquastil-piscines', 'Aquastil Piscines', 'aquastil14@gmail.com', 'Bonjour,',
  "Sur votre site actuel, quelques fautes se sont glissées sur l'accueil (« Décrouvrez », « Tous nos piscines ») : des détails, mais qui comptent pour une entreprise primée aux Trophées de la Piscine 2023."),
 ('us', 'jack-olivers-pool-spa-patio', "Jack Oliver's Pools", 'jackoliverpools@jackoliverpools.com', 'Hi Jack,',
  "One thing I noticed on your current site: the footer still says ©2017, and the \"Hear From Our Clients\" link shows raw code instead of opening your reviews. With 231 reviews, that page deserves to work."),
 ('us', 'b-and-b-pools', 'B & B Pools', 'store@bandbpoolsinc.com', 'Hi there,',
  "One thing I noticed on your current site: the \"Get Your Free Quote\" section shows no form fields, so visitors can't actually request a quote online."),
 ('us', 'andes-pools', "Ande's Pools", 'andespools@hotmail.com', 'Hi there,',
  "One thing I noticed on your current site: some pages still use Wix's default addresses (like /copy-of-services) and the footer reads \"© 2024 Ande's Pools. Rights Reserved.\" Small things, but homeowners notice them."),
 ('us', '1st-choice-pools', '1st Choice Pools', 'firstchoicepools@live.com', 'Hi there,',
  "One thing I noticed on your current site: the estimate form on the contact page shows \"JavaScript is required for this content\" and some tracking links appear as plain text, so leads can slip away."),
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
