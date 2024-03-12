---
marp: true
title: Odomknutie Budúcnosti Zubného Lekárstva
paginate: true
footer: 'AI: Dental'
theme: custom-default
class: invert
---

<!-- _footer: "" -->
# How can you work with our datasets?
## AI:Dental

![bg right](img/mascot/AID_4.svg)

---

# Setup python enviroment
```bash 
conda create -n dvc python>=3.12;
conda activate dvc;
```
# Install DVC for azure storage
```bash
pip install dvc>=3.47.0 dvc_azure>=3.1.0;
```

---

# Set up enviroments variables
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
# Make .dvc file dependency in **your git project**

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