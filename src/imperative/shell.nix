# https://github.com/NixOS/nixpkgs/issues/71178
{ nixpkgs ? import (fetchTarball https://github.com/NixOS/nixpkgs/archive/refs/tags/24.05.tar.gz) {}
}:

with nixpkgs;

stdenv.mkDerivation rec {
  name = "module dependencies";
  env = buildEnv { name = name; paths = buildInputs; };
  buildInputs = [
    python3
    python3Packages.black
    python3Packages.pytest
    pyright
  ];
}
