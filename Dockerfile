FROM ubuntu:latest

RUN apt update
RUN apt install -y        \
      autoconf            \
      autoconf-archive    \
      automake            \
      build-essential     \
      cmake               \
      curl                \
      git                 \
      libgl-dev           \
      libwayland-dev      \
      libx11-dev          \
      libxcursor-dev      \
      libxi-dev           \
      libxinerama-dev     \
      libxkbcommon-dev    \
      libxrandr-dev       \
      ninja-build         \
      pkg-config          \
      wget                \
      zip

RUN git clone https://github.com/microsoft/vcpkg /vcpkg
ENV VCPKG_ROOT=/vcpkg
RUN /vcpkg/bootstrap-vcpkg.sh
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
