models=( benthamHalfLookaheadBinary benthamHalfLookaheadTop benthamNoLookaheadTop egoisticHalfLookaheadTop rawSugarscape )
graphs=( meanTimeToLive percentPopGrowth starvationDeaths wealthCollected totalWealth)
scrapingScripts=( scrapeMeanTimeToLive scrapePercentPopGrowth scrapeStarvationDeaths scrapeWealthCollected scrapeTotalWealth)
plottingScripts=( plotMeanTimeToLive plotPercentPopGrowth plotStarvationDeaths plotWealthCollected plotTotalWealth)

tempDir=$(mktemp -d graphData.XXX)
cd $tempDir
absDir=$(pwd)

for ((index=0; index<${#graphs[@]}; index++)) #iterate over all graphs to be generated
do
    mkdir ${graphs[$index]}
    cd ${graphs[$index]}
    # pwd
    for ((model=0; model<${#models[@]}; model++)) #iterate over all decision models
    do
        # echo ${scrapingScripts[$index]}
        python3 "../../"${scrapingScripts[$index]}.py -p "../../../../100-run-json" -l ${models[$model]}".dat" -m ${models[$model]}
    done
    cd ..
done
cd ../../../plots

for ((graphIndex=0; graphIndex<"${#graphs[@]}"; graphIndex++))
do
    gnuplot -c '../data/scripts/'${plottingScripts[$graphIndex]}'.gp' $absDir
done

#cleanup temp
# trap "rm -rf $absDir" EXIT