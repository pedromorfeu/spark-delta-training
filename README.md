# Spark Delta training material

## Setup

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

## MacOS initial setup

* install iterm https://iterm2.com/
  * --> install oh my zsh https://github.com/ohmyzsh/ohmyzsh?tab=readme-ov-file#basic-installation
    * (optional) set color preset “Solarized Dark“
  * --> Alt+backspace fix https://stackoverflow.com/questions/63557311/mac-os-x-iterm2-backward-delete-word
* install brew https://brew.sh/
* install Slack https://slack.com/downloads/instructions/mac?os=osx&build_architecture=
  * --> Access https://colbatechnologies.slack.com/
* install Teams https://www.microsoft.com/en-us/microsoft-teams/download-app
  * --> for older Mac (Monterery 12.7.6) https://answers.microsoft.com/en-us/msoffice/forum/all/i-have-an-old-mac-with-old-software-monterey-1276/79f96cbb-1956-40d2-aabf-8a5b0a648c5b  
* install git https://cli.github.com/
* install sublime text https://www.sublimetext.com/download
* install intellij community https://www.jetbrains.com/idea/download/?section=mac
  * --> install python community plugin
  * --> macos comes with python3 (3.9.6) in /usr/bin/python3
* install JDK 1.8 Azul https://formulae.brew.sh/cask/zulu@8
* install spark https://spark.apache.org/downloads.html
  * --> version 3.5.0 https://archive.apache.org/dist/spark/spark-3.5.0/  - spark-3.5.0-bin-hadoop3.tgz
  * --> unzip
  * --> move to the final folder (example: ˜/spark/)
  * --> running with Delta: `./spark/spark-3.5.0-bin-hadoop3/bin/pyspark --packages io.delta:delta-spark_2.12:3.2.0 --conf spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension --conf spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog`
* install python 3.11.0 https://www.python.org/downloads/macos/
* install Postgres 17 https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
* install Docker Desktop https://www.docker.com/products/docker-desktop/ 
