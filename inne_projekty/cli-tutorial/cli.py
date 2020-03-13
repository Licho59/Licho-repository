#! python
# cli.py - step by step tutorial on 'click' library usage to transform script into reusable command-line interface (CLI) after medium post/tutorial: https://towardsdatascience.com/how-to-write-python-command-line-interfaces-like-a-pro-f782450caf0d

import click
import pandas as pd

@click.command()
@click.option("--in", "-i", "in_file", required=True, help='Path to csv file to be processed.',)
@click.option("--out-file", "-o", default="./output.xlsx", help="Path to excel file to store the result.")
def process(in_file, out_file):
    """
    Processes the input file IN and stores the result to output file )OUT.
    """
    input_file = pd.read_csv(in_file)
    input_file.to_excel(out_file)
    
if __name__ == '__main__':
    process()