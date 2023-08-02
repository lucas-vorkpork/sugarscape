set title "Starvation Deaths"
set xlabel "Timestep"
set ylabel "Number of Starvation Deaths"
set lt 1 lw 2 lc "black"
set term pdf
set output ARGV[1]
plot 'sppg.dat' with linespoints lt 1 dt 1 pt 0