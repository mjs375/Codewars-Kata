# Raspberry Pi Plotter

- **Plotter**: *devices that print images with a pen (rather than the modern inkjet with its dot-matrix).*
- **Types**:
  - **Hanging Wall Plotter**: *a vertical plotter that uses servo/stepper motors to modulate the length of two strings, both of which connect to a hanging gondola-apparatus in the center. By modulating the length of each, the gondola can brought to any point within the drawing area, and a third servo motor can raise or lower the pen.*


### General Principle
- 1. Paper is taped on a vertical plotter easel (or wall).
- 2. Installed at the top left and right corner of the easel are two motors. 
  - 2b. These motors hold the gondola-belts, and can tighten/loosen to change the location of the gondola (pen-holder). Belts are toothed to prevent slippage and improve accuracy. Counter-weights are hung on the far ends of the belts.
- 3. A gondola, or pen-holder, held between the two belts.
  - 3b. The gondola has its own motor, which simply raises or lowers the pen to the surface of the paper (if toggled off, a non-ink point stabilizes the gondola against the surface).
4. The motors are driven in sync, using mathematical theorems, to guide the gondola either i) where it needs to be next, or ii) where it goes as it draws a line.

### Mathematics
- **Format**: Cartesian Coordinates
  - *i.e. if I want the pen at point(x,y), how long should the L-belt and R-belt be?*
- **Variables**:
  - **```h```**: height of paper
  - **```w```**: width between two motor spindles

### G-CODE
- the numerically-controlled language of 3D printing.
  - a series of commands, most starting with ```G``` (some ```M```). They tell the printer where to move, at what speed, &c., &c. Each code is written on a separate line.
- **G-Code**:
  - ```G28; home all axes (x, y, z)```: home all axes by default (to [0,0,0], or elsewhere by providing X,Y,Z).
    - ```G28 Z ; home z-axis only```
    - ```G28 X Y ; home X/Y-axis```

### Project SPIDERWEB
- a hanging pen plotter



### Sources
- [Maths (J. Proudlock)](https://hackspace.raspberrypi.org/articles/use-pythagoras-theorem-to-draw-pictures)
- [erik](https://github.com/yosemitebandit/erik)
- [Brachiograph](https://github.com/evildmp/BrachioGraph)
- [polargraph](http://www.polargraph.co.uk/)
- [inkylinesplots](https://linktr.ee/inkylinesplots)
- [Pen plotter](https://www.basjacobs.com/post/pen-plotter/)
- [Travelling Salesman Tutorial/Code](https://towardsdatascience.com/solving-travelling-salesperson-problems-with-python-5de7e883d847)
- [Optimizing TSP: Code!](https://nb.paulbutler.org/optimizing-plots-with-tsp-solver/)
