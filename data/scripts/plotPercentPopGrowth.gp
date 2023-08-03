set title "Percent Population Growth From Last Timestep"
set xlabel "Timestep"
set ylabel "Percent Population Growth"
set lt 1 lw 2 lc "black"
set term pdf
set output "percentPopGrowth.pdf"
path =ARGV[1].'/percentPopGrowth/'
plot path.'benthamHalfLookaheadBinary.dat' with linespoints lt 1 dt 1 pt 0, \
    path.'benthamHalfLookaheadTop.dat' with linespoints lt 1 dt 2 pt 0, \
    path.'benthamNoLookaheadTop.dat' with linespoints lt 1 dt 3 pt 0, \
    path.'egoisticHalfLookaheadTop.dat' with linespoints lt 1 dt 4 pt 0, \
    path.'rawSugarscape.dat' with linespoints lt 1 dt 5 pt 0