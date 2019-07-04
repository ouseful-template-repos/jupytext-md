# jupytext-py
Define a BinderHub environment that lets you edit `.py` python files via a notebook UI using Jupytext.

If you mark code cells with `{"active": "ipynb"}` metadata (from a notebook menu, `View -> Cell Toolbar -> Edit Metadata`), then those code cells will be commented out in the saved `py` file  ([docs](https://jupytext.readthedocs.io/en/latest/examples.html#importing-jupyter-notebooks-as-modules)).

If you have downloaded this repo, you can build and run it locally on the command line from the top level of the directory:

`repo2docker --image-name jupytextnbpy --user-name jovyan --volume .:/home/jovyan/ .`


`nbgitpuller` is also installed so you can use this container as a Jupytext base container.
