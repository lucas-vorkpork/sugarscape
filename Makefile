CLEAN = log.json \
		data/scripts/*.diff \
		data/scripts/*.json \
		data/scripts/*.log \
		data/scripts/*.logs
CONFIG = config.json
SUGARSCAPE = sugarscape.py

all: 

test:
	python $(SUGARSCAPE) --conf $(CONFIG)

data:
	cd data/scripts && sh collect.sh

generate:
	cd data/scripts && sh generate.sh

clean:
	rm -rf $(CLEAN) || true

.PHONY: all clean data generate

# vim: set noexpandtab tabstop=4:
