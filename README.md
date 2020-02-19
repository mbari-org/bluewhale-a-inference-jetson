# BlueA_infer
Blue Whale A inference optimization project using Jetson Nano
Authors: Daniel De Leon (Cal Poly) and Danelle Cline (MBARI)

## Steps to creating working evnironment
1. Create a python3 virtual environment with access to global libraries on the Nano
    * `virtualenv --python=python3 --system-site-packages <virtual_env_name>`
2. Activate virtual environment
    * in bash: `source <virtual_env_name>/bin/activate`
    * in fish: `. <virtual_env_name>/bin/activate.fish`
3. Install juypter notebook in the virtual environment
    * `pip3 install jupyter`
4. Install custom jupyter notebook kernel
    * `ipython kernel install --name "<kernel_name>" --user`
5. Run `jupyter notebook` and start a new notebook with your custom "kernel-name"
