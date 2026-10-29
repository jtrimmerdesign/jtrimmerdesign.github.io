import json, html, os, re
D=os.path.dirname(os.path.abspath(__file__))
S=json.load(open(f"{D}/content/site.json"))
e=html.escape
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@500;600;700&family=Source+Serif+4:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">'
def contact():
    l=[f'<a href="mailto:{S["email"]}">{S["email"]}</a>']
    if S["linkedin"]: l.append(f'<a href="{S["linkedin"]}">LinkedIn</a>')
    if S["bluesky"]: l.append(f'<a href="{S["bluesky"]}">Bluesky</a>')
    return '<nav class="contact" aria-label="Contact">'+''.join(l)+'</nav>'
def page(fn,title,body,cur,desc):
    nav=''.join(f'<a href="{h}"{" aria-current=\"page\"" if k==cur else ""}>{t}</a>' for k,h,t in [("home","index.html","Home"),("work","work.html","All projects"),("about","about.html","About"),("cv","cv.html","CV")])
    out=f'''<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)}</title><meta name="description" content="{e(desc)}">{FONTS}<link rel="stylesheet" href="css/style.css"></head><body><a class="skip" href="#main">Skip to content</a><header class="site"><a class="name" href="index.html">{S["name"]}, {S["role"]}</a><nav class="main" aria-label="Main">{nav}</nav>{contact()}</header><main id="main">{body}</main><footer class="site">&copy; {S["name"]}. Game content shown is copyright of its respective owners.</footer></body></html>'''
    open(f"{D}/{fn}","w").write(out)
def cards(ps):
    return '<ul class="grid">'+''.join(f'<li><a class="card" href="{p["file"]}"><strong>{e(p["title"])}</strong><span class="role">{e(p["role"])}. {e(p["tags"])}</span></a></li>' for p in ps)+'</ul>'
def inline(t):
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',e(t))
def paras(ls):
    o=''
    for t in ls:
        if t.startswith("## "): o+=f'<h3>{e(t[3:])}</h3>'
        elif t.startswith("PASTE"): o+=f'<p class="placeholder">[{e(t)}]</p>'
        else: o+=f'<p>{inline(t)}</p>'
    return o
P=S["projects"]
page("index.html",f'{S["name"]}, {S["role"]}',f'<section class="hero"><h1>Mission and encounter designer</h1><p>{e(S["home_bio"])}</p></section><h2>Projects</h2>{cards(P)}',"home",S["home_bio"])
page("work.html","All projects",f'<section class="hero"><h1>All projects</h1></section>{cards(P)}',"work","Projects by Jamie Trimmer")
for p in P:
    b=f'<section class="hero"><h1>{e(p["title"])}</h1></section>'
    b+='<dl class="ledger">'+''.join(f'<dt>{e(k)}</dt><dd>{e(v)}</dd>' for k,v in p["info"])+f'<dt>Link</dt><dd><a href="{p["link"]}">{p["link"].replace("https://","")}</a></dd></dl>'
    b+='<div class="prose">'+paras(p["intro"])+'</div>'
    for sid in p["studies"]:
        s=S["studies"][sid]
        b+=f'<article class="study" id="{sid}"><h2>{e(s["title"])}</h2>'
        if s["epigraph"]: b+=f'<blockquote class="epigraph">{e(s["epigraph"])}<footer>In-game dialogue</footer></blockquote>'
        if s["video"]: b+=f'<div class="media"><iframe src="https://www.youtube-nocookie.com/embed/{s["video"]}" title="{e(s["title"])}" loading="lazy" allowfullscreen></iframe></div>'
        elif s["image"]: b+=f'<div class="media"><img src="{s["image"]}" alt="" loading="lazy"></div>'
        b+='<div class="prose">'+paras(s["body"])+'</div></article>'
    page(p["file"],p["title"],b,"work",p["intro"][0])
A=S["about"]
ab=f'<section class="hero"><h1>{e(A["title"])}</h1></section><div class="about-grid"><div class="prose">{paras(A["bio"])}</div><img class="portrait" src="images/jt.jpg" alt="Jamie Trimmer" width="1000" height="563"></div>'
ab+='<section class="panel"><div class="panel-col"><h2>EXPERIENCE</h2><p class="employer">'+e(A["experience_employer"])+'</p><ul>'+''.join(f'<li>{e(t)}<ul class="sub"><li>{e(d)}</li></ul></li>' for t,d in A["experience"])+'</ul></div><div class="panel-col"><h2>SKILLS</h2><ul>'+''.join(f'<li>{e(s)}</li>' for s in A["skills"])+'</ul></div></section>'
page("about.html","About",ab,"about","About Jamie Trimmer")
cvb='<section class="hero"><h1>CV</h1></section><p><a class="button" href="assets/Jamie_Trimmer_CV.pdf" download>Download CV (PDF)</a></p><div class="cv-pages">'+''.join(f'<img src="assets/cv-{i}.png" alt="CV page {i}">' for i in (1,2))+'</div>'
page("cv.html","CV",cvb,"cv","CV of Jamie Trimmer")
print("built")
