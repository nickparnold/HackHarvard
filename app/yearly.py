import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls

def makeGraph(username, bills):
    # Add data
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Create and style traces
    points = go.Scatter(
        x = month,
        y = bills,
        name = 'Bill',
        line = dict(
            color = ('rgb(0, 153, 0)'),
            width = 4)
    )
    
    data = [points]
    # Edit the layout
    layout = dict(title = 'Yearly Electric Bills',
                  xaxis = dict(title = 'Month'),
                  yaxis = dict(title = 'Money Spent'),
                  )

    # Plot and embed in ipython notebook!
    fn = username+"/year"
    plot_url = py.plot(data, filename=fn, auto_open=False)
    return tls.get_embed(plot_url)


bills = [32.5, 37.6, 49.9, 53.0, 69.1, 75.4, 76.5, 76.6, 70.7, 60.6, 45.1, 29.3]

print (makeGraph("yello", bills))