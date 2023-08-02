models=( benthamHalfLookaheadBinary benthamHalfLookaheadTop benthamNoLookaheadTop egoisticHalfLookaheadTop rawSugarscape )
graphs=( meanTimeToLive percentPopGrowth starvationDeaths wealthCollected totalWealth)
scripts=( scrapeMeanTimeToLive scrapePercentPopGrowth scrapeStarvationDeaths scrapeWealthCollected scrapeTotalWealth)
scrapedDataPath=$(mktemp -d tempDataDir.XXX)
cd $scrapedDataPath

for model in "${models[@]}"
do
    for ((index=0; index<${#graphs[@]}; index++))
    do
        python3 "../"${scripts[$index]}.py -p "../../../jsonTest" -l ${graphs[$index]}.".dat" -m $model
    done
done


