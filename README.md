```shell
git clone ...
cd acme-employee-payment
python -m venv .venv
source .venv/bin/activate
pip install .
employee-payment tests/sample.txt

# cleanup
deactivate
rm -rf .venv
```
