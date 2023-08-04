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
plot path.'benthamHalfLookaheadBinary.dat' with linespoints pointinterval 100 pointsize 0.75 lt 1 dt 1 pt 0 title 'benthamHalfLookaheadBinary', \
    path.'benthamHalfLookaheadTop.dat' with linespoints pointinterval 100 pointsize 0.75 lt 1 dt 2 pt 1 title 'benthamHalfLookaheadTop', \
    path.'benthamNoLookaheadTop.dat' with linespoints pointinterval 100 pointsize 0.75 lt 1 dt 3 pt 2 title 'benthamNoLookaheadTop', \
    path.'egoisticHalfLookaheadTop.dat' with linespoints pointinterval 100 pointsize 0.75 lt 1 dt 4 pt 3 title 'egoisticHalfLookaheadTop', \
    path.'rawSugarscape.dat' with linespoints pointinterval 100 pointsize 0.75 lt 1 dt 5 pt 4 title 'rawSugarscape'