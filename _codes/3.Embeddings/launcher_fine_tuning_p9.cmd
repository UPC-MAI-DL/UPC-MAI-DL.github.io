#!/bin/bash

#SBATCH --job-name="fine_tuning"
#SBATCH -D .
#SBATCH --output=fine_tuning_%j.out
#SBATCH --error=fine_tuning_%j.err
#SBATCH --ntasks=40
#SBATCH --gres=gpu:1
#SBATCH --time=00:10:00

module purge; module load gcc/6.4.0 cuda/9.1 cudnn/7.1.3 openmpi/3.0.0 atlas/3.10.3 scalapack/2.0.2 fftw/3.3.7 szip/2.1.1 ffmpeg/4.0.2 opencv/3.4.1 python/3.6.5_ML

python fine_tuning.py
