$ErrorActionPreference = "Stop"

python tests/validate_skill.py
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

python tests/eval_dataset.py
exit $LASTEXITCODE
