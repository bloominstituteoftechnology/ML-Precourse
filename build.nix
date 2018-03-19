with import <nixpkgs> {};

python.withPackages (ps: with ps; [ numpy toolz ])

