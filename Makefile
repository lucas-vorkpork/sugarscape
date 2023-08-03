CLEAN = log.json \
		data/configs/*.diff \
		data/configs/*.json \
		data/configs/*.log \
		data/configs/*.logs \
		plots/*.pdf \
		data/scripts/graphData.??? \
		data/scripts/whiskerData.??? \
		plots/boxplots
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

graphs:
	cd data/scripts && sh generateLineGraphs.sh && sh generateWhiskersAggregate.sh

.PHONY: all clean data generate

# vim: set noexpandtab tabstop=4:
