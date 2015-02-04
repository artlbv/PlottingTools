# PlottingTools
Plotting tools mainly for ROOT histograms

* ***PlotStack.py*** -- acts like hadd: collects same histograms from different files and plots (stacks) them depending on signal/background definition.

  Usage: `./PlotStack.py FileDir [Pattern]`
  
  Example: `./PlotStack.py submit CMG_MC`
  
* ***DumpPlots.py*** -- dumps the plots (including directory structure) into a given directory 

  Usage: `./DumpPlots.py PlotFile [OutDir]`
  
  Example: `./DumpPlots.py StackPlots.root Plots`
