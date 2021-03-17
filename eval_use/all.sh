#!/bin/bash

gnuplot $1.gp
epstopdf $1.eps

#gnuplot cpuh.gp
#epstopdf cpuh.eps
#cp ./cpuh.pdf ../FIGS/cpuh.pdf
#
#gnuplot cpu.gp
#epstopdf cpu.eps
#cp ./cpu.pdf ../FIGS/cpu.pdf
