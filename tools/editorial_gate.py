#!/usr/bin/env python3
"""Offline quality gate for PhiBee edition JSON. Does not claim to verify URLs live."""
import json,sys,re
from pathlib import Path
from urllib.parse import urlparse
CATS={'crypto','world','nature','meditation','ideas','creator','ayurveda','yoga','strength'}
if len(sys.argv)!=2:sys.exit('Usage: python3 editorial_gate.py EDITION.json')
p=Path(sys.argv[1]); d=json.loads(p.read_text(encoding='utf-8'))
errors=[];items=d.get('discoveries',[])
if len(items)!=9 or {x.get('category') for x in items}!=CATS:errors.append('Exactly nine distinct required categories')
seen=set()
for x in items:
 c=x.get('category','?');url=x.get('url','');u=urlparse(url)
 for field in ('headline','why','source','format','duration','published_date'):
  if not str(x.get(field) or '').strip():errors.append(f'{c}: missing {field}')
 if u.scheme!='https' or not u.netloc:errors.append(f'{c}: invalid HTTPS experience URL')
 if u.path in ('','/') and not u.query:errors.append(f'{c}: generic homepage URL; use direct experience')
 if url in seen:errors.append(f'{c}: duplicate URL')
 seen.add(url)
 if c=='nature' and not str(x.get('credit') or '').strip():errors.append('nature: photographer/creator credit required')
 if str(x.get('published_date','')).lower().strip() in ('today','recent','new'):errors.append(f'{c}: vague publication date')
 q=x.get('quote')
 if q is not None:
  if not (isinstance(q,dict) and str(q.get('text','')).strip() and str(q.get('by','')).strip() and str(q.get('source_url','')).startswith('https://')):errors.append(f'{c}: a quote needs text, by and an https source_url where it was verified')
  elif len(str(q['text']).split())>60:errors.append(f'{c}: keep quotes under 60 words')
 if 'podcast' in str(x.get('format','')).lower() and not isinstance(x.get('listen_minutes'),int):errors.append(f'{c}: podcasts need listen_minutes (a whole number)')
if not any('podcast' in str(x.get('format','')).lower() for x in items):errors.append('At least one podcast each day, for listening on the go')
if errors:
 print('EDITORIAL GATE FAILED:');print('\n'.join('- '+e for e in errors));sys.exit(2)
print('EDITORIAL STRUCTURE PASSED. Still requires HUMAN/AI SOURCE VERIFICATION: URLs reachable, attribution, content accuracy, freshness, rights, and quality.')
