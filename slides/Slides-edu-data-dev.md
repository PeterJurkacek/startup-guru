---
marp: true
title: Odomknutie Budúcnosti Zubného Lekárstva
paginate: true
footer: 'AI: Dental'
theme: custom-default
class: invert
---

<!-- _footer: "" -->
# The way you can train AI on our datasets
## AI:Dental

![bg right](img/mascot/AID_4.svg)

---

# Content
### 1. Setup python enviroment
### 2.a Download dataset into your project **(dvc import)**
### 2.b Download dataset during colab session **(dvc get)**
### More info

---

# Setup python enviroment
```bash 
conda create -n dvc python>=3.12;
conda activate dvc;
```

---

# Download dataset into your project **(dvc import)**

--- 

```bash
#!/bin/bash

pip install "dvc>=3.47.0" "dvc_azure>=3.1.0";

export GIT_REPO="Check your mail";
export GIT_COMMIT="Check your mail";
export GIT_DATASET_DVC_OUTPUT="Check your mail";
export GIT_DVC_REMOTE="Check your mail";
export AZURE_STORAGE_SAS_TOKEN="Check your mail";
export LOCAL_DATASET_PATH="Check your mail";

mkdir -p data;

# !!!Make sure you are in the git repository or run 
# git init;
dvc init;
dvc config core.autostage true;

mkdir -p data;

dvc import --remote $GIT_DVC_REMOTE -o data --no-download $GIT_REPO $GIT_DATASET_DVC_OUTPUT;

dvc update --rev $GIT_COMMIT $LOCAL_DATASET_PATH;
```

---

# Download dataset during colab session **(dvc get)**

---

```bash
#!/bin/bash

pip install "dvc>=3.47.0" "dvc_azure>=3.1.0";

export GIT_REPO="Check your mail";
export GIT_COMMIT="Check your mail";
export GIT_DATASET_DVC_OUTPUT="Check your mail";
export GIT_DVC_REMOTE="Check your mail";
export AZURE_STORAGE_SAS_TOKEN="Check your mail";
export LOCAL_DATASET_PATH="Check your mail";

mkdir -p data;

dvc get --remote $GIT_DVC_REMOTE -o data $GIT_REPO $GIT_DATASET_DVC_OUTPUT;
```

---

# More info

---


# Install DVC for azure storage
```bash
pip install dvc>=3.47.0 dvc_azure>=3.1.0;
```

---

# Set up enviroment variables
### *NOTE: Check your email*
```bash
export GIT_ACCESS_TOKEN='Will be provided by AID';
export GIT_COMMIT='Will be provided by AID';
export GIT_REPO="Will be provided by AID";
export GIT_DATASET_DVC_OUTPUT="Will be provided by AID";
export GIT_DVC_REMOTE="Will be provided by AID";
export AZURE_STORAGE_SAS_TOKEN="Will be provided by AID"
export LOCAL_DATASET_PATH="data/up_to_you";
```
---


# Go to your project
*NOTE: E.g. your training pipeline, experiment repo, ...*
```bash
cd your_project;
```
```bash
# Initialize a new Git repository
git init;
```
```bash
# Initialize a new DVC (Data Version Control) repository
dvc init;
# Configure DVC to automatically stage changes
dvc config core.autostage true;
```

---
# Import dataset dependency **your git project**

*NOTE: Check if you have file after run: `$LOCAL_DATASET.dvc`*

```bash
# # Make sure that enviroment variable `AZURE_STORAGE_SAS_TOKEN` is set

# Create a directory to store data
mkdir -p $LOCAL_DATASET_PATH;

# Import data from a remote repository into the local DVC repository without downloading it. It will make .dvc file
dvc import --remote $GIT_DVC_REMOTE -o $LOCAL_DATASET_PATH --no-download $GIT_REPO $GIT_DATASET_DVC_OUTPUT;
```

---
# Run to see if everything is **up to date**
```bash
# Make sure that enviroment variable `AZURE_STORAGE_SAS_TOKEN` is set
dvc update --rev $GIT_COMMIT $LOCAL_DATASET_PATH --no-download;
```


# Run to **download** dataset

```bash
# Make sure that enviroment variable `AZURE_STORAGE_SAS_TOKEN` is set
dvc update --rev $GIT_COMMIT $LOCAL_DATASET_PATH;
```