# Dependencies and reproduction environment

Python 3.10 virtual environment. Direct versions: numpy 2.2.6 (BSD), scipy 1.15.3 (BSD), matplotlib
3.10.6 (Matplotlib/PSF-based license), Pillow 11.3.0 (MIT-CMU). Full resolved versions are pinned in
requirements-lock.txt. These published packages are installed through pip; source is not vendored.
Review package metadata/license files for redistribution obligations; build output is not a license grant.

Icarus Verilog 12.0 development build is the independent open-source simulator (GPL tool, not bundled).
Vivado 2025.2 / XSim is the authoritative installed proprietary tool; not redistributed.
The installed dependency set passes `pip check`; compatibility and actual model tests are verified locally.
No live vulnerability-feed audit or certification of all transitive dependencies is claimed.

The project does not use external AI APIs, telemetry, paid services or a deployment target. GitHub is
the user-selected existing public repository. Board originals remain excluded from public Git.
