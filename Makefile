.ONESHELL:
README.md: %: %.in
	exec >$@
	cat $<
	./tojson --help | sed 's/^/\t/'
