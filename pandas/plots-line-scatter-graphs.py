# Shows line graphs…
# From matplotlib import pyplot as plt… matplotlib is module, pyplot is a submodule, plt is alias
# Plt.plot( xaxis_values, yaxis_values)… Dosen't show the graph as we might add new lines etc
# Plot.show()… displays the graph
# Matplotlib gives two different colors to different lines by default

# Add legends, title, axis labels…
# Plt.xlabel("")… adds x axis label
# Plt.ylabel("")… adds y axis label
# Plt.title("")… adds title to the graph
# Plt.plot(x_values, y_values, label="something")… used to plot legend
# Plt.legend()…. Just like show displays the legend…
# Plt.text(x_coordinate, y_coordinate, "message")… adds notes to a specific coordinate on a graph
# Plt.title("plot title", fontsize=20)
# Plt.legend(color='green')… For list of allowed colors look up webcolors on wikipedia

# Adding style to the plots…
# Plt.plot(x, y, color="some color")…. Adds color to a line 
# Plt.plot(x, y, linewidth=1)…. Modifies the line width… 1, 2, 3, 4… greater no wider the line
# Plt.plot(x, y, linestyle="-")… modifies the lines… - for simple, -- for dashed line, -. For dash dot, : for dotted
# Plt.plot(x, y, markers="x")… modifies the markers… x, s, o, d, *, h… markers the lines itself
# Plt.style.use('fivethirtyeight')… changes the theme of the graph…  ggplot, seaborn, default
# Plt.style.available…. Lists all the available styles


# Scatter Plot…
# Line plots helps visualize ordered date points
# Scatter plots help visualize unordered date points
# Plt.scatter(x, y)… plots scatter graph
# Plt.xlabel(""), plt.ylabel(""), plt.show()…. Xlabel, ylabel and show
# Plt.scatter(x, y, alpha=0.1)… Scatter plots can have layers, aplha makes the points transparent, smaller alpha parameter the more transparent point… now the darker areas contains more points and the lighter ones lesser…


