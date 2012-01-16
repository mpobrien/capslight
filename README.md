##How to build

```bash
python ./setup.py build
cd build
cd lib.macosx-10.7-intel-2.7 # may vary on your system
```

Then:

```python
import led
led.setlight(1)
led.setlight(0)
```
