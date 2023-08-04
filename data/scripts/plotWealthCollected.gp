set title "Normalized Agent Wealth Collected"
set xlabel "Timestep"
set ylabel "Agent Wealth Collected / Enviroment Wealth Created"
set lt 1 lw 2 lc "black"
set yrange [0:30]
set xtics nomirror
set ytics nomirror
set term pdf
set output "wealthCollected.pdf"
path =ARGV[1].'/wealthCollected/'
plot path.'benthamHalfLookaheadBinary.dat' with linespoints pointinterval 100 pointsize 0.75 lt 1 dt 1 pt 0 title 'benthamHalfLookaheadBinary', \
    path.'benthamHalfLookaheadTop.dat' with linespoints pointinterval 100 pointsize 0.75 lt 1 dt 2 pt 1 title 'benthamHalfLookaheadTop', \
    path.'benthamNoLookaheadTop.dat' with linespoints pointinterval 100 pointsize 0.75 lt 1 dt 3 pt 2 title 'benthamNoLookaheadTop', \
    path.'egoisticHalfLookaheadTop.dat' with linespoints pointinterval 100 pointsize 0.75 lt 1 dt 4 pt 3 title 'egoisticHalfLookaheadTop', \
    path.'rawSugarscape.dat' with linespoints pointinterval 100 pointsize 0.75 lt 1 dt 5 pt 4 title 'rawSugarscape'