# Installation

Example with [stow](https://www.gnu.org/software/stow/):

	PREFIX=$HOME/stow/tojson
	git clone https://github.com/woky/tojson && cd tojson
	pip3 install --user .
	./setup.py install --root=$PREFIX --prefix=''

# Usage

	% tojson --help
	Usage: tojson [FILES]...
	
	  Converts YAML and TOML documents to concatenated JSON stream.
	
	  Each input document is converted into standalone JSON document.
	  Input YAML files can be composed of multiple documents. Only
	  standard YAML tags are recognized (yaml.safe_load_all() function is
	  used). Converted JSON documents are printed to standard output and
	  separated by newline character. JSON document on input is copied to
	  output verbatim.
	
	  Input documents can be fed via standard input and/or positional
	  arguments. Format of input documents specified before any format
	  option (see below) is guessed from their filename extension
	  (matching is case-insensitive, both `yaml` and `yml` imply YAML).
	  You need to specify format for filenames with non-standard extension
	  or for standard input specified either explicitly by "-" argument or
	  implicitly by supplying no positional arguments.
	
	  Hosted at https://github.com/woky/tojson. Licensed under GPLv3.
	
	  This tool was created mainly for further processing of JSON
	  documents by jq (https://stedolan.github.io/jq/).
	
	Options:
	    -h, --help              Show this message and exit.
	
	  Following options change format of all positional arguments that
	  follows until another format option, or of standard input if no
	  positional arguments are specified.
	
	    -y, --yaml              Force YAML format
	    -t, --toml              Force TOML format
	    -j, --json              Force JSON format (verbatim copy)
	
	Examples:
	  Turn YAML documents on standard input into JSON stream:
	    tojson -y
	
	  Turn foo.yaml file and bar.toml on standard input into JSON stream:
	    tojson foo.yaml -t - <bar.toml
	
