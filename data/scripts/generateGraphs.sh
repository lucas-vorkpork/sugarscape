models=( benthamHalfLookaheadBinary benthamHalfLookaheadTop benthamNoLookaheadTop egoisticHalfLookaheadTop rawSugarscape )
graphs=( meanTimeToLive percentPopGrowth starvationDeaths wealthCollected totalWealth)
scrapingScripts=( scrapeMeanTimeToLive scrapePercentPopGrowth scrapeStarvationDeaths scrapeWealthCollected scrapeTotalWealth)
plottingScripts=( )
tempDir=$(mktemp -d tempDataDir.XXX)
cd $tempDir
absDir=$(pwd)
for model in "${models[@]}"
do
    mkdir $model
    cd $model
    for ((index=0; index<${#graphs[@]}; index++))
    do
        python3 "../../"${scrapingScripts[$index]}.py -p "../../../../jsonTest" -l ${graphs[$index]}".dat" -m $model
    done
    cd ..
done
cd ../../../plots

for model in "${models[@]}"
do
    for 
done



