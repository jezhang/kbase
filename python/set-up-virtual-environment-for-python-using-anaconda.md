

### Step 1: Check if conda is installed in your path.

```sh
conda -V
```


### Step 2: Update the conda environment 

```sh
conda update conda
```

### Step 3: Set up the virtual environment

```sh
conda create -n envname python=x.x
conda create -n envname python=x.x anaconda
```

### Step 4: Activating the virtual environment

```sh
conda activate envname
```


### Step 5: Installation of required packages to the virtual environment

```sh
conda install -n yourenvname package
```

### Step 6: Deactivating the virtual environment

```sh
conda deactivate
```

### Step 7: Deletion of virtual environment

```sh
conda info --envs
conda remove -n envname -all
conda env remove -n xxxx
```




