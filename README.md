# Collecte d'informations sur l'usage des crypto-monnaies

## Projet POM réalisé par :
- BERBEZIER Nathan
- VIALATOUX Lucas


## Description du sujet :

Récupérer les adresses reliées à des utilisateurs sur Twitter en crawlant Twitter.

## Statistiques :
**1.000 threads**
Nombre de tweets : 1004
Nombre d'adresses récoltées : 217
Pourcentage : 21.61%
Durée traitement : 0.8 minutes

**10.000 threads**
Nombre de tweets : 10.002
Nombre d'adresses récoltées : 3028
Pourcentage : 30%
Durée traitement : 8 minutes

**50.000 threads**
Nombre de tweets : 12.059
Nombre d'adresses : 4090
Pourcentage : 34%
Durée traitement : 11 minutes



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

## Some examples :
Get last 100 tweets
```bash
py Main.py
```

Get last 1.000 tweets since 2016/01/01 and until 2016/01/31
```bash
py Main.py -n 1000 -ts 2016-01-01 -tu 2016-01-31
```

Get last 1.000 tweets since 2016/01/01 and until 2016/01/31
```bash
py Main.py -n 1000 -ts 2016-01-01 -tu 2016-01-31
```

Get last 1.000 tweets before 2016
```bash
py Main.py -n 1000 -y 2016
```

Get last 1.000 tweets from username 'test'
```bash
py Main.py -n 1000 -u test
```

Get last 1.000 tweets with this searching phrase : 'my btc wallet is'
```bash
py Main.py -n 1000 -p 'my btc wallet is'
```

## Advanced Installation (with visualization) :

**Elasticsearch:**
```bash
Download 'Elasticsearch' from https://www.elastic.co/downloads/elasticsearch
Go to 'elasticsearch-X.X.X' folder (where X.X.X is your version)
Open a new cmd in this folder and type : 'elasticsearch'
Check on your web browser that 'http://localhost:9200/' is working
```

**Kibana:**
```bash
Download 'Kibana' from https://www.elastic.co/downloads/kibana
Go to 'kibana-X.X.X-XXXXXX' folder (where X.X.X-XXXXXX is your version and OS system)
Open a new cmd in this folder and type : 'kibana'
Check on your web browser that 'http://localhost:5601/' is working
```

## Advanced utilisation :

**Start Elasticsearch & Kibana:**
```bash
Go to 'elasticsearch-X.X.X' folder (where X.X.X is your version)
Run 'bin/elasticsearch' (or 'bin\elasticsearch.bat' on Windows)
Go to 'kibana-X.X.X-XXXXXX' folder (where X.X.X-XXXXXX is your version and OS system)
Run 'bin/kibana' (or 'bin\kibana.bat' on Windows)
```

**Set-up Visualisation Dashboard:**
```bash
Go to 'http://localhost:5601/'
Select 'Management' tab, 'Saved Objects' and then select 'export.ndjson'.
After this just go to 'Dashboard' tab and click on 'Twint Dashboard'
```

**Scrap tweets directly to Visualisation Dashboard:**
```bash
python3 Graph.py
On 'http://localhost:5601/' just click 'Refresh' button
```
