# Installation

Example with [stow](https://www.gnu.org/software/stow/):

	PREFIX=$HOME/stow/tojson
	git clone https://github.com/woky/tojson && cd tojson
	pip3 install --user .
	./setup.py install --root=$PREFIX --prefix=''

# Usage

	% tojson --help
	Usage: tojson [OPTIONS] [FILES]...

	  Converts YAML and TOML documents to concatenated JSON stream.

	  Each input document is converted into standalone JSON document. Input YAML
	  files can be composed of multiple documents. Only standard YAML tags are
	  recognized (yaml.safe_load_all() function is used). Converted JSON
	  documents are printed to standard output and separated by newline
	  character.

	  Input documents can be fed via standard input and/or positional arguments.
	  Format of each input document is guessed from its filename extension
	  (matching is case-insensitive, `yaml` and `yml` is YAML, `toml` is TOML)
	  unless you force the format with `--format` option. If your input files
	  have non-standard extension or one of input files is stdin, you need to
	  force the format or error will be reported. Standard input can be
	  specified either by `-` in positional arguments or by not supplying any
	  positional arguments.

	  Hosted at https://github.com/woky/tojson. Licensed under GPLv3.

	  This tool was created mainly for further processing of JSON documents by
	  jq (https://stedolan.github.io/jq/).

	Options:
	  -f, --format [yaml|toml]  Force format of all input files.
	  --help                    Show this message and exit.
