#!/bin/bash
cd ./static
mpiexec -np 2 -hosts mpi-manager,sheep-1,sheep-2 ./make_blurry_mpi $1 $2
