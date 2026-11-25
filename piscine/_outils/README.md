# Prospection Goual Studio — mode d'emploi (pour les tâches programmées)

## Templates
- `piscine/index.html` : template FRANÇAIS (source). `piscine/index-en.html` : template ANGLAIS (généré par make_en.py).
- Tout le contenu client est dans l'objet `CONFIG` + quelques textes HTML remplacés par chaînes exactes.
- Assets partagés : `piscine/frames/`, `piscine/frames-pc/`, `piscine/villa/`, `piscine/formes/`. Une démo vit dans `piscine/<slug>/index.html`
  et doit réécrire les chemins : `"frames/f_"`→`"../frames/f_"`, `"frames-pc/f_"`→`"../frames-pc/f_"`, `src="villa/`→`src="../villa/`, `"formes/`→`"../formes/`.

## Générer une démo
Partir d'un exemple : `exemple_compass.py` (anglais, logo texte), `exemple_eco.py` (français, logo image sur pastille blanche,
vrais modèles shape 6 aux dimensions L×W, 8 photos créations), `exemple_np.py` (français, logo texte, 6 photos).
Règles : vérifier chaque remplacement (afficher « INTROUVABLE » si absent) ; logo inconnu (couleur) → logo TEXTE ;
moins de 6 photos de réalisations → `creations: []` ; pas d'email → `email: ""` (le formulaire lance un appel) ;
garder `demoReviews: true` (avis d'exemple marqués) ; `score` seulement si la note Google est connue.

## Aperçu pour le mail
Capture Playwright (Chrome `/usr/bin/google-chrome`, flags `--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader --allow-file-access-from-files`) :
1280×800, haut de page + section `#config` (forcer `st.night=1;st.nightT=1;st.lights=1;st.lightsT=1;st.sht-=5`), empiler, redimensionner 900 px, JPEG q78 (< 200 Ko)
→ `piscine/<slug>/apercu.jpg`. Dans le mail : pièce jointe inline `contentId:"apercu"` via
`https://raw.githubusercontent.com/mane458957-maker/goualart/main/piscine/<slug>/apercu.jpg` (pousser avant d'envoyer),
logo signature `contentId:"logo"` via `.../main/img/goual-studio-logo.png`.

## Mail
Expéditeur : `Goual Studio <contact@goual.fr>` (Resend, domaine vérifié). Lien démo : `https://studio.goual.fr/piscine/<slug>/`.
Signature : voir `mail_templates.py` (en = Moyen-Orient +971 50 315 4697 ; fr = France +33 6 59 03 94 38 ; site affiché goual.fr).
Prix : Émirats AED 2,500 ; France 500 € TTC (retouches incluses, connexion du nom de domaine et du mail, options à discuter).
Structure : salutation → « j'ai pris la liberté de refaire votre site » + ce que fait la démo → aperçu cliquable → bouton démo
→ offre → (Dubaï : rendez-vous en personne possible) → signature. Un point concret de leur site actuel si utile, avec tact.


## Signature : JAMAIS de prénom
Ne jamais écrire « Mohammed » ni « Mohammed Goual » dans les mails ou messages (demande du 25/11/2026).
Fin de mail FR : « Bien cordialement,<br>L'équipe Goual Studio » ; EN : « Best regards,<br>The Goual Studio team ». Puis la signature de mail_templates.py.
