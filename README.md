# F2Depine
La mejor catedra

## Para instalarlo corran en la consola el siguiente comando:
### pueden probar con pip o pip3
>pip3 install F2Depine

## Para cuando quieran usar funciones de Fourier:

> from F2Depine import fourier;
### Luego usan
>  soga = fourier.CondicionesIniciales(contoro,longitud,v_f, F(x),rango_de_modos)# vean el ejemplo de fourier para 
 
## Para cuando quieran usar funciones de Modos:

> from F2Depine import modos;
### Luego usan
>  modo1 = modos.Modo(1,contoro,longitud,v_f)# vean el ejemplo de Modo
### Esto mismo si quieren combinacion de modos usan
> modos = modos.CombinacionDeModos([1,4,5,7,8],.....) # vean el ejemplo de Combinacion de modos
 

