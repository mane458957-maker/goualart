# Démos vague Moyen-Orient du 26/11/2026 (template anglais)
import re,os,json
BASE='/home/claude/goualart/piscine/'
T=open(BASE+'index-en.html').read()
def A(t,p=""): return (t,p)
P=json.load(open(os.path.join(os.path.dirname(__file__),'prospects_2026_11_26.json')))
def gen(d):
    s=T
    R=[('"frames/f_"','"../frames/f_"'),('"frames-pc/f_"','"../frames-pc/f_"'),('src="villa/','src="../villa/'),('"formes/','"../formes/'),
       ('<title>AQUAVILLA — Swimming Pool Builder</title>',f'<title>{d["title"]}</title>'),
       ('content="Custom swimming pool builder: concrete, fibreglass, renovation. Free design and quote."',f'content="{d["desc"]}"'),
       ('name: "AquaVilla"',f'name: "{d["name"]}"'),
       ('logoHtml: "AQUA<span>VILLA</span>"',f'logoHtml: "{d["logo"]}"'),
       ('AQUA<span>VILLA</span></a>',d["logo"]+'</a>'),
       ('data-c="logoHtml">AQUA<span>VILLA</span></div>','data-c="logoHtml">'+d["logo"]+'</div>'),
       ('city: "Côte d\'Azur"',f'city: "{d["city"]}"'),
       ('since: "2009"',f'since: "{d.get("since") or ""}"'),
       ('zone: "Alpes-Maritimes & Var"',f'zone: "{d["zone"]}"'),
       ('phone: "06 00 00 00 00"',f'phone: "{d["phone"]}"'),
       ('whatsapp: "",',f'whatsapp: "{d["wa"]}",'),
       ('email: "contact@aquavilla.fr"',f'email: "{d["email"]}"'),
       ('address: "12 avenue des Pins, 06000 Nice"',f'address: "{d["address"]}"'),
       ('callLabel: "📞 Appeler"','callLabel: "📞 Call"'),
       ('{ name:"Noir",       material:"Mosaïque noire brillante", water:"Effet miroir",','{ name:"Black",      material:"Glossy black mosaic",      water:"Mirror effect",'),
       ('alt="Villa avec piscine"','alt="Villa with pool"'),
       ('Your garden has potential.<br><em>We turn it into a pool.</em>',d["tagline"]),
       ('<span data-c="city">Côte d\'Azur</span> · Free quote</div>',f'<span data-c="city">{d["city"]}</span> · {d["subtag"]}</div>'),
       ('Pool builder since <span data-c="since">2009</span>',d["eyebrow"]),
       ('<h2 class="rv">Pools designed to last, built to be lived in.</h2>',f'<h2 class="rv">{d["h2"]}</h2>'),
       ('Concrete, fibreglass or renovation: we design, build and maintain. One team, from the first sketch to the first swim.',d["lead"]),
       ('<h2 class="rv">A pool for every plot and every budget.</h2>',f'<h2 class="rv">{d["svc_h2"]}</h2>'),
       ('We work across <span data-c="zone">Alpes-Maritimes &amp; Var</span>. Free site visit and design.',d["zone_html"]),
       ('<div>📍 <span data-c="address">12 avenue des Pins, 06000 Nice</span></div>',f'<div>📍 <span data-c="address">{d["address"]}</span></div>'+d.get("extra_contact","")),
       ('· Swimming pool builder</div><div>Structural warranty · Legal notice</div>',f'· {d["foot1"]}</div><div>{d["foot2"]}</div>'),
       ('<span data-c="name">AquaVilla</span>','<span data-c="name">'+d["name"]+'</span>'),('alt="Piscine ${s.title}"','alt="Pool ${s.title}"'),('<div class="no">FORME DE PISCINE</div>','<div class="no">POOL SHAPE</div>'),
       ('06 00 00 00 00</a>',d["phone"]+'</a>'),('contact@aquavilla.fr</a>',(d["email"] or "")+'</a>')]
    for a,b in R:
        if a not in s: print(d["slug"],"INTROUVABLE:",a[:60])
        s=s.replace(a,b)
    st='\n'.join(f'      <div><strong>{a}</strong><span>{b}</span></div>' for a,b in d["stats"])
    s,n=re.subn(r'(<div class="stats rv">\n).*?(\n    </div>)',lambda m:m.group(1)+st+m.group(2),s,count=1,flags=re.S); assert n
    cards='\n'.join(f'      <article class="card rv"><div class="n">0{i+1}</div><h3>{h}</h3><p>{p}</p><div class="price">{pr}</div></article>' for i,(h,p,pr) in enumerate(d["cards"]))
    s,n=re.subn(r'(<div class="cards">\n).*?(\n    </div>)',lambda m:m.group(1)+cards+m.group(2),s,count=1,flags=re.S); assert n
    cr=d.get("creations") or []
    if len(cr)>=6:
        cjs="  creations: [\n"+",\n".join(f'    {{ title:"{a}", place:"{b}", img:"{c}" }}' for a,b,c in cr)+"\n  ],\n"
    else: cjs="  creations: [],\n"
    s,n=re.subn(r"  creations: \[\n.*?\n  \],\n",lambda m:cjs,s,count=1,flags=re.S); assert n
    s=s.replace(".bigLogo span{color:var(--aqua2)}",".bigLogo span{color:var(--aqua2)}\n.bigLogo{letter-spacing:4px}")
    low=s.lower()
    for bad in []:
        # vérifie le texte visible (hors commentaires)
        vis=re.sub(r'<!--.*?-->|//[^\n]*|/\*.*?\*/','',s,flags=re.S).lower()
        if bad in vis and bad not in ("nice",): print(d["slug"],"RESTE:",bad)
    if d.get("country","UAE")!="UAE":
        for a,b in [('city:"Palm Jumeirah"','city:"%s"'%d["city"]),('city:"Dubai Hills"','city:"%s"'%d["city"]),('city:"Al Barari"','city:"%s"'%d["city"]),('city:"Arabian Ranches"','city:"%s"'%d["city"]),('city:"Emirates Hills"','city:"%s"'%d["city"]),('city:"Jumeirah"','city:"%s"'%d["city"]),('city:"Mirdif"','city:"%s"'%d["city"]),('city:"The Springs"','city:"%s"'%d["city"])]:
            s=s.replace(a,b)
    if d.get("logo_url"):
        img='<img src=\\"%s\\" alt=\\"%s\\">'%(d["logo_url"],d["name"].replace('"',''))
        img2='<img src="%s" alt="%s">'%(d["logo_url"],d["name"].replace('"',''))
        s=s.replace('logoHtml: "'+d["logo"]+'"','logoHtml: "'+img+'"').replace(d["logo"]+'</a>',img2+'</a>').replace('data-c="logoHtml">'+d["logo"],'data-c="logoHtml">'+img2)
        if d.get("logo_mode")=="blanc":
            css=".bigLogo img{height:clamp(90px,22vw,190px);width:auto;max-width:86vw;object-fit:contain;display:block;filter:drop-shadow(0 6px 24px rgba(0,0,0,.45))}\n.logo img{height:40px;width:auto;max-width:200px;object-fit:contain;display:block}"
        else:
            css=".bigLogo img{height:clamp(90px,22vw,190px);width:auto;max-width:86vw;object-fit:contain;display:block;background:#fff;padding:clamp(10px,2vw,18px) clamp(16px,3vw,28px);border-radius:20px;box-shadow:0 10px 40px rgba(0,0,0,.35)}\n.logo img{height:40px;width:auto;max-width:200px;object-fit:contain;display:block;background:#fff;padding:4px 10px;border-radius:10px}"
        s=s.replace(".bigLogo span{color:var(--aqua2)}",".bigLogo span{color:var(--aqua2)}\n"+css,1)
    else: print(d["slug"],"ATTENTION logo texte")
    vis=re.sub(r'<script.*?</script>|<!--.*?-->','',s,flags=re.S)
    for bad in ['AquaVilla','AQUAVILLA','Côte d','Alpes-Maritimes','avenue des Pins','Appeler','Mosaïque','Devis gratuit','Piscine ','AED']:
        if bad in s: print(d["slug"],"RESTE:",bad,s.count(bad))
    os.makedirs(BASE+d["slug"],exist_ok=True)
    open(BASE+d["slug"]+'/index.html','w').write(s)
import sys
for d in P:
    if len(sys.argv)<2 or d['slug'] in sys.argv[1:]: gen(d)
print("ok",len(P))
