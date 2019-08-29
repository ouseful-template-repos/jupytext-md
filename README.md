# jupytext-md (minimal)
Define a BinderHub environment that runs notebooks from Jupytext markdown and that doesn't save notebook files.

Any documents with file types supported by Jupytext, including `.md`, will be opened as a notebook from the notebook tree menu. 

This can be useful if you do not want to save any documents that contain the outputs of executed code cells.

If you have downloaded this repo, you can build and run it locally on the command line from the top level of the directory:

`repo2docker --image-name jupytextmd --ref minimal --user-name jovyan --volume .:/home/jovyan/ .`

`nbgitpuller` is also installed so you can use this container as a Jupytext base container.
