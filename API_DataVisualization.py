# importing the required modules
import requests     # allows us to api integration
import matplotlib.pyplot as plt     # allows us to  visualization of the data
import io   # allows us to manage the file-related input and output operations
import base64   # allows us to create the byte object of the input data
import dash     # allows us to create a dash (with image(non interactive) / interactive)
from dash import html       # allows us to create html components

# Initialize the Dash app
app = dash.Dash(__name__)

# creating an API key
API_key = "API_KEY"

# defining variables to store data
max_temp_list = []
min_temp_list = []
humidity_list = []
wind_speed_list = []
wind_gust_speed_list = []
weather_main_list = []
weather_all_clouds_list = []

# defining the URL for the API
url = "https://api.openweathermap.org/data/2.5/forecast"
# creating/defining parameters
payload = {"q": "alwar", 'cnt': 7, "appid": API_key}

# making a request with the payload as a parameter
response = requests.get(url, params=payload)
if response.status_code == 200:     # checks weather the call is successfull
    r = response.json()     # normalize the response data to json
for i in range(len(r['list'])):     # iterate over the response data
        max_temp_list.append(r['list'][i]['main']['temp_max'])
        min_temp_list.append(r['list'][i]['main']['temp_min'])
        humidity_list.append(r['list'][i]['main']['humidity'])
        wind_speed_list.append(r['list'][i]['wind']['speed'])
        wind_gust_speed_list.append(r['list'][i]['wind']['gust'])
        weather_main_list.append(r['list'][i]['weather'][0]['main'])
        weather_all_clouds_list.append(r['list'][i]['clouds']['all'])

# Create categories for the x-axis
categories = ['Day1', 'Day2', 'Day3', 'Day4', 'Day5', 'Day6', 'Day7']
# defining font-family and size
font1 = {'family':'sans-serif','color':'blue','size':20}
font2 = {'family':'sans-serif','color':'darkred','size':15}
# resiging again to for better understanding
max_Temp_list=[i - 273.15 for i in max_temp_list]       # default value is in Kelvin converting Kelvin -> Celcius so substract -273.15
min_Temp_list=[i - 273.15 for i in min_temp_list]       # default value is in Kelvin converting Kelvin -> Celcius so substract -273.15


# Converting image to Graph
def image_convert():
    img = io.BytesIO()  # initiallize the bytesio 
    plt.savefig(img, format='png')  # save the figure(graph) to a file
    img.seek(0)
    img_b64 = base64.b64encode(img.getvalue()).decode('utf-8')  # generate the a byte code of the saved figure(graph)
    return img_b64  # return the byte object

# Function to convert Matplotlib plot to image
def plot_to_image(x_axis_value,y_axis_value1,y_axis_value2,G_Title,x_label,y_label,label1,label2):
    figure,ax = plt.subplots()      # display multiple plots in one window(allows you to organize them)
    ax.plot(x_axis_value, y_axis_value1, color='r', marker="o", label=label1)   # create lineplot for max tempreature
    ax.plot(x_axis_value, y_axis_value2, color='b', marker="x", label=label2)   # create lineplot for min tempreature
    ax.set_xlabel(x_label,fontdict=font2)
    ax.set_ylabel(y_label,fontdict=font2)
    ax.set_title(G_Title,fontdict=font1)
    ax.legend()
    # Convert the plot to an image
    img_b64 = image_convert()       # variable stores the output(byte object) put of the function image_convert()
    plt.close(figure)
    return img_b64

# Function to convert Matplotlib pie to image
def pie_to_image(axis_values,pieLabels,Exploder,G_Title):
    figure, ax = plt.subplots()
    ax.pie(axis_values,labels=pieLabels,explode=Exploder)
    ax.set_title(G_Title,fontdict=font1)
    ax.legend()
    # Convert the pie chart to an image
    img_b64 = image_convert()
    plt.close(figure)
    return img_b64


# Function to convert Matplotlib BarChart to image
def bar_to_image(x_axis_value,y_axis_value1,G_Title,x_label,y_label):
    figure, ax = plt.subplots()
    ax.bar(x_axis_value,y_axis_value1)
    ax.set_xlabel(x_label,fontdict=font2)
    ax.set_ylabel(y_label,fontdict=font2)
    ax.set_title(G_Title,fontdict=font1)
    # Convert the pie chart to an image
    img_b64 = image_convert()
    plt.close(figure)
    return img_b64


# Function to convert Matplotlib BarChart to image
def scatter_to_image(x_axis_value,y_axis_value1,G_Title,x_label,y_label):
    figure, ax = plt.subplots()
    ax.scatter(x_axis_value,y_axis_value1)
    ax.set_xlabel(x_label,fontdict=font2)
    ax.set_ylabel(y_label,fontdict=font2)
    ax.set_title(G_Title,fontdict=font1)
    # Convert the pie chart to an image
    img_b64 = image_convert()
    plt.close(figure)
    return img_b64


# Define the app layout
app.layout = html.Div([
    # heading of the dashboard
    html.H1("Weather Dashboard", style={'text-align': 'center','color':'green'}),

    # Display the temperature plot as an image
    html.Div([
        html.H2("Temperature Visualization"),
        
        # PARAMETERS = x_axis_value, y_axis_value1, y_axis_value2, Graph_Title, x_label, y_label, line_label1, line_label2 
        html.Img(src='data:image/png;base64,' + plot_to_image(categories,max_Temp_list,min_Temp_list,"Temprature Visualization","Days","Temprature (C)",'Max Temp','Min Temp'))     # display the image of to the dash with src and the returned output of the function
    ], style={'text-align': 'center'}),

    # Display the humidity barchart as an image
    html.Div([
        html.H2("Visualizing Humidity"),
        
        # PARAMETERS = x_axis_value, y_axis_value1, Graph_Title, x_label, y_label
        html.Img(src='data:image/png;base64,' + bar_to_image(categories,humidity_list,"Visualizing Humidity","Days","Humidity (%)"))
    ], style={'text-align': 'center'}),

    # Display the pie chart as an image
    html.Div([
        html.H2("Visualizing Weather Cloudiness"),
        
        # PARAMETERS = x-axis_values, pie-parts-Labels, Exploder, Graph_Title
        html.Img(src='data:image/png;base64,' + pie_to_image(weather_all_clouds_list,categories,[0.2,0.7,0,0,0,0,0.1],"Visualizing Wing Speed"))
    ], style={'text-align': 'center'}),

    # Display the ClearSky scatterchart as an image
    html.Div([
        html.H2("Visualizing Humidity"),
        
        # PARAMETERS = x_axis_value, scatter-graph-y_axis_value, Graph_Title, x_label, y_label
        html.Img(src='data:image/png;base64,' + scatter_to_image(categories,weather_main_list,"Weather Description","Days","Sky Clearness"))
    ], style={'text-align': 'center'}),

    # Display the wind speed plot as an image
    html.Div([
        html.H2("Visualizing Wing Speed"),

        # PARAMETERS = x_axis_value, y_axis_value1, y_axis_value2, Graph_Title, x_label, y_label, line_label1, line_label2 
        html.Img(src='data:image/png;base64,' + plot_to_image(categories,wind_speed_list,wind_gust_speed_list,"Visualizing Wing Speed",'Days','Wind Speed m/sec','Wind Speed','Wind Gust'))
    ], style={'text-align': 'center'}),



])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
