# Collecte d'informations sur l'usage des crypto-monnaies

## Projet POM réalisé par :
- BERBEZIER Nathan
- VIALATOUX Lucas


## Description du sujet :

Récupérer les adresses reliées à des utilisateurs sur Twitter en crawlant Twitter.


## Basic Installation :

**Python:**
```bash
sudo apt-get python3
```

**Twint (pour ligne de commande):**
```bash
pip3 install twint
```
or

```bash
git clone https://github.com/twintproject/twint.git
cd twint
pip3 install . -r requirements.txt
```
## Basic utilisation :
```bash
python3 Main.py
```

## Advanced Installation (with visualization) :

**Elasticsearch:**
```bash
Download Elasticsearch from https://www.elastic.co/downloads/elasticsearch
Go to elasticsearch-X.X.X folder (where X.X.X is your version)
Open a new cmd in this folder and type : elasticsearch
Check on your web browser that http://localhost:9200/ is working
```

**Kibana:**
```bash
Download Kibana from https://www.elastic.co/downloads/kibana
Go to kibana-X.X.X-XXXXXX folder (where X.X.X-XXXXXX is your version and OS system)
Open a new cmd in this folder and type : kibana
Check on your web browser that http://localhost:5601/ is working
```

## Advanced utilisation :

**Set-up Visualisation Dashboard:**
```bash
Go to http://localhost:5601/
Select 'Management' tab, 'Saved Objects' and then select 'export.ndjson'.
After this just go to 'Dashboard' tab and click on 'Twint Dashboard'
```

**Scrap tweets directly to Visualisation Dashboard:**
```bash
python3 Graph.py
On http://localhost:5601/ just click Refresh button
```