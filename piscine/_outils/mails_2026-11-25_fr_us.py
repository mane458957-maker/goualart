import sys, json; sys.path.insert(0, '/home/claude/goualart/piscine/_outils')
from mail_templates import signature_html, signature_text
OUT = '/tmp/claude-0/-home-claude-goualart/e7fa4c2e-d263-5760-8d07-b33d88e953b6/scratchpad/mails.json'
RAW = 'https://raw.githubusercontent.com/mane458957-maker/goualart/main/'
M = [
 ('fr', 'piscine-thomas', 'Piscine Thomas', 'piscinethomas@orange.fr', 'Bonjour,',
  "Sur votre site actuel, certains diaporamas affichent encore les textes du modèle (« Titre de la diapositive », « Écrivez votre légende ici ») et le menu « Nos réalisations » ne mène nulle part : la démo met vos piscines et votre parcours au premier plan."),
 ('fr', 'piscine-et-bien-etre', 'Piscine et Bien-Être', 'contact@piscineetbien-etre.com', 'Bonjour,',
  "Sur votre site actuel, le bandeau cookies affiche « {title} » et « {vendor_count} », et une partie des photos de votre galerie est au format .heic, que la plupart des navigateurs n'affichent pas : vos réalisations méritent d'être vues."),
 ('fr', 'castel-piscines', 'Castel Piscines', 'contact@castel-piscines.fr', 'Bonjour,',
  "Sur votre site actuel, le pied de page est resté sur « ©2021 » et l'accueil annonce « 29 ans » d'activité, alors que vous construisez des piscines depuis 1990 : plus de 35 ans de métier qui méritent d'être mis en avant."),
 ('fr', 'inter-piscine', 'Inter Piscine', 'interpiscine@gmail.com', 'Bonjour,',
  "Sur votre site actuel, quelques fautes sont visibles (« Vaulcuse », « une large choix ») et la rubrique « Présentation » est vide : vos réalisations dans le Luberon méritent une vitrine à leur hauteur."),
 ('us', 'purple-heart-pools', 'Purple Heart Pools', 'purpleheartpools@gmail.com', 'Hi Chad,',
  "One thing I noticed on your current site: the footer \"Home\" link points to a staging domain (michaels793.sg-host.com), \"Core Values\" opens the template's demo site, and the Gallery page shows 9 empty tiles."),
 ('us', 'pool-time-pool-spa', 'Pool Time Pool &amp; Spa', 'pooltime@pooltimepoolspa.com', 'Hi Joe,',
  "One thing I noticed on your current site: the footer shows pooltime@pooltimepool.com while the email link goes to pooltime@pooltimepoolspa.com, and there's no gallery page to show off your builds. With 196 reviews, your site should match your reputation."),
 ('us', 'seahorse-pools-spas', 'Seahorse Pools &amp; Spas', 'scasale@seahorsepools.com', 'Hi there,',
  "One thing I noticed on your current site: the footer still says \"© Copyright 2022\", a gallery category reads \"Forth Worth Store\", and a stray \"Select Page\" label shows on every page."),
 ('us', 'klapprodt-pools', 'Klapprodt Pools', 'sales@klapprodtpools.com', 'Hi there,',
  "One thing I noticed on your current site: the browser tab still reads \"Home | Klapprodt Pools\", gallery photos are labeled \"Image Item\", and the header and the page list two different showroom hours."),
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
    text = f"{hi}\n\n{p1}\n" + ''.join(f"- {f}\n" for f in feats) + f"\n{btn} : {url}\n\n{weak}\n\n{offer_t}\n\n{end_t}\n\n{sigt}\n"
    out.append(dict(slug=slug, to=to, subject=subj, html=html, text=text,
                    attachments=[{"filename": "apercu.jpg", "url": RAW + f"piscine/{slug}/apercu.jpg", "contentId": "apercu"},
                                 {"filename": "goual-studio-logo.png", "url": RAW + "img/goual-studio-logo.png", "contentId": "logo"}]))
json.dump(out, open(OUT, 'w'), ensure_ascii=False, indent=0)
print(len(out))
