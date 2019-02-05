#!/usr/bin/env python3
# Licensed under GPLv3

import sys
import re
import json

import click
import yaml
import pytoml

yaml_re = re.compile('\.ya?ml$', re.I)
toml_re = re.compile('\.toml$', re.I)
json_re = re.compile('\.json$', re.I)

def detect_format(f):
    if yaml_re.search(f.name):
        return 'yaml'
    if toml_re.search(f.name):
        return 'toml'
    if json_re.search(f.name):
        return 'json'
    raise click.UsageError('Cannot determine format of file ' + f.name)

def convert_yaml(f):
    for doc in yaml.safe_load_all(f):
        print(json.dumps(doc))

def convert_toml(f):
    print(pytoml.load(f))

def convert_json(f):
    print(f.read())

convert_funs = {
    'yaml': convert_yaml,
    'toml': convert_toml,
    'json': convert_json,
}

@click.command()
@click.option('-f', '--format',
        type=click.Choice(['yaml', 'toml', 'json']),
        help='Force format of all input files.')
@click.argument('files', type=click.File('r'), nargs=-1)
def convert(format, files):
    '''
    Converts YAML and TOML documents to concatenated JSON stream.

    Each input document is converted into standalone JSON document.
    Input YAML files can be composed of multiple documents. Only
    standard YAML tags are recognized (yaml.safe_load_all() function
    is used). Converted JSON documents are printed to standard output
    and separated by newline character. JSON document on input is
    copied to output verbatim.

    Input documents can be fed via standard input and/or positional
    arguments. Format of each input document is guessed from its
    filename extension (matching is case-insensitive, both `yaml` and
    `yml` implies YAML) unless you force the format with `--format`
    option. If your input files have non-standard extension or one of
    input files is standard input, you need to force the format or
    error will be reported. Standard input can be specified either by
    `-` in positional arguments or by not supplying any positional
    arguments.

    Hosted at https://github.com/woky/tojson. Licensed under GPLv3.

    This tool was created mainly for further processing of JSON
    documents by jq (https://stedolan.github.io/jq/).
    '''
    if not files:
        files = [sys.stdin]
    if format:
        convert = convert_funs[format]
    for f in files:
        if not format:
            convert = convert_funs[detect_format(f)]
        convert(f)

if __name__ == '__main__':
    convert()
