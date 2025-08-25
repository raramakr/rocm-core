#Scope:
The current scope of this is for producing AMD vendor packaging for hosting in AMD repositories. We expect that a good deal of this work can be adapted for future upstream OS packaging activities, but those are currently out of scope of what is being built here

#Prerequisites:
Python version required : python 3.12 or above
Install rpm package. Ex: apt install rpm (in Ubuntu)
pip install -r requirements.txt

#Usage:
./build_package.py --artifact-url "https://therock-artifacts.s3.amazonaws.com/16418185899-linux/index-gfx94X-dcgpu.html" --dest-dir ./OUTPUT_PKG --rocm-version 7.1.0

For more options ./build_package.py -h
