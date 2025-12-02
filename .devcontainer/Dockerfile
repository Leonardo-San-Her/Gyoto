# Imagen base para Codespaces (Ubuntu con utilidades de desarrollo)
FROM mcr.microsoft.com/devcontainers/base:ubuntu-24.04

# Evitar prompts interactivos en apt
ENV DEBIAN_FRONTEND=noninteractive

# Paquetes necesarios para compilar Gyoto + plugin de Python
RUN apt-get update && \
    apt-get install -y \
      build-essential \
      g++ \
      gfortran \
      autoconf \
      automake \
      libtool \
      pkg-config \
      git \
      libboost-all-dev \
      libeigen3-dev \
      libcfitsio-dev \
      libudunits2-dev \
      libxerces-c-dev \
      swig3.0 \
      doxygen \
      graphviz \
      python3 \
      python3-dev \
      python3-pip \
      python3-numpy \
      python3-matplotlib \
      python3-astropy \
      && rm -rf /var/lib/apt/lists/*

# Hack de compatibilidad: Gyoto busca aclocal-1.18 / automake-1.18
# pero en Ubuntu solo tenemos "aclocal" y "automake".
RUN ln -s /usr/bin/aclocal /usr/bin/aclocal-1.18 || true && \
    ln -s /usr/bin/automake /usr/bin/automake-1.18 || true

# No compilamos Gyoto aquí como root; lo haremos en postCreateCommand
# como el usuario normal del Codespace.
