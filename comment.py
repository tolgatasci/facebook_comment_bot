#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import json
import collections
import fb
from tinydb import TinyDB, Query
from facepy import GraphAPI
import sys
import random
import time
import pprint
reload(sys)

sys.setdefaultencoding("utf-8")

pages = TinyDB('pages.json');
page_work = TinyDB('pages_work.json');
#token = "#" müzik caddesi
token = "#";
facebook = fb.graph.api(token)
graph1 = GraphAPI(token)
def insert_test():
	Page_work = Query();
	page_work.insert({'post_id': '268986530241931_273519493121968'});
def yorum_cek():
	com =  ['Telefonuza müzik indirmek isterseniz, Müzik Caddesi programını Google Playden indirebilirsiniz.', 
			'Müzik indirme programını Google Play\'den indir. https://play.google.com/store/apps/details?id=com.muzikcaddesi.muzikcaddesi',
			'Müzik Caddesi hemen indir. Telefonuna müzik indir. Google Play\'de müzik caddesi aratarak indirebilirsin.', 
			'Şarkı dinlemeyi seviyorsan, telefonuna şarkı indiremiyorsan aradığım program Müzik Caddesi! Google play\'den aratabilir indirebilirsin.'];
	secure_random = random.SystemRandom();
	return secure_random.choice(com).encode("utf-8");
def kontrol(id):
	try:
		for sayfa in id:
			profile = graph1.get(sayfa["page_id"]+"/posts");
			
			if(len(profile["data"][0]["id"])< int(1)):
				break;
			ilkpost = profile["data"][0]["id"];	
			Pages_work = Query()
			donen = page_work.search(Pages_work.post_id == ilkpost)
			if(len(donen)<1):
				print(ilkpost+" commenting function ");
				yorum(ilkpost,sayfa["page_id"]);
			else:
				print(ilkpost+" comment exits master.");
	except:
		print "This is an error message!"			
def tara(id):
	Pages = Query();
	tara = pages.search(Pages.page_id == id)
	kontrol(tara);
def yorum(i,sayfa_id):
   Pages_work = Query();
   mess = yorum_cek();
   com = facebook.publish(cat = "comments", id = i, message = mess);
   print(com);
   facebook.publish(cat = "likes", id = i);
  
   page_work.insert({'post_id': i,"page_id":sayfa_id});
def sonsuz():
	Pages = Query();
	donen = pages.all();
	for pageid in donen:
		tara(pageid['page_id']);
		time.sleep(5);
		
	time.sleep(100);	
	sonsuz();

sonsuz();
