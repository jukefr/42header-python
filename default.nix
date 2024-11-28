{
  lib,
  python3Packages,
  # fetchFromGitHub,
  # pkgs,
}:

python3Packages.buildPythonPackage rec {
  pname = "header42";
  version = "1.0.0";
  pyproject = true;

  # src = fetchFromGitHub {
  #   owner = "jukefr";
  #   repo = "c_formatter_42";
  #   rev = "db2dfedfd851c0b1d525060de289d3ae6ea33452";
  #   sha256 = "0x92kj32apvcd86yyplzwzrly5ya0snf1q00nvi1c27vdq45aipa";
  # };

  src = ./.;

  build-system = with python3Packages; [
    hatchling
    setuptools
    wheel
  ];

  dependencies = [ ];

  meta = with lib; {
    description = "42 header (rewritten in python and working with stdin/stdout)";
    homepage = "https://github.com/jukefr/header42";
    license = licenses.mit;
    maintainers = with maintainers; [ jukefr ];
  };

}
