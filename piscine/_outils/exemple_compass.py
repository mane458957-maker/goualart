# Page démo Compass (Dubai) — à partir du template anglais /piscine/index-en.html
import re,os
s=open('/home/claude/goualart/piscine/index-en.html').read()
R=[('"frames/f_"','"../frames/f_"'),('"frames-pc/f_"','"../frames-pc/f_"'),('src="villa/','src="../villa/'),('"formes/','"../formes/')]
R+=[('<title>AQUAVILLA — Swimming Pool Builder</title>','<title>Compass — The Swimming Pool Company, Dubai since 1989</title>'),
    ('content="Custom swimming pool builder: concrete, fibreglass, renovation. Free design and quote."','content="Compass, the swimming pool company in Dubai since 1989: turnkey pools, spas and water features, maintenance, equipment and chemicals. Choose your tiles and see your pool in your villa."'),
    ('name: "AquaVilla"','name: "Compass"'),
    ('logoHtml: "AQUA<span>VILLA</span>"','logoHtml: "COM<span>PASS</span>"'),
    ('city: "Côte d\'Azur"','city: "Dubai"'),
    ('zone: "Alpes-Maritimes & Var"','zone: "Dubai & the UAE"'),
    ('phone: "06 00 00 00 00"','phone: "+971 4 339 0411"'),
    ('whatsapp: "",','whatsapp: "97143390411",'),
    ('email: "contact@aquavilla.fr"','email: "info@compass-me.com"'),
    ('address: "12 avenue des Pins, 06000 Nice"','address: "18 Street, Al Quoz Industrial Area 1, Dubai"'),
    ('Your garden has potential.<br><em>We turn it into a pool.</em>','The swimming pool company.<br><em>Dubai, since 1989.</em>'),
    ('</span> · Free quote</div>','</span> · 33+ years · Free consultation</div>'),
    ('Pool builder since <span data-c="since">2009</span>','Pool builder since <span data-c="since">1989</span>'),
    ('<h2 class="rv">Pools designed to last, built to be lived in.</h2>','<h2 class="rv">Your pool, from the first sketch to every swim after.</h2>'),
    ('Concrete, fibreglass or renovation: we design, build and maintain. One team, from the first sketch to the first swim.','Turnkey pools, spas, saunas and water features, then maintenance, equipment and chemicals from our own store: one company for the whole life of your pool.'),
    ('<div><strong data-count="250">0</strong><span>pools built</span></div>','<div><strong>1989</strong><span>founded in Dubai</span></div>'),
    ('<div><strong data-count="15">0</strong><span>years of experience</span></div>','<div><strong>33+</strong><span>years of experience</span></div>'),
    ('<strong>10 years</strong><span>structural warranty</span>','<strong>10 years</strong><span>warranty on the pool shell</span>'),
    ('<strong>48 h</strong><span>for your quote</span>','<strong>24/7</strong><span>pool support</span>'),
    ('<h2 class="rv">A pool for every plot and every budget.</h2>','<h2 class="rv">Build, maintain, equip.</h2>'),
    ('<h3>Custom concrete pools</h3><p>Freeform, infinity, mirror: total freedom of size and finish.</p><div class="price">From AED 120,000</div>','<h3>Turnkey construction</h3><p>Pools, spas, saunas and water features, designed and built for your villa.</p><div class="price">Free consultation</div>'),
    ('<h3>Fibreglass pools</h3><p>Fast installation in 2 to 3 weeks, ideal for medium-sized gardens.</p><div class="price">From AED 70,000</div>','<h3>Maintenance</h3><p>Servicing and 24/7 support, with water kept to Dubai Municipality standards.</p><div class="price">Annual contracts</div>'),
    ('<h3>Renovation</h3><p>Tiles, coping, equipment, compliance: your pool like new.</p><div class="price">On quotation</div>','<h3>Equipment &amp; chemicals</h3><p>Pumps, filters, lighting, spare parts and chemicals in our pool store.</p><div class="price">Compass Pool Store</div>'),
    ('<h3>Maintenance &amp; equipment</h3><p>Annual contracts, covers, chillers, heat pumps, LED lighting.</p><div class="price">Contracts from AED 350/month</div>','<h3>Salt chlorination</h3><p>AquaClear salt systems for softer, easier water.</p><div class="price">On quotation</div>'),
    ('We work across <span data-c="zone">Alpes-Maritimes &amp; Var</span>. Free site visit and design.','Based in Al Quoz, we work across <span data-c="zone">Dubai and the UAE</span>. Free consultation.'),
    ('<div>📍 <span data-c="address">12 avenue des Pins, 06000 Nice</span></div>','<div>📍 <span data-c="address">18 Street, Al Quoz Industrial Area 1, Dubai</span></div>\n        <div>📱 +971 56 604 3511</div>'),
    ('· Swimming pool builder</div><div>Structural warranty · Legal notice</div>','· The Swimming Pool Company</div><div>Al Quoz, Dubai</div>')]
for a,b in R:
    if a not in s: print("INTROUVABLE:",a[:70])
    s=s.replace(a,b)
s=re.sub(r"  creations: \[\n.*?\n  \],\n","  creations: [],\n",s,count=1,flags=re.S)
s=s.replace(".bigLogo span{color:var(--aqua2)}",".bigLogo span{color:var(--aqua2)}\n.bigLogo{letter-spacing:6px}")
os.makedirs('/home/claude/goualart/piscine/compass',exist_ok=True)
open('/home/claude/goualart/piscine/compass/index.html','w').write(s)
print("ok")
