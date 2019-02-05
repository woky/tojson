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

def detect_format(f):
    if yaml_re.match(f.name):
        return 'yaml'
    if toml_re.match(f.name):
        return 'toml'
    raise click.UsageError('Cannot determine format of file ' + f.name)

def parse_yaml(f):
    return yaml.safe_load_all(f)

def parse_toml(f):
    return [ pytoml.load(f) ]

parse_funs = {
    'yaml': parse_yaml,
    'toml': parse_toml,
}

@click.command()
@click.option('-f', '--format',
        type=click.Choice(['yaml', 'toml']),
        help='Force format of all input files.')
@click.argument('files', type=click.File('r'), nargs=-1)
def convert(format, files):
    '''
    Converts YAML and TOML documents to concatenated JSON stream.

    Each input document is converted into standalone JSON document.
    Input YAML files can be composed of multiple documents. Converted
    JSON documents are printed to standard output and separated by
    newline character.

    Input documents can be fed via standard input and/or positional
    arguments. Format of each input document is guessed from its
    filename extension (matching is case-insensitive, `yaml` and `yml`
    is YAML, `toml` is TOML) unless you force the format with
    `--format` option. If your input files have non-standard extension
    or one of input files is stdin, you need to force the format or
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
        parse = parse_funs[format]
    for f in files:
        if not format:
            parse = parse_funs[detect_format(f)]
        for doc in parse(f):
            print(json.dumps(doc))

if __name__ == '__main__':
    convert()
