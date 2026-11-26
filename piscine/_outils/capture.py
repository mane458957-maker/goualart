import sys,asyncio,io
from playwright.async_api import async_playwright
from PIL import Image
BASE='/home/claude/goualart/piscine/'
async def shot(p,slug):
    import os
    exe='/usr/bin/google-chrome' if os.path.exists('/usr/bin/google-chrome') else None
    b=await p.chromium.launch(executable_path=exe,args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--allow-file-access-from-files'])
    pg=await b.new_page(viewport={'width':1280,'height':800})
    await pg.route('**/*',lambda r: r.continue_() if r.request.url.startswith('file:') else r.abort())
    await pg.goto('file://'+BASE+slug+'/index.html'); await pg.wait_for_timeout(3500)
    await pg.evaluate("""document.querySelectorAll('.bigLogo img,.logo img').forEach(i=>{if(!i.naturalWidth){const s=document.createElement('span');s.textContent=i.alt;s.style.color='#fff';i.replaceWith(s)}})""")
    top=await pg.screenshot()
    await pg.evaluate("document.querySelector('#config').scrollIntoView()"); await pg.wait_for_timeout(1500)
    try: await pg.evaluate("st.night=1;st.nightT=1;st.lights=1;st.lightsT=1;st.sht-=5")
    except Exception as e: print(slug,'st err',e)
    await pg.wait_for_timeout(2500)
    cfg=await pg.screenshot()
    await b.close()
    a=Image.open(io.BytesIO(top)).convert('RGB'); c=Image.open(io.BytesIO(cfg)).convert('RGB')
    im=Image.new('RGB',(1280,1600)); im.paste(a,(0,0)); im.paste(c,(0,800))
    im=im.resize((900,1125),Image.LANCZOS); im.save(BASE+slug+'/apercu.jpg',quality=78)
async def main():
    async with async_playwright() as p:
        for s in sys.argv[1:]: await shot(p,s)
asyncio.run(main())
