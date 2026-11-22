# Modèles de mail de prospection Goual Studio, par langue / pays
# Liens de démo : https://studio.goual.fr/piscine/<slug>/   Site dans la signature : goual.fr
SIG = {
 "en": {  # Moyen-Orient (Émirats, Qatar, Arabie saoudite)
  "tagline": "Websites &amp; AI video · Dubai", "phone": "+971 50 315 4697", "wa": "971503154697", "wa_label": "(WhatsApp)",
 },
 "fr": {  # France / Europe francophone
  "tagline": "Sites internet &amp; vidéo IA", "phone": "+33 6 59 03 94 38", "wa": "33659039438", "wa_label": "(WhatsApp)",
 },
 "es": {  # Espagne
  "tagline": "Páginas web y vídeo con IA", "phone": "+33 6 59 03 94 38", "wa": "33659039438", "wa_label": "(WhatsApp)",
 },
 "us": {  # États-Unis
  "tagline": "Websites &amp; AI video", "phone": "+33 6 59 03 94 38", "wa": "33659039438", "wa_label": "(WhatsApp)",
 },
}
def signature_html(lang):
    s = SIG[lang]
    return ('<table cellpadding="0" cellspacing="0" style="margin-top:6px;border-top:1px solid #e3e8ee;padding-top:12px"><tr>'
            '<td style="padding-right:14px;vertical-align:middle"><img src="cid:logo" alt="Goual Studio" width="110" style="width:110px;display:block"></td>'
            '<td style="vertical-align:middle;font-size:13px;color:#5b6875;line-height:1.6;border-left:2px solid #2bb3c0;padding-left:14px">'
            f'<b style="color:#0b1620;font-size:14px">Goual Studio</b><br>{s["tagline"]}<br>'
            f'<a href="https://wa.me/{s["wa"]}" style="color:#2bb3c0;text-decoration:none">{s["phone"]}</a> {s["wa_label"]}<br>'
            '<a href="mailto:contact@goual.fr" style="color:#5b6875;text-decoration:none">contact@goual.fr</a> · '
            '<a href="https://goual.fr" style="color:#5b6875;text-decoration:none">goual.fr</a></td></tr></table>')
def signature_text(lang):
    s = SIG[lang]
    return f"Goual Studio\n{s['tagline'].replace('&amp;','&')}\n{s['phone']} {s['wa_label']}\ncontact@goual.fr · goual.fr"
