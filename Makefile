.ONESHELL:
README.md: tojson README.md.pre README.md.post
	exec >$@
	cat README.md.pre
	./tojson --help | sed 's/^/\t/'
	cat README.md.post
