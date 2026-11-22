import sys, json; sys.path.insert(0, '/home/claude/goualart/piscine/_outils')
from mail_templates import signature_html, signature_text
OUT = '/tmp/claude-0/-home-claude-goualart/a6719a15-e75d-55f7-a415-05b1109a44c6/scratchpad/mails.json'
RAW = 'https://raw.githubusercontent.com/mane458957-maker/goualart/main/'
M = [
 ('fr', 'technisud-piscine', 'Technisud Piscine', 'technisudpiscine@free.fr', 'Bonjour Monsieur Jacquet,',
  "Petite remarque sur votre site actuel : le bas de page affiche encore « © 2017 » et certains boutons apparaissent en double (« DEVIS GRATUIT DEVIS GRATUIT »). Des détails, mais vos clients les voient."),
 ('fr', 'sud-est-piscines', 'Sud Est Piscines', 'sudestpiscines@gmail.com', 'Bonjour Monsieur Chave,',
  "Sur votre site actuel, le bas de page indique « © 2021 » et l'on lit « depuis 2010 » à côté de « plus de 30 ans d'expérience » : la nouvelle version met en avant vos vrais chiffres (500 piscines, 2 000 clients)."),
 ('fr', 'gm-piscine', 'GM Piscine', 'contact@gmpiscine.fr', 'Bonjour Monsieur Siaud,',
  "Sur votre site actuel, la rubrique « Qui sommes-nous ? » est vide : la nouvelle version présente votre activité dès la première page, avec vos modèles Aboral (Maatea, Caraïbes, Maeva…) à leurs vraies dimensions."),
 ('fr', 'piscines-gatel', 'Piscines Gatel', 'contact@piscine-gatel.com', 'Bonjour,',
  "Sur votre site actuel, la galerie de réalisations date de 2016 et deux chiffres se contredisent (1 500 piscines construites d'un côté, 700 clients de l'autre) : la nouvelle version remet tout cela au propre."),
 ('fr', 'rhonalp-piscines', 'Rhonalp Piscines', 'rhonalp@rhonalp-piscines.fr', 'Bonjour,',
  "Sur votre site actuel, la page Réalisations n'affiche aucune photo (les fiches indiquent « Piscine Piscine Piscine ») : la démo, elle, met vos rénovations du Grésivaudan en grand."),
 ('fr', 'bleu-30-piscines', 'Bleu 30 Piscines', 'bleu30piscines@gmail.com', 'Bonjour Monsieur Cicirello,',
  "Sur votre site actuel, quelques fautes se sont glissées dans le menu (« CONTRUCTION PISCINE », « REOVATION PISCINE ») et l'adresse email affichée n'est pas celle du lien : des détails qui comptent pour un client qui compare."),
 ('us', 'paradise-pools-tampa-bay', 'Paradise Pools of Tampa Bay', 'paradisepoolstb@yahoo.com', 'Hi there,',
  "One thing I noticed on your current site: the contact page still uses Wix's default address (/contact-8), the \"More\" menu item leads nowhere and there is no street address or social link. With 177 five-star reviews, your website should look as good as your work."),
 ('us', 'atlas-pools-central-florida', 'Atlas Pools of Central Florida', 'help@atlaspoolsofcentralfl.net', 'Hi there,',
  "One thing I noticed on your current site: some raw Google Tag Manager code shows as text at the top of the page, and the years of experience don't match from one page to another (1978, 30, 40 and 43 years)."),
 ('us', 'vineyard-pools', 'Vineyard Pools', 'info@vineyardpools.com', 'Hi there,',
  "One thing I noticed on your current site: the footer still says © 2023 and one blog post still sits at WordPress's default /hello-world/ address. Small things, but homeowners notice them."),
 ('us', 'impeccable-pools', 'Impeccable Pools', 'justin@impeccablepools.com', 'Hi Justin,',
  "One thing I noticed on your current site: the \"GET STARTED\" button, the logo and the main slider link to your developer's test copy (fresnopools.wpengine.com) instead of impeccablepools.com, so visitors can land on the wrong site."),
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
