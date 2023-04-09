#/bin/bash
docker run -it --rm -p 8888:8888 -v $(pwd):/home/jovyan/work jupyter/scipy-notebook:2023-02-28
