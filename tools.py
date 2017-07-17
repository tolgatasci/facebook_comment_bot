#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import json
import collections
import fb
from tinydb import TinyDB, Query
from facepy import GraphAPI
import sys
import urllib
import random
reload(sys)
sys.setdefaultencoding("utf-8")
import pprint
from optparse import OptionParser
pages = TinyDB('pages.json');
page_work = TinyDB('pages_work.json');
token = ""
facebook = fb.graph.api(token)
graph1 = GraphAPI(token)
def add_database(id,caunt_fan):
	Pages = Query();
	donen = pages.search(Pages.page_id == id)
	if(len(donen)<1):
		pages.insert({'page_id': id,"count_fan":caunt_fan});
	else:
		print(id+" Database Exits Page");
def control(id):
	count_page_like = graph1.get(id+"/?fields=fan_count");
	if(count_page_like["fan_count"]>int(limit)):
		add_database(id,count_page_like["fan_count"]);
	else:
		print(id+" page_fan_count < "+limit);
	#print(count_page_like["fan_count"]);
def search(keyword):
		profile = graph1.get("/search?q="+urllib.quote(keyword)+"&type=page");
		for page in profile["data"]:
			control(page['id']);

parser = OptionParser()
parser.add_option("-s", "--search", dest="search",
                  help="Search Page", metavar="helpful_message")
parser.add_option("-l", "--limit", dest="limit",
                 help="Limit Plase", metavar="int")
(options, args) = parser.parse_args();
limit = options.limit;

if not options.search:
	print("Plase Required -s or --search keyword");
if not limit:
	limit = 10000;
search(options.search);
