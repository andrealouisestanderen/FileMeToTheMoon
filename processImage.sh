#!/bin/bash
cd ./static
mpiexec -np 7 -hosts mpi-manager,sheep-1,sheep-2,sheep-3,sheep-4,sheep-5,sheep-6 ./make_blurry_mpi $1 $2
