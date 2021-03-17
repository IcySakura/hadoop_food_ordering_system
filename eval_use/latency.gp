set terminal postscript eps enhanced font 'Times-Roman,' #size 10cm,6.5cm
set output 'latency.eps'

set size ratio 0.62 # golden ratio 0.62

set boxwidth 0.4 absolute
# set style fill pattern 0 border
set style data histograms
set style histogram rowstacked
set offset -0.7,-0.7,0,0
set auto x

set ylabel font "Times-New-Roman, 35" "Execution Time (Sec.)" offset -1

set xtics font ", 20" offset 0.0,-1 #graph -1 nomirror
set ytics font ", 35" offset 0.5,graph 0 nomirror

set yrange [0:0.5] noreverse nowriteback

set key right top font ",45" spacing 5 width 1 #samplen 5 # rmargin
# set key invert reverse Left outside
set key autotitle columnheader

set lmargin 10
set bmargin 4

set bars 1.5

set style fill solid border -1

plot 'latency.dat' using (column(2)):xtic(1) lc rgb "#264E86" lt -1, \
    '' using 0:(column(2)):3 with errorbars notitle lw 2 lt -1



