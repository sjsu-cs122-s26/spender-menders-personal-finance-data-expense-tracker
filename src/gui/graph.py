import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class PlotWidget(FigureCanvas):
  def __init__(self, plot_type='line', parent=None):
    self.figure = Figure(figsize=(6, 7), dpi=100)
    self.axes = self.figure.add_subplot(111)
    super().__init__(self.figure)
    self.setParent(parent)

    self.plot_type = plot_type
    self.title = None
    self.xlabel = None
    self.ylabel = None

    self.x = []
    self.y = []
    self.labels = []

    self.line = None
    self.bar_container = None
    self._set_style()

  def set_data(self, x, y):
    if self.plot_type == "line" or "bar":
      self.x = x
      self.y = y
    
    elif self.plot_type == "pie":
      self.labels = x
      self.y = y

  def set_labels(self, title, xlabel, ylabel):
    self.title = title
    self.xlabel = xlabel
    self.ylabel = ylabel

    self.axes.set_title(title)
    self.axes.set_xlabel(xlabel)
    self.axes.set_ylabel(ylabel)
    self.axes.tick_params(axis='x', rotation=45)

  def init_plot(self):
    self._draw()
    # self.axes.clear()
    # self._restore_labels()
    # self._set_style()

    # if self.plot_type == "line":
    #   (self.line,) = self.axes.plot(self.x, self.y)

    # elif self.plot_type == "bar":
    #   self.bar_container = self.axes.bar(self.x, self.y)

    # elif self.plot_type == "pie":
    #   self.axes.pie(self.y, 
    #                 labels=self.labels, 
    #                 autopct="%1.1f%%", 
    #                 startangle=90, 
    #                 wedgeprops={"edgecolor": "white"})
    #   self.axes.axis("equal")

    # self.draw_idle()

  def update_plot(self, x, y):
    if x is not None and y is not None:
      self.x = x
      self.y = y

    self._draw()

    # if self.plot_type == "line":
    #   self.line.set_data(self.x, self.y)

    #   self.axes.relim()
    #   self.axes.autoscale_view()

    # elif self.plot_type == "bar":
    #   self.axes.clear()
    #   self.ax.bar(self.x, self.y)

    #   self._restore_labels()

    # self.draw_idle()

  def _draw(self):
    self.axes.clear()
    self._set_style()

    if self.plot_type == "line":
      self.axes.plot(self.x, self.y)
      self._restore_labels()

    elif self.plot_type == "bar":
      self.axes.bar(self.x, self.y)
      self._restore_labels()

    elif self.plot_type == "pie":
      self.axes.pie(self.y, 
                    labels=self.labels, 
                    autopct="%1.1f%%", 
                    startangle=90, 
                    wedgeprops={"edgecolor": "white"})
      self.axes.axis("equal")

    # self.figure.tight_layout(pad=0, w_pad=0, h_pad=0)
    self.figure.tight_layout()
    self.figure.subplots_adjust(top=0.85, bottom=0.30)
    self.draw_idle()
    

  def _restore_labels(self):
    if self.title:
      self.axes.set_title(self.title)
    if self.xlabel:
      self.axes.set_xlabel(self.xlabel)
      self.axes.tick_params(axis='x', rotation=45)
    if self.ylabel:
      self.axes.set_ylabel(self.ylabel)

  def _set_style(self):
    self.figure.patch.set_facecolor('#171717')  

    self.axes.set_facecolor('#1c1c1c')  
    self.axes.tick_params(axis='both', colors='#E6E6E6')  

    self.axes.xaxis.label.set_color('#E6E6E6') 
    self.axes.yaxis.label.set_color('#E6E6E6')  

    self.axes.spines['top'].set_color('#E6E6E6')
    self.axes.spines['right'].set_color('#E6E6E6')
    self.axes.spines['left'].set_color('#E6E6E6')
    self.axes.spines['bottom'].set_color('#E6E6E6')

    self.axes.title.set_color('#E6E6E6')
    self.axes.title.set_fontsize(14)
    self.axes.title.set_fontweight(50)