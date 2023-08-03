set title "Agent Mean Time To Live"
set xlabel "Timestep"
set ylabel "Average Time To Live"
set xrange [0:1000]
set yrange [0:200]
set lt 1 lw 2 lc "black"
set term pdf
set output "meanTimeToLive.pdf"
path =ARGV[1].'/meanTimeToLive/'
plot path.'benthamHalfLookaheadBinary.dat' with linespoints lt 1 dt 1 pt 0, \
    path.'benthamHalfLookaheadTop.dat' with linespoints lt 1 dt 2 pt 0, \
    path.'benthamNoLookaheadTop.dat' with linespoints lt 1 dt 3 pt 0, \
    path.'egoisticHalfLookaheadTop.dat' with linespoints lt 1 dt 4 pt 0, \
    path.'rawSugarscape.dat' with linespoints lt 1 dt 5 pt 0