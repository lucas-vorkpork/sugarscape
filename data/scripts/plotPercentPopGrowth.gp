set title "Percent Population Growth From Last Timestep"
set xlabel "Timestep"
set ylabel "Percent Population Growth"
set lt 1 lw 2 lc "black"
set term pdf
set output ARGV[1]
plot 'sppg.dat' with linespoints lt 1 dt 1 pt 0