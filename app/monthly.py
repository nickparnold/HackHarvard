import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
import datetime


def makeGraph(username, etc):
    # Add data
    now = datetime.datetime.now()
    days = [1]
    
    if now.month == "January" or now.month == "March" or now.month == "May" or now.month == "July" or now.month == "August" or now.month == "October" or now.month == "December":
        days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31] 
        
    elif now.month == "April" or now.month == "June" or now.month == "September" or now.month == "November":
        days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        
    elif (now.year % 4) == 0:
       days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
    
        
    else:
        days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    
        
    # Create and style traces
    points = go.Scatter(
        x = days,
        y = etc,
        name = 'Bill',
        line = dict(
            color = ('rgb(0, 153, 0)'),
            width = 4)
    )
    
    data = [points]
    # Edit the layout
    layout = dict(title = 'Daily Electric Estimates',
                  xaxis = dict(title = 'Days'),
                  yaxis = dict(title = 'Estimated Money Spent'),
                  )

    # Plot and embed in ipython notebook!
    fn = username+"/"+str(now.month)
    plot_url = py.plot(data, filename=fn, auto_open=False)
    return tls.get_embed(plot_url)


bills = [32.5, 37.6, 49.9, 53.0, 69.1, 75.4, 76.5, 76.6, 70.7, 60.6, 45.1, 29.3]

print (makeGraph("yello", bills))