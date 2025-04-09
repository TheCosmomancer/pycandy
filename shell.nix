let
  nixpkgs = fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-24.05";
  pkgs = import nixpkgs { config = {}; overlays = []; };
in

pkgs.mkShellNoCC {
  packages = with pkgs; [
    python312Full
    python312Packages.pygame
    python312Packages.pygame-gui
    python312Packages.pygame-sdl2
    python312Packages.pygame-ce
    python312Packages.pyrect
  ];
}