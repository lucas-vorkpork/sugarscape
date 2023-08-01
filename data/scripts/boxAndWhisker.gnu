set errorbars 4.0
set style fill transparent
set boxwidth 0.2 absolute
unset parametric
plot 'GNUPlotData3.txt' using 2:4:3:7:6:xticlabels(1) with candlesticks lt 3 lw 2 notitle whiskerbars, \
    '' using 2:5:5:5:5 with candlesticks lt 3 lw 2 notitle
