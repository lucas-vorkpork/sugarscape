set title "Normalized Agent Wealth Collected"
set xlabel "Timestep"
set ylabel "Agent Wealth Collected / Enviroment Wealth Created"
set lt 1 lw 2 lc "black"
set term pdf
set output ARGV[1]
plot ARGV[2] with linespoints lt 1 dt 1 pt 0