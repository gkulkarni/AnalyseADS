
# File: download_ads_data.py
#  Cre: 2014-07-06
#
# Downloads all 2013 refereed astronomy abstracts from ADS in plain
# text format.  Stores them in a pickle.  Use carefully, or they will
# block you!

import urllib2 
import pickle

# You need to provide `total' by manually doing a preliminary ADS
# search.
total = 24433
data = "foo"

for n in range(1,24433,3000):
    url = ("http://adsabs.harvard.edu/cgi-bin/nph-abs_connect?"
           "db_key=AST&qform=AST&sim_query=YES&ned_query=YES&adsobj_query=YES"
           "&aut_logic=OR&obj_logic=OR&author=&object=&start_mon=01&start_year=2013"
           "&end_mon=12&end_year=2013&ttl_logic=OR&title=&txt_logic=OR&text=&"
           "nr_to_return=3000&start_nr="+str(n)+"&jou_pick=NO&ref_stems=&data_and=ALL&"
           "group_and=ALL&start_entry_day=&start_entry_mon=&start_entry_year=&"
           "end_entry_day=&end_entry_mon=&end_entry_year=&min_score=&sort=SCORE&"
           "data_type=PLAINTEXT&aut_syn=YES&ttl_syn=YES&txt_syn=YES&aut_wt=1.0&"
           "obj_wt=1.0&ttl_wt=0.3&txt_wt=3.0&aut_wgt=YES&obj_wgt=YES&ttl_wgt=YES&"
           "txt_wgt=YES&ttl_sco=YES&txt_sco=YES&version=1")
    f = urllib2.urlopen(url) 
    data += f.read()
    print str(n)+" done!"

with open("ads_data.dat","wb") as f:
    pickle.dump(data,f)

