# jupytext-py
Define a BinderHub environment that supports Jupytext dualled python (`.py`) and ipynb files.

Any `.ipynb` files created in a top-level `notebooks` directory will be paired with a Jupytext markdown file in a top level `py` directory, and *vice versa*.

When run using BinderHub/`repo2docker`, the `notebooks` and `py` directories will be automatically created if they do not already exist.

Files in subdirectories will not be paired.

You can change the directory names (for example, you could use a hidden directory) by changing the settings in the `binder/postBuild` config file. If you don't specify directory paths, all python and ipynb files will be paired on whatever path they are located.

If you have downloaded this repo, you can build and run it locally on the command line from the top level of the directory:

`repo2docker --image-name jupytextnbpy --user-name jovyan --volume .:/home/jovyan/ .`

If `notebooks` and `py` directories exist in the host directory, you can mount them as volumes against the corresponding directories inside the container:

`repo2docker --image-name jupytextnbpy --user-name jovyan --volume notebooks:/home/jovyan/notebooks --volume py:/home/jovyan/py .`

`nbgitpuller` is also installed so you can use this container as a Jupytext base container.
