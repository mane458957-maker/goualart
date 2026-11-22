# Génère la page prospect NewPool Express à partir du template /piscine/index.html
import re,os,json
s=open('/home/claude/goualart/piscine/index.html').read()
R=[]  # (ancien, nouveau)
U=""
# chemins partagés (la page est dans /piscine/labege-piscines/)
R+=[('"frames/f_"','"../frames/f_"'),('"frames-pc/f_"','"../frames-pc/f_"'),('src="villa/','src="../villa/'),('"formes/','"../formes/')]
# identité
L="https://www.piscine-newpoolexpress.com/_assets/"
R+=[("<title>AQUAVILLA — Constructeur de piscines</title>","<title>NewPool Express — Rénovation et construction de piscines à Montpellier</title>"),
    ('content="Constructeur de piscines sur-mesure : béton, coque, rénovation. Étude et devis gratuits."','content="NewPool Express, entreprise familiale à Montpellier depuis plus de 30 ans : rénovation PVC armé, construction de piscines et terrasses. Choisissez votre revêtement et voyez-le chez vous."'),
    ('name: "AquaVilla"','name: "NewPool Express"'),
    ('logoHtml: "AQUA<span>VILLA</span>"','logoHtml: "NewPool <span>Express</span>"'),
    ('city: "Côte d\'Azur"','city: "Montpellier"'),
    ('zone: "Alpes-Maritimes & Var"','zone: "Montpellier et l’Hérault"'),
    ('phone: "06 00 00 00 00"','phone: "06 86 71 97 69"'),
    ('email: "contact@aquavilla.fr"','email: ""'),
    ('address: "12 avenue des Pins, 06000 Nice"','address: "13 rue des Cades, 34680 Saint-Georges-d’Orques"'),
    ('Votre jardin a du potentiel.<br><em>On le transforme en piscine.</em>','Votre piscine comme neuve,<br><em>en quelques jours.</em>'),
    ('</span> · Devis gratuit</div>','</span> · Depuis plus de 30 ans · Diagnostic gratuit</div>'),
    ('<div class="eyebrow rv">Constructeur depuis <span data-c="since">2009</span></div>','<div class="eyebrow rv">Entreprise familiale · 2 générations</div>')]
R+=[('<h2 class="rv">Des piscines pensées pour durer, construites pour être vécues.</h2>','<h2 class="rv">Rénover, construire, sublimer.</h2>'),
    ('<p class="lead rv">Béton, coque ou rénovation : on conçoit, on construit et on entretient. Une seule équipe, du premier croquis à la mise en eau.</p>','<p class="lead rv">Béton, enduit, coque ou liner : on redonne vie à votre bassin avec la membrane PVC armé Renolit Alkorplan 2 mm. Particuliers, hôtels, campings et architectes nous font confiance.</p>'),
    ('<div><strong data-count="250">0</strong><span>piscines construites</span></div>','<div><strong>4,9/5</strong><span>sur 184 avis Google</span></div>'),
    ('<div><strong data-count="15">0</strong><span>ans d\'expérience</span></div>','<div><strong>200</strong><span>piscines rénovées par an</span></div>'),
    ('<div><strong>10 ans</strong><span>garantie décennale</span></div>','<div><strong>13 000 m²</strong><span>de PVC armé posés par an</span></div>'),
    ('<div><strong>48 h</strong><span>pour votre devis</span></div>','<div><strong>30 ans</strong><span>d’expérience, 2 générations</span></div>')]
R+=[('<h2 class="rv">Une piscine pour chaque terrain, chaque budget.</h2>','<h2 class="rv">Tout pour votre piscine, de la rénovation à la terrasse.</h2>'),
    ('<h3>Piscine béton sur-mesure</h3><p>Forme libre, débordement, miroir : liberté totale de dimensions et de finitions.</p><div class="price">À partir de 35 000 €</div>','<h3>Rénovation PVC armé</h3><p>Piscines béton, carrelées, enduites ou coques : membrane Renolit Alkorplan 2 mm, gammes Élégance et Authentic.</p><div class="price">Diagnostic en ligne offert</div>'),
    ('<h3>Piscine coque</h3><p>Installation rapide en 2 à 3 semaines, idéale pour les jardins de taille moyenne.</p><div class="price">À partir de 18 000 €</div>','<h3>Remplacement de liner</h3><p>Un liner neuf, posé rapidement par nos équipes.</p><div class="price">Sur devis</div>'),
    ('<h3>Rénovation</h3><p>Liner, carrelage, margelles, mise aux normes : votre bassin comme neuf.</p><div class="price">Sur devis</div>','<h3>Terrasses &amp; réaménagement</h3><p>Terrasses en pierre naturelle, ajout d’escalier, réaménagement du bassin.</p><div class="price">Sur devis</div>'),
    ('<h3>Entretien &amp; équipements</h3><p>Contrats annuels, volets, abris, pompes à chaleur, éclairage LED.</p><div class="price">Contrats dès 49 €/mois</div>','<h3>Construction</h3><p>Piscines neuves pour particuliers, hôtels et campings.</p><div class="price">Étude personnalisée</div>')]
R+=[('<h3>Visite gratuite</h3><p>On vient chez vous étudier le terrain, l\'accès et vos envies.</p>','<h3>Votre projet</h3><p>On étudie votre terrain et vos envies, en magasin ou chez vous.</p>'),
    ('<h3>Plan 3D &amp; devis</h3><p>Vous visualisez votre future piscine avant de signer.</p>','<h3>Diagnostic</h3><p>On étudie votre bassin et on choisit ensemble le revêtement.</p>'),
    ('<h3>Chantier</h3><p>4 à 8 semaines selon le projet, avec un suivi photo chaque semaine.</p>','<h3>Chantier</h3><p>Pose du PVC armé par nos 9 professionnels agréés.</p>'),
    ('<h3>Mise en eau</h3><p>Livraison, réglages et prise en main de vos équipements.</p>','<h3>Mise en eau</h3><p>Réglages, prise en main et conseils d\'entretien.</p>')]
R+=[('Intervention dans tout le secteur <span data-c="zone">Alpes-Maritimes &amp; Var</span>. Visite et étude offertes.','Basés à Saint-Georges-d’Orques, on intervient à <span data-c="zone">Montpellier et dans l’Hérault</span>.'),
    ('<div>📍 <span data-c="address">12 avenue des Pins, 06000 Nice</span></div>','<div>📍 <span data-c="address">13 rue des Cades, 34680 Saint-Georges-d’Orques</span></div>\n        <div>📞 Paul (administratif) : 06 23 00 51 58</div>'),
    ('· Constructeur de piscines</div><div>Garantie décennale · Mentions légales</div>','· Rénovation &amp; construction de piscines</div><div>34680 Saint-Georges-d’Orques</div>')]
for a,b in R:
    if a not in s: print("INTROUVABLE:",a[:70])
    s=s.replace(a,b)
s=re.sub(r"  creations: \[\n.*?\n  \],\n","  creations: [],\n",s,count=1,flags=re.S)
s=s.replace("  demoReviews: true,","  demoReviews: true,\n  score: { note:\"4,9\", label:\"184 avis Google\" },")
cr=[("Piscine rénovée","Saint-Gély-du-Fesc","piscine-saint-gely-du-fesc.SoAfyYSO_Z7vqoE.jpg"),("Terrasse en pierre naturelle","","terrasse-pierre-naturelle-2.Tfn70u4f_1xI8Lb.jpg"),("Piscine","Béziers","piscine-beziers.DEpeEtvd_Zlsl8G.jpg"),("Piscine rénovée","Sète","piscine-sete.OmO21TWd_1jJa2D.jpg"),("Terrasse piscine","Montpellier","terrasse-1.ULfyCwyc_oeVcp.jpg"),("Rénovation PVC armé","","piscine-2.LASGbh4S_Z9AJ59.jpg")]
cjs="  creations: [\n"+",\n".join(f'    {{ title:"{a}", place:"{b}", img:"{L}{c}" }}' for a,b,c in cr)+"\n  ],\n"
s=s.replace("  creations: [],\n",cjs,1)
s=s.replace(".bento .b0{grid-column:span 2}",".bento .b0{grid-column:span 2}\n@media(min-width:900px){.bento .b4,.bento .b5{grid-column:span 2}}\n@media(max-width:899px){.bento .b5{grid-column:span 2}}\n.bigLogo{font-size:clamp(44px,10vw,130px)!important;white-space:nowrap}",1)
# logo image
s=s.replace(".bigLogo span{color:var(--aqua2)}",".bigLogo span{color:var(--aqua2)}\n.bigLogo img{height:clamp(90px,22vw,190px);width:auto;display:block;background:#fff;padding:clamp(10px,2vw,18px) clamp(16px,3vw,28px);border-radius:20px;box-shadow:0 10px 40px rgba(0,0,0,.35)}\n.logo img{height:40px;width:auto;display:block;background:#fff;padding:4px 10px;border-radius:10px}")
os.makedirs('/home/claude/goualart/piscine/newpool-express',exist_ok=True)
open('/home/claude/goualart/piscine/newpool-express/index.html','w').write(s)
print("ok")
