set title "Normalized Agent Wealth"
set xlabel "Timestep"
set ylabel "Agent Wealth / Enviroment Wealth"
set lt 1 lw 2 lc "black"
set yrange [0:140]
set xtics nomirror
set ytics nomirror
set term pdf
set output "totalWealth.pdf"
path =ARGV[1].'/totalWealth/'
plot path.'benthamHalfLookaheadBinary.dat' with linespoints lt 1 dt 1 pt 0 title 'benthamHalfLookaheadBinary', \
    path.'benthamHalfLookaheadTop.dat' with linespoints lt 1 dt 2 pt 0 title 'benthamHalfLookaheadTop', \
    path.'benthamNoLookaheadTop.dat' with linespoints lt 1 dt 3 pt 0 title 'benthamNoLookaheadTop', \
    path.'egoisticHalfLookaheadTop.dat' with linespoints lt 1 dt 4 pt 0 title 'egoisticHalfLookaheadTop', \
    path.'rawSugarscape.dat' with linespoints lt 1 dt 5 pt 0 title 'rawSugarscape'