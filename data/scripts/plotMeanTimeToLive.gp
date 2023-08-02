set title "Agent Mean Time To Live"
set xlabel "Timestep"
set ylabel "Average Time To Live"
set xrange [0:1000]
set yrange [0:200]
set lt 1 lw 2 lc "black"
set term pdf
set output ARGV[1]
plot 'smttl.dat' with linespoints lt 1 dt 1 pt 0, \
    'smttl2.dat' with linespoints lt 1 dt 2 pt 0, \
    'smttl3.dat' with linespoints lt 1 dt 3 pt 0, \