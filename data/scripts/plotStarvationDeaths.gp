set title "Starvation Deaths"
set xlabel "Timestep"
set ylabel "Number of Starvation Deaths"
set lt 1 lw 2 lc "black"
set term pdf
set output "starvationDeaths.pdf"
path =ARGV[1].'/starvationDeaths/'
plot path.'benthamHalfLookaheadBinary.dat' with linespoints lt 1 dt 1 pt 0, \
    path.'benthamHalfLookaheadTop.dat' with linespoints lt 1 dt 2 pt 0, \
    path.'benthamNoLookaheadTop.dat' with linespoints lt 1 dt 3 pt 0, \
    path.'egoisticHalfLookaheadTop.dat' with linespoints lt 1 dt 4 pt 0, \
    path.'rawSugarscape.dat' with linespoints lt 1 dt 5 pt 0