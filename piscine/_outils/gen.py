# Générateur générique de démo (FR ou US) à partir d'un dict prospect.
# Usage : from gen import build ; build(P)
import re, os, json
ROOT = '/home/claude/goualart/piscine'

US_REVIEWS = [
 ("Mike R.", "Custom pool", "September", "From the first meeting to the first swim, everything was spot on. The build stayed on schedule and the crew left the yard spotless."),
 ("Jennifer L.", "Pool & spa", "August", "Our backyard is narrow and they found the right design. Seeing the 3D plan first really helped us decide."),
 ("David K.", "Remodel", "July", "New tile, coping and lighting. The pool is 15 years old and looks brand new. Great communication the whole way."),
 ("Ashley M.", "Geometric pool", "June", "Stunning result, exactly what we pictured. The lights at night are magical."),
 ("Chris P.", "Freeform pool", "May", "Tricky sloped lot, no problem at all. Clear quote and no surprises on the final invoice."),
 ("Megan T.", "Pool with sun shelf", "April", "The kids never want to get out! Reliable, punctual team with great advice on finishes."),
 ("Brian S.", "Spillover spa", "April", "Professional from start to finish. They walked us through all the equipment at handover."),
 ("Laura F.", "Pool service", "March", "Two years with them now and the water is always perfect. Quick to respond when the pump had an issue."),
]

def js(s):
    return json.dumps(s, ensure_ascii=False)

def sub1(s, pat, rep, label, flags=re.S):
    n = len(re.findall(pat, s, flags))
    if n == 0:
        print("INTROUVABLE:", label)
        return s
    return re.sub(pat, lambda m: rep, s, count=1, flags=flags)

def build(P):
    us = P['lang'] == 'us'
    s = open(f"{ROOT}/{'index-en.html' if us else 'index.html'}").read()
    for a, b in [('"frames/f_"', '"../frames/f_"'), ('"frames-pc/f_"', '"../frames-pc/f_"'), ('src="villa/', 'src="../villa/'), ('"formes/', '"../formes/')]:
        if a not in s: print("INTROUVABLE:", a)
        s = s.replace(a, b)
    s = sub1(s, r'<title>.*?</title>', f"<title>{P['title']}</title>", 'title')
    s = sub1(s, r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{P["meta"]}">', 'meta')
    # CONFIG
    for k in ['name', 'city', 'zone', 'phone', 'email', 'address']:
        s = sub1(s, rf'\n  {k}: "(?:[^"\\]|\\.)*"', f"\n  {k}: {js(P[k])}", 'cfg ' + k)
    s = sub1(s, r'\n  logoHtml: "[^\n]*",', f"\n  logoHtml: {js(P['logoHtml'])},", 'logoHtml')
    s = sub1(s, r'\n  whatsapp: "",', f"\n  whatsapp: {js(P.get('whatsapp',''))},", 'whatsapp')
    # textes visibles du logo par défaut (avant JS)
    s = s.replace('AQUA<span>VILLA</span></a>', P['logoHtml'] + '</a>').replace('data-c="logoHtml">AQUA<span>VILLA</span>', 'data-c="logoHtml">' + P['logoHtml'])
    s = sub1(s, r'<div class="tagline" id="tagline">.*?</div>', f'<div class="tagline" id="tagline">{P["hero"]}</div>', 'hero')
    s = sub1(s, r'<div class="subtag" id="subtag"><span data-c="city">[^<]*</span> · [^<]*</div>', f'<div class="subtag" id="subtag"><span data-c="city">{P["city"].replace("&","&amp;")}</span> · {P["subtag"]}</div>', 'subtag')
    s = sub1(s, r'<div class="eyebrow rv">(?:Constructeur depuis|Pool builder since) <span data-c="since">2009</span></div>\s*<h2 class="rv">[^<]*</h2>\s*<p class="lead rv">[^<]*</p>',
             f'<div class="eyebrow rv">{P["eyebrow"]}</div>\n    <h2 class="rv">{P["about_h2"]}</h2>\n    <p class="lead rv">{P["about_lead"]}</p>', 'about')
    for i, (st, lb) in enumerate(P['stats']):
        s = sub1(s, r'<div><strong(?: data-count="\d+")?>[^<]*</strong><span>(?:piscines construites|ans d\'expérience|garantie décennale|pour votre devis|pools built|years of experience|structural warranty|for your quote)</span></div>',
                 f'<div><strong>{st}</strong><span>{lb}</span></div>', f'stat{i}')
    s = sub1(s, r'(<div class="eyebrow rv">(?:Nos savoir-faire|What we do)</div>\s*<h2 class="rv">)[^<]*(</h2>)', None, 'svc h2') if False else s
    s = re.sub(r'(<div class="eyebrow rv">(?:Nos savoir-faire|What we do)</div>\s*<h2 class="rv">)[^<]*(</h2>)', lambda m: m.group(1) + P['svc_h2'] + m.group(2), s, count=1)
    cpat = r'<h3>(?:Piscine béton sur-mesure|Piscine coque|Rénovation|Entretien &amp; équipements|Custom concrete pools|Fibreglass pools|Renovation|Maintenance &amp; equipment)</h3><p>[^<]*</p><div class="price">[^<]*</div>'
    ms = list(re.finditer(cpat, s))
    if len(ms) < len(P['services']): print("INTROUVABLE: cartes", len(ms))
    for m, (h, p, pr) in reversed(list(zip(ms, P['services']))):
        s = s[:m.start()] + f'<h3>{h}</h3><p>{p}</p><div class="price">{pr}</div>' + s[m.end():]
    s = sub1(s, r'<p class="lead rv">[^\n]*?<span data-c="zone">.*?</p>', f'<p class="lead rv">{P["zone_lead"]}</p>', 'zone lead')
    s = sub1(s, r'<div>📍 <span data-c="address">[^<]*</span></div>', f'<div>📍 <span data-c="address">{P["address"]}</span></div>' + ''.join(f'\n        <div>{x}</div>' for x in P.get('extra_contact', [])), 'address div')
    s = sub1(s, r'<span data-c="email" data-href="mailto">[^<]*</span>|<a data-c="email" data-href="mailto">[^<]*</a>', f'<a data-c="email" data-href="mailto">{P["email"]}</a>', 'email vis')
    s = s.replace('06 00 00 00 00', P['phone']).replace('<span data-c="name">AquaVilla</span>', '<span data-c="name">'+P['name']+'</span>')
    s = sub1(s, r'· (?:Constructeur de piscines|Swimming pool builder)</div><div>[^<]*</div></div></footer>', f'· {P["footer1"]}</div><div>{P["footer2"]}</div></div></footer>', 'footer')
    # créations
    cr = P.get('creations', [])
    cjs = "  creations: [],\n" if len(cr) < 6 else "  creations: [\n" + ",\n".join(f'    {{ title:{js(t)}, place:{js(pl)}, img:{js(u)} }}' for t, pl, u in cr[:8]) + "\n  ],\n"
    s = sub1(s, r"  creations: \[\n.*?\n  \],\n", cjs, 'creations')
    if len(cr) in (6, 7):
        s = s.replace(".bento .b0{grid-column:span 2}", ".bento .b0{grid-column:span 2}\n@media(min-width:900px){.bento .b4,.bento .b5{grid-column:span 2}}\n@media(max-width:899px){.bento .b5{grid-column:span 2}}", 1)
    if P.get('models'):
        mj = "  models: [\n" + ",\n".join(f'    {{ name:{js(n)}, dims:{js(d)}, shape:6, L:{l}, W:{w} }}' for n, d, l, w in P['models']) + "\n  ],\n"
        s = sub1(s, r"  models: \[\n.*?\n  \],\n", mj, 'models')
    if P.get('score'):
        s = s.replace("  demoReviews: true,", f"  demoReviews: true,\n  score: {{ note:{js(P['score'][0])}, label:{js(P['score'][1])} }},")
    if us:
        s = s.replace('See it in your own villa.', 'See it in your own backyard.')
        s = s.replace('alt="Villa avec piscine"', 'alt="Home with a pool"')
        s = s.replace('callLabel: "📞 Appeler"', 'callLabel: "📞 Call"')
        s = s.replace('"Mosaïque noire brillante", water:"Effet miroir"', '"Glossy black mosaic", water:"Mirror effect"')
        s = s.replace('Filtration, chiller, lighting', 'Filtration, heater, lighting')
        s = s.replace('id="scoreN">4,9<', 'id="scoreN">4.9<')
        s = s.replace('We visit your villa to study the plot', 'We visit your home to study the yard')
        cities = P['us_places']
        rv = "  reviews: [\n" + ",\n".join(f'    {{ name:{js(n)}, city:{js(cities[i % len(cities)])}, project:{js(pj)}, date:{js(d)}, text:{js(t)} }}' for i, (n, pj, d, t) in enumerate(US_REVIEWS)) + "\n  ],\n"
        s = sub1(s, r"  reviews: \[\n.*?\n  \],\n", rv, 'reviews')
        if not P.get('models'):
            s = s.replace('dims:"10 × 5 m"', 'dims:"33 × 16 ft"').replace('dims:"9 × 4.5 m"', 'dims:"30 × 15 ft"').replace('dims:"10 × 6 m"', 'dims:"33 × 20 ft"').replace('dims:"5 × 3 m"', 'dims:"16 × 10 ft"').replace('dims:"8 × 4 m"', 'dims:"26 × 13 ft"').replace('dims:"9 × 5 m"', 'dims:"30 × 16 ft"')
    s = s.replace(".bigLogo span{color:var(--aqua2)}", ".bigLogo span{color:var(--aqua2)}\n.bigLogo{font-size:clamp(40px,9vw,120px)!important;white-space:nowrap}", 1)
    os.makedirs(f"{ROOT}/{P['slug']}", exist_ok=True)
    open(f"{ROOT}/{P['slug']}/index.html", 'w').write(s)
    # contrôles
    bad = ['AquaVilla', 'AQUAVILLA', 'aquavilla', 'Côte d', 'Alpes-Maritimes', '12 avenue des Pins', 'AED', 'Palm Jumeirah', 'Dubai']
    if us: bad += ['Appeler', 'Mosaïque', 'Devis', ' piscine', 'piscine"', ' m"']
    for b in bad:
        if b in s: print(P['slug'], "RESTE:", b, s.count(b))
    print("ok", P['slug'])
