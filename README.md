# Collecte d'informations sur l'usage des crypto-monnaies

## Projet POM réalisé par :
- BERBEZIER Nathan
- VIALATOUX Lucas


## Description du sujet :

Récupérer les adresses reliées à des utilisateurs sur Twitter en crawlant Twitter.

## Statistiques :
**2016/01/01 jusqu'à 2016/12/31**
- Nombre de tweets : 11590
- Nombre d'adresses récoltées : 361
- Pourcentage : 3.11%
- Durée de la recherche : 18.97 min



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
**Default search : get adresses since 2016/01/01 and until 2016/12/31**
```bash
py Main.py
```

**Get adresses since 2019/03/15 and until 2019/12/31**
```bash
py Main.py -ts 2019-03-15 -tu 2019-12-31
```

**Get adresses with this searching phrase : 'my btc wallet is'**
```bash
py Main.py -p 'my btc wallet is'
```

**Get adresses with this searching phrase : 'my btc wallet is' since 2019/03/15 and until 2019/12/31**
```bash
py Main.py -p 'my btc wallet is' -ts 2019-03-15 -tu 2019-12-31
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
