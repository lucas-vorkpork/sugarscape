set errorbars 4.0
set style fill transparent
set boxwidth 0.2 absolute
unset parametric
set yrange [0:850]
set linetype 1 lc rgb "black" lw 2 pt 11
set xtics rotate by -45
plot 'GNUPlotData3.txt' using 2:4:3:7:6:xticlabels(1) with candlesticks lt 1 lw 2 notitle whiskerbars, \
    '' using 2:5:5:5:5 with candlesticks lt 1 lw 2 notitle
