A quick demonstration of content extraction with elasticsearch
===============================================================

Inside this folder is a copy of the example code from my web SIG presentation at Oxford University

The aim is to extract tags from unstructured text

Step 1:
--------

Install Java SE 7 and Download a copy of elasticsearch and extract somewhere writable

Step 2
--------
Install the elasticsearch head plugin by changing to the elasticsearch directory and running
bin/plugin -install mobz/elasticsearch-head

Step 3
--------
set the ES_HEAP_SIZE as high as you can on your machine - i have 16 GB RAM...
	export ES_HEAP_SIZE=13g

Step 4
--------
Start elasticsearch by running
	./bin/elasticsearch

Step 5
-------
Install python and pip then run
	pip install elasicsearch



Step 6
--------
In a new terminal window run the indexing code using:
	python indexer.py


Step 7
--------
In a new terminal window run the indexing code using:
	python using_tags.py

Or for the description only version, use:
	python using_only_description.py

You can also run other queries in the browser using the head plugin at:

localhost:9200/_plugin/head/

Please contact me if you would like help indexing with Elasticsearch...


