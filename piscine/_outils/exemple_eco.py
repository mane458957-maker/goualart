# Génère la page prospect Ecopiscine à partir du template /piscine/index.html
import re,os,json
s=open('/home/claude/goualart/piscine/index.html').read()
R=[]  # (ancien, nouveau)
U=""
# chemins partagés (la page est dans /piscine/labege-piscines/)
R+=[('"frames/f_"','"../frames/f_"'),('"frames-pc/f_"','"../frames-pc/f_"'),('src="villa/','src="../villa/'),('"formes/','"../formes/')]
# identité
L="https://ecopiscine.eu/wp-content/uploads/"
R+=[("<title>AQUAVILLA — Constructeur de piscines</title>","<title>Ecopiscine — Piscines coques à Saint-Priest (Lyon)</title>"),
    ('content="Constructeur de piscines sur-mesure : béton, coque, rénovation. Étude et devis gratuits."','content="Ecopiscine à Saint-Priest, près de Lyon : plus de 100 piscines coques polyester, installées par ECOTP sans sous-traitance. Choisissez votre modèle et voyez-le chez vous."'),
    ('name: "AquaVilla"','name: "Ecopiscine"'),
    ('logoHtml: "AQUA<span>VILLA</span>"',f'logoHtml: \'<img src="{L}2018/12/Logo-3.png" alt="Ecopiscine">\''),
    ('city: "Côte d\'Azur"','city: "Lyon"'),
    ('zone: "Alpes-Maritimes & Var"','zone: "Lyon, le Rhône et l’Ain"'),
    ('phone: "06 00 00 00 00"','phone: "04 37 25 93 58"'),
    ('email: "contact@aquavilla.fr"','email: "ecopiscine@orange.fr"'),
    ('address: "12 avenue des Pins, 06000 Nice"','address: "228 route de Grenoble (RN6), 69800 Saint-Priest"'),
    ('Votre jardin a du potentiel.<br><em>On le transforme en piscine.</em>','Vous achetez votre piscine chez nous,<br><em>on l’installe.</em>'),
    ('</span> · Devis gratuit</div>','</span> · Sans sous-traitance · Devis gratuit</div>'),
    ('<div class="eyebrow rv">Constructeur depuis <span data-c="since">2009</span></div>','<div class="eyebrow rv">Depuis 2007</div>')]
R+=[('<h2 class="rv">Des piscines pensées pour durer, construites pour être vécues.</h2>','<h2 class="rv">Une piscine coque, du showroom à la mise en eau.</h2>'),
    ('<p class="lead rv">Béton, coque ou rénovation : on conçoit, on construit et on entretient. Une seule équipe, du premier croquis à la mise en eau.</p>','<p class="lead rv">Plus de 100 coques polyester fabriquées en France à découvrir au showroom de Saint-Priest. Notre entreprise de travaux ECOTP s’occupe de tout : terrassement, réseaux et pose.</p>'),
    ('<div><strong data-count="250">0</strong><span>piscines construites</span></div>','<div><strong>5/5</strong><span>sur 198 avis Google</span></div>'),
    ('<div><strong data-count="15">0</strong><span>ans d\'expérience</span></div>','<div><strong>80+</strong><span>piscines installées par an</span></div>'),
    ('<div><strong>10 ans</strong><span>garantie décennale</span></div>','<div><strong>100+</strong><span>modèles de coques</span></div>'),
    ('<div><strong>48 h</strong><span>pour votre devis</span></div>','<div><strong>10 ans</strong><span>garantie produit et pose</span></div>')]
R+=[('<h2 class="rv">Une piscine pour chaque terrain, chaque budget.</h2>','<h2 class="rv">Un seul interlocuteur, de A à Z.</h2>'),
    ('<h3>Piscine béton sur-mesure</h3><p>Forme libre, débordement, miroir : liberté totale de dimensions et de finitions.</p><div class="price">À partir de 35 000 €</div>','<h3>Piscines coques</h3><p>Plus de 100 modèles polyester, fabriqués en France, à voir au showroom.</p><div class="price">Étude et devis offerts</div>'),
    ('<h3>Piscine coque</h3><p>Installation rapide en 2 à 3 semaines, idéale pour les jardins de taille moyenne.</p><div class="price">À partir de 18 000 €</div>','<h3>Installation par ECOTP</h3><p>Notre entreprise de travaux pose votre piscine, sans sous-traitance.</p><div class="price">Garantie décennale</div>'),
    ('<h3>Rénovation</h3><p>Liner, carrelage, margelles, mise aux normes : votre bassin comme neuf.</p><div class="price">Sur devis</div>','<h3>Terrassement &amp; aménagement</h3><p>Terrassement, réseaux divers et aménagement autour du bassin.</p><div class="price">Sur devis</div>'),
    ('<h3>Entretien &amp; équipements</h3><p>Contrats annuels, volets, abris, pompes à chaleur, éclairage LED.</p><div class="price">Contrats dès 49 €/mois</div>','<h3>Accessoires &amp; traitement</h3><p>Équipements, accessoires et produits de traitement au magasin.</p><div class="price">Conseils en boutique</div>')]
R+=[('<h3>Visite gratuite</h3><p>On vient chez vous étudier le terrain, l\'accès et vos envies.</p>','<h3>Votre projet</h3><p>On étudie votre terrain et vos envies, en magasin ou chez vous.</p>'),
    ('<h3>Plan 3D &amp; devis</h3><p>Vous visualisez votre future piscine avant de signer.</p>','<h3>Choix au showroom</h3><p>Forme, taille, équipements : on choisit ensemble à Saint-Priest.</p>'),
    ('<h3>Chantier</h3><p>4 à 8 semaines selon le projet, avec un suivi photo chaque semaine.</p>','<h3>Pose par ECOTP</h3><p>Terrassement, réseaux et pose par nos propres équipes.</p>'),
    ('<h3>Mise en eau</h3><p>Livraison, réglages et prise en main de vos équipements.</p>','<h3>Mise en eau</h3><p>Réglages, prise en main et conseils d\'entretien.</p>')]
R+=[('Intervention dans tout le secteur <span data-c="zone">Alpes-Maritimes &amp; Var</span>. Visite et étude offertes.','Showroom à Saint-Priest (RN6), intervention à <span data-c="zone">Lyon, dans le Rhône et l’Ain</span>.'),
    ('<div>📍 <span data-c="address">12 avenue des Pins, 06000 Nice</span></div>','<div>📍 <span data-c="address">228 route de Grenoble (RN6), 69800 Saint-Priest</span></div>\n        <div>🕘 Mar–Sam 10h–12h / 14h–18h</div>'),
    ('· Constructeur de piscines</div><div>Garantie décennale · Mentions légales</div>','· Piscines coques</div><div>69800 Saint-Priest</div>')]
for a,b in R:
    if a not in s: print("INTROUVABLE:",a[:70])
    s=s.replace(a,b)
s=re.sub(r"  creations: \[\n.*?\n  \],\n","  creations: [],\n",s,count=1,flags=re.S)
s=s.replace("  demoReviews: true,","  demoReviews: true,\n  score: { note:\"5,0\", label:\"198 avis Google\" },")
P=L+"2025/10/"
cr=[("Plaisance 700","7 × 4 m","PLAISANCE-PPPEST-6-scaled-e1760101835712.jpg"),("Plaisance 700 Plage","9,5 × 4 m","PLAISANCE-PLAGE-scaled-e1760101796871.jpg"),("Brazilia","10 × 4,2 m","Plaisance-Plage-3-scaled-e1760102023638.jpg"),("Plaisance 1000 Media Plage","11,5 × 4,2 m","Plaisance-Media-Plage-PPPEST-4-e1760101981326.jpg"),("Plaisance 700","7 × 4 m","PLAISANCE-PPPEST-3-scaled-e1760101821145.jpg"),("Plaisance 700 Plage","9,5 × 4 m","PLAISANCE-PLAGE-PPPEST-3-scaled-e1760102060292.jpg"),("Brazilia","10 × 4,2 m","Plaisance-Plage-1-scaled-e1760101993804.jpg"),("Plaisance 1000 Media Plage","11,5 × 4,2 m","Plaisance-Media-Plage-PPPEST-2-e1760101970570.jpg")]
cjs="  creations: [\n"+",\n".join(f'    {{ title:"{a}", place:"{b}", img:"{P}{c}" }}' for a,b,c in cr)+"\n  ],\n"
s=s.replace("  creations: [],\n",cjs,1)
mods=[("Plaisance 1000 Media Plage","11,50 × 4,20 m",11.5,4.2),("Brazilia","10,00 × 4,20 m",10,4.2),("Plaisance 700 Plage","9,50 × 4,00 m",9.5,4),("Plaisance 700","7,00 × 4,00 m",7,4)]
js="  models: [\n"+",\n".join(f'    {{ name:"{n}", dims:"{d}", shape:6, L:{l}, W:{w} }}' for n,d,l,w in mods)+"\n  ],\n"
s=re.sub(r"  models: \[\n.*?\n  \],\n",js,s,count=1,flags=re.S)
# logo image
s=s.replace(".bigLogo span{color:var(--aqua2)}",".bigLogo span{color:var(--aqua2)}\n.bigLogo img{height:clamp(90px,22vw,190px);width:auto;display:block;background:#fff;padding:clamp(10px,2vw,18px) clamp(16px,3vw,28px);border-radius:20px;box-shadow:0 10px 40px rgba(0,0,0,.35)}\n.logo img{height:40px;width:auto;display:block;background:#fff;padding:4px 10px;border-radius:10px}")
os.makedirs('/home/claude/goualart/piscine/ecopiscine',exist_ok=True)
open('/home/claude/goualart/piscine/ecopiscine/index.html','w').write(s)
print("ok")
