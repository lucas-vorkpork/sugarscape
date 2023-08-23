set title "Starvation Deaths"
set xlabel "Timestep"
set ylabel "Number of Starvation Deaths"
set lt 1 lw 2 lc "black"
set yrange [0:130]
set xtics nomirror
set ytics nomirror
set term pdf
set output "starvationDeaths.pdf"
path =ARGV[1].'/starvationDeaths/'
plot path.'benthamHalfLookaheadBinary.dat' with linespoints pointinterval 100 pointsize 1 lt 1 dt 1 pt 0 title 'benthamHalfLookaheadBinary', \
    path.'benthamHalfLookaheadTop.dat' with linespoints pointinterval 100 pointsize 1.5 lt 1 dt 1 pt 1 title 'benthamHalfLookaheadTop', \
    path.'benthamNoLookaheadTop.dat' with linespoints pointinterval 100 pointsize 1 lt 1 dt 1 pt 2 title 'benthamNoLookaheadTop', \
    path.'egoisticHalfLookaheadTop.dat' with linespoints pointinterval 100 pointsize 1.33 lt 1 dt 1 pt 3 title 'egoisticHalfLookaheadTop', \
    path.'rawSugarscape.dat' with linespoints pointinterval 100 pointsize 1 lt 1 dt 1 pt 4 title 'rawSugarscape'