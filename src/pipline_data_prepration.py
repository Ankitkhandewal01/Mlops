import os
import yaml
import argparse
import logging 

if __name__=="__main__":
    arg= argparse.ArgumentParser()
    arg.add_argument("--config",default="default")
    arg.add_argument("--datasource",default=None)

parsed_arg=arg.parse_args()
print(parsed_arg)
print(parsed_arg.config)