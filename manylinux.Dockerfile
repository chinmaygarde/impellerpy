FROM quay.io/pypa/manylinux2014_aarch64

RUN yum install -y cmake libX11-devel libXrandr-devel libXinerama-devel libXi-devel libXcursor-devel mesa-libGL-devel libXdamage-devel libudev-devel wayland-devel libxkbcommon-devel
