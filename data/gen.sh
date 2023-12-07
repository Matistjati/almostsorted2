#!/bin/bash
. ../testdata_tools/gen.sh

use_solution quadratic.cpp

compile gen_yes.py
compile gen_rand.py



group group2 20
for i in {1..1000}
do
tc g2-$i gen_rand
tc g1-$i gen_yes

done