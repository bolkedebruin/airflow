#!/usr/bin/env bash
set -o verbose

MINIKDC_VERSION=1.0-SNAPSHOT
MINIKDC_HOME=/tmp/minikdc
MINIKDC_CACHE=${CACHE}/minikdc
MINICLUSTER_URL=https://github.com/bolkedebruin/minikdc/files/324103/minikdc-${MINIKDC_VERSION}-bin.zip

PRINCIPALS="airflow airflow-webserver airflow-scheduler airflow-worker"

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

# setup cache dir
mkdir -p ${TRAVIS_CACHE}/minikdc

# Setup MiniKDC environment
mkdir -p ${MINIKDC_HOME}
mkdir -p ${MINIKDC_CACHE}

echo "Downloading and unpacking MiniKDC"
curl -z ${TRAVIS_CACHE}/minikdc/minikdc.zip -o ${TRAVIS_CACHE}/minikdc/minikdc.zip -L ${MINICLUSTER_URL}
unzip ${TRAVIS_CACHE}/minikdc/minikdc.zip -d /tmp

echo "Path = ${PATH}"

java -cp "/tmp/minikdc-${MINIKDC_VERSION}/*" org.apache.airflow.MiniKdc /tmp ${DIR}/minikdc.properties /tmp/minikdc.keytab \${PRINCIPALS} &
