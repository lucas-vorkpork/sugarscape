models=( benthamHalfLookaheadBinary benthamHalfLookaheadTop benthamNoLookaheadTop egoisticHalfLookaheadTop rawSugarscape )
descriptors=( agentWealthCollected agentWealthTotal environmentWealthCreated environmentWealthTotal \
                agentStarvationDeaths agentMeanTimeToLive agentMeanTimeToLiveAgeLimited agentReproduced )
tempDir=$(mktemp -d whiskerData.XXX)
cd $tempDir
absDir=$(pwd)
echo $tempDir

for desc in "${descriptors[@]}" #iterate over all graphs to be generated
do
    python3 "../boxAndWhiskerAggregate.py" "../../../100-run-json/" -l $desc".dat" -d $desc
done
pwd
cd ../../../plots

mkdir boxPlots
cd boxPlots

for ((graphIndex=0; graphIndex<"${#descriptors[@]}"; graphIndex++))
do
    case ${descriptors[$graphIndex]} in 
        "agentWealthCollected" | "agentWealthTotal" | "environmentWealthCreated" | "environmentWealthTotal")
            ylabel="wealth"
            ;;
        "agentStarvationDeaths")
            ylabel="deaths"
            ;;
        "agentMeanTimeToLive" | "agentMeanTimeToLiveLimited")
            ylabel="timesteps"
            ;;
        "agentReproduced")
            ylabel="babies"
            ;;
        *)
            ylabel="weeee"
            ;;
        esac
    gnuplot -c '../../data/scripts/plotBoxAndWhisker.gp' ${descriptors[$graphIndex]} $ylabel ${descriptors[$graphIndex]} $absDir'/'${descriptors[graphIndex]}'.dat'
done

#cleanup temp
# trap "rm -rf $absDir" EXIT
# gnuplot -c '../data/scripts/plotBoxAndWhisker.gp' 'population' 'ylabel' bnw 'agentMeanTimeToLive.dat'