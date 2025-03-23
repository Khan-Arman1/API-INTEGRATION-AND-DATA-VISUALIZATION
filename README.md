# API-INTEGRATION-AND-DATA-VISUALIZATION


## DESCRIPTION of Task:
This project implements on visualization of data through graphs, Visualizing the weather for next 7 days. This project use requests library for acessing data through API(data source Openweathermapapi), matplotlib for data visualization, io for data input/output or storing data, base64 for converting matplotlib graph into images, plotly dash is used to create a dashboard. 

Imported necessary libraries like- pandas, matplotlib, requests, base64, io, and dash(for creating dashboard).

_dash.Dash()_ inistillize the object of dash. Then create API key, multiple empty lists for stroing values, created a payload for sending and calling the API, _if response.status_code == 200:_ this check whether the request is sucessfull or not, then stored data into lists.

Now declared a category list of days, define fonts for labelling the axises on graph, _max_Temp_list=[i - 273.15 for i in max_temp_list]_ changed the temperature from Kelvien to Celcius.

_image_convert()_ is a function that converts the graph to image, _io.BytesIO()_ convert the image to bytes input/ouput, _format='png'_ stores the images into '.png' formate.

Created multiple fucntions to convert different graphs to image,
_plot_to_image(x_axis_value,y_axis_value1,y_axis_value2,G_Title,x_label,y_label,label1,label2)_ this method converts a line plot to image. Simillarly other methods were created.

Created a Dashboard layout using _app.layout = html.Div()_ creates a interactive dash board using plotly dash library,
_html.H1("Weather Dashboard", style={'text-align': 'center','color':'green'}),_ creates a heading1 on the dashboard, then a div block adds a block of image to the dashboard for data visuallization.

_if __name__ == '__main__': _ This method checks wheather the current file is executing or not, _app.run_server(debug=True)_ this line of code starts the execution of file by declaring _app.run_server_.


## OUTPUT PICTURE
![Image](https://github.com/user-attachments/assets/64dfe2de-f08f-482d-9ccd-c6d1fdd7a434)
