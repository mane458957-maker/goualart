import sys, json; sys.path.insert(0, '/home/claude/goualart/piscine/_outils')
from mail_templates import signature_html, signature_text
OUT = '/tmp/claude-0/-home-claude-goualart/2e9643b7-312f-5437-bbbd-2aa728de3325/scratchpad/mails.json'
RAW = 'https://raw.githubusercontent.com/mane458957-maker/goualart/main/'
M = [
 ('fr', 'tradi-piscines', 'Tradi Piscines', 'kitpiscine@aol.com', 'Bonjour,',
  "Sur votre site actuel, la description qui s'affiche dans Google et sur les réseaux indique « Orélans (45) » au lieu d'Orléans, et le pied de page affiche « KIT PISCINES ART DECO LOISIRS » plutôt que Tradi Piscines : la démo remet votre nom et vos réalisations au premier plan."),
 ('fr', 'lorraine-piscines', 'Lorraine Piscines', 'lorraine.piscines@hotmail.fr', 'Bonjour,',
  "Sur votre site actuel, le bouton Facebook renvoie vers l'accueil de Facebook plutôt que vers votre page, et la section « Nos produits » est restée vide : avec plus de 100 avis Google, votre vitrine mérite d'être à la hauteur."),
 ('fr', 'normandie-piscines', 'Normandie Piscines', 'caen@normandie-piscines.com', 'Bonjour,',
  "Sur votre site actuel, la section « Ce qu'ils disent de nous » est vide, alors que près d'une centaine de clients vous ont laissé un avis Google : la démo met vos réalisations et leurs retours en avant."),
 ('fr', 'aqua-and-co', 'Aqua And Co', 'contact@aqua-and-co.fr', 'Bonjour,',
  "Sur votre site actuel, la page Contacts n'affiche pas votre adresse email (« activez JavaScript ») et montre un bloc de connexion en anglais (« Login with Google + ») à vos visiteurs : la démo leur permet de vous joindre en un clic."),
 ('fr', 'piscine-de-latlantique', "Piscine de l'Atlantique", 'piscine@piscinedelatlantique.com', 'Bonjour,',
  "Sur votre site actuel, le bandeau cookies affiche des balises non remplies (« {title} », « {vendor_count} ») et les cartes « Nos piscines » ne mènent nulle part : la démo présente vos modèles de façon interactive."),
 ('us', 'griffin-pools', 'Griffin Pools', 'michelle@griffinpools.com', 'Hi Michelle,',
  "One thing I noticed on your current site: the \"What We Do\" menu item doesn't lead anywhere, and the About page still says \"over 45 years\" for a company building pools since 1975. Fifty-one years deserves to be front and center."),
 ('us', 'san-diego-pools', 'San Diego Pools', 'info@sandiegopools.com', 'Hi there,',
  "One thing I noticed on your current site: the \"Portfolio\" menu item doesn't lead anywhere, subpages still show \"© 2022\", and the homepage and footer list two different addresses (Santee and La Jolla)."),
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
        end = "Je reste disponible pour en parler par téléphone ou WhatsApp.<br><br>Bien cordialement,<br>L'équipe Goual Studio"
        end_t = "Je reste disponible pour en parler par téléphone ou WhatsApp.\n\nBien cordialement,\nL'équipe Goual Studio"
        sig, sigt = signature_html('fr'), signature_text('fr')
    else:
        subj = f'{co}: your new website is ready'
        p1 = f"I took the liberty of redesigning your website, to show what {co} could offer its clients:"
        feats = ["homeowners pick their pool model and tile finish", "they switch from day to night and turn on the pool lights", "they see the result right away in a real backyard setting"]
        btn = f'Open the {co} demo'
        offer = "<b>Current offer: $500, all included</b> (domain connection, professional email, small adjustments)."
        offer_t = "Current offer: $500, all included (domain connection, professional email, small adjustments)."
        end = "Happy to walk you through it on a quick call.<br><br>Best regards,<br>The Goual Studio team"
        end_t = "Happy to walk you through it on a quick call.\n\nBest regards,\nThe Goual Studio team"
        sig, sigt = signature_html('us'), signature_text('us')
    li = ''.join(f'<li>{f}</li>' for f in feats)
    html = (f'<div style="{B};max-width:620px">'
            f'<p>{hi}</p><p>{p1}</p><ul style="padding-left:20px;margin:0 0 14px">{li}</ul>'
            f'<p style="margin:18px 0"><a href="{url}"><img src="cid:apercu" alt="{btn}" width="560" style="width:100%;max-width:560px;border-radius:12px;border:1px solid #e3e8ee;display:block"></a></p>'
            f'<p style="margin:18px 0"><a href="{url}" style="background:#2bb3c0;color:#fff;text-decoration:none;padding:12px 22px;border-radius:999px;font-weight:bold;display:inline-block">{btn}</a></p>'
            f'<p>{weak}</p><p>{offer}</p><p>{end}</p>{sig}</div>')
    text = f"{hi}\n\n{p1}\n" + ''.join(f"- {f}\n" for f in feats) + f"\n{btn}{' :' if lang == 'fr' else ':'} {url}\n\n{weak}\n\n{offer_t}\n\n{end_t}\n\n{sigt}\n"
    out.append(dict(slug=slug, to=to, subject=subj, html=html, text=text,
                    attachments=[{"filename": "apercu.jpg", "url": RAW + f"piscine/{slug}/apercu.jpg", "contentId": "apercu"},
                                 {"filename": "goual-studio-logo.png", "url": RAW + "img/goual-studio-logo.png", "contentId": "logo"}]))
json.dump(out, open(OUT, 'w'), ensure_ascii=False, indent=0)
print(len(out))
