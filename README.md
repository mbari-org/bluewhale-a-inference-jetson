# BlueA_infer
Blue Whale A inference optimization project using Jetson Nano
Authors: Daniel De Leon (Cal Poly) and Danelle Cline (MBARI)

## Creating working evnironment
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

## TensorFlow .pb to .UFF
`python3 /usr/lib/python3.6/dist-packages/uff/bin/convert_to_uff.py <model_name.pb>`

## .UFF to serialized .engine file
* Run pb2uff.ipynb:
    * Make sure "Automatically deduced input nodes" and "Automatically deduced out nodes" names are placed in the parser.register_input and parser.register_output function - not the names from graph in TF before making the pb file
    * The dimension of the input, however, do need to match those from TF
    * TODO: Find best max_batch_size and max_workspace_size parameter values for engine
