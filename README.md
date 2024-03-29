# Rope Simulation
F2Depine is a Python library created for calculating oscillation modes of ropes based on their tension, length, and other parameters. This library enables users to perform Fourier analysis and visualize animations based on the initial position of the ropes.


## Installation
To install, run the following command in your console. You can use either pip or pip3:
```bash
pip3 install F2Depine
```

## Usage: Fourier Functions
If you wish to use Fourier functions, import the following from F2Depine:
```python
from F2Depine import soga
```

Then, you can use the following syntax:
```python
soga = soga.CondicionesIniciales(contour, length, v_f, F(x), modes_range)# See the Fourier example for details
```

## Usage: Modes Functions
If you want to use mode functions, import the following from F2Depine:
```python
from F2Depine import soga
```

Then, you can use the following syntax:
```python
mode1 = soga.Modo(1, contour, length, v_f)# See the Mode example for details
```

For combination of modes, you can use:
```python
modes = soga.CombinacionDeModos([1, 4, 5, 7, 8],.....) # See the Combination of Modes example for details
```
