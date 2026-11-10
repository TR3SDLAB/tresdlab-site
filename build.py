from pathlib import Path
import json
root=Path(__file__).resolve().parent.parent
items=[]
for p in (root/'conteudo').glob('*.json'):
    d=json.loads(p.read_text(encoding='utf-8'))
    if not d.get('active',True): continue
    price=lambda n: 'R$ '+format(float(n),'.2f').replace('.',',')
    items.append({'name':d['name'],'cat':d.get('category','Outros'),'price':price(d.get('price',0)), 'desc':d.get('description',''),'photos':d.get('photos') or [],'options':[{'label':o['label'],'price':price(o['price'])} for o in (d.get('options') or [])], 'frames':d.get('frames360') or [],'model3d':d.get('model3d') or '', 'order':d.get('order',99)})
items.sort(key=lambda x:(x['order'],x['name']))
contact=json.loads((root/'conteudo-loja'/'contato.json').read_text())
(root/'catalogo.js').write_text('window.CATALOGO_PRODUTOS='+json.dumps(items,ensure_ascii=False)+';\nwindow.CATALOGO_WHATSAPP='+json.dumps(contact.get('whatsapp',''))+';\n',encoding='utf-8')
print('Catálogo gerado:',len(items),'produtos')
