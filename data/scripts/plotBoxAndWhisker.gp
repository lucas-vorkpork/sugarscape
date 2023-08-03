#Note use 'call 'boxAndWhisker.gp' yAxisName' to execute script from interactive session
#use 'gnuplot -c boxAndWhisker.gp tester' to exectue script from terminals
set style fill transparent
set boxwidth 0.2 absolute
unset parametric
set linetype 1 lc rgb "black" lw 2 pt 11
set xtics rotate by -20
set xlabel "Decision Models"
set title ARGV[1]
set ylabel ARGV[2]
#change to epdfps for latex
set term pdf
set output ARGV[3].".pdf"
plot ARGV[4] using 2:4:3:7:6:xticlabels(1) with candlesticks lt 1 lw 2 notitle whiskerbars, \
    '' using 2:5:5:5:5 with candlesticks lt 1 lw 2 notitle