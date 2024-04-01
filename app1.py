from flask import Flask,request,render_template
from flask_cors import cross_origin
import pickle
import pandas as pd

model = pickle.load(open('flight_rf.pkl','rb'))

app = Flask(__name__)

@app.route('/')
@cross_origin()
def home():
	return render_template('home.html')

@app.route('/predict',methods=['GET','POST'])
@cross_origin()
def predict():
    if request.method=='POST':
        departure_time = request.form['departure_time']
        
        Journey_day = pd.to_datetime(departure_time,format="%Y-%m-%dT%H:%M").day
        Journey_month = pd.to_datetime(departure_time,format="%Y-%m-%dT%H:%M").month

        Departure_hour = pd.to_datetime(departure_time,format="%Y-%m-%dT%H:%M").hour
        Departure_min = pd.to_datetime(departure_time,format="%Y-%m-%dT%H:%M").minute

        arrival_time = request.form['arrival_time']
        Arrival_hour =  pd.to_datetime(arrival_time,format="%Y-%m-%dT%H:%M").hour
        Arrival_min =  pd.to_datetime(arrival_time,format="%Y-%m-%dT%H:%M").minute

        no_of_stops = int(request.form['stops'])

        duration_days = abs(arrival_time-departure_time)
        duration_hours = abs(arrival_time-departure_time)
        duration_mins = abs(arrival_time-departure_time)

        airline=request.form['airline']
        if(airline=='Vistara'):
            Vistara = 1
            Air_India = 0
            SpiceJet = 0
            GO_FIRST = 0
            Indigo = 0
            AirAsia = 0

        elif (airline=='Air_India'):
            Vistara = 0
            Air_India = 1
            SpiceJet = 0
            GO_FIRST = 0
            Indigo = 0
            AirAsia = 0

        elif (airline=='SpiceJet'):
            Vistara = 0
            Air_India = 0
            SpiceJet = 1
            GO_FIRST = 0
            Indigo = 0
            AirAsia = 0

        elif (airline=='GO_FIRST'):
            Vistara = 0
            Air_India = 0
            SpiceJet = 0
            GO_FIRST = 1
            Indigo = 0
            AirAsia = 0

        elif (airline=='Indigo'):
            Vistara = 0
            Air_India = 0
            SpiceJet = 0
            GO_FIRST = 0
            Indigo = 1
            AirAsia = 0
            
        elif (airline=='AirAsia'):
            Vistara = 0
            Air_India = 0
            SpiceJet = 0
            GO_FIRST = 0
            Indigo = 0
            AirAsia = 1

        else:
            Vistara = 0
            Air_India = 0
            SpiceJet = 0
            GO_FIRST = 0
            Indigo = 0
            AirAsia = 0
            
        
        source = request.form["source_city"]
        if (source_city == 'Delhi'):
            source_city_Delhi = 1
            source_city_Kolkata = 0
            source_city_Mumbai = 0
            source_city_Chennai = 0
            source_city_Bangalore = 0
            source_city_Hyderabad = 0

        elif (source_city == 'Kolkata'):
            source_city_Delhi = 0
            source_city_Kolkata = 1
            source_city_Mumbai = 0
            source_city_Chennai = 0
            source_city_Bangalore = 0
            source_city_Hyderabad = 0

        elif (source_city == 'Mumbai'):
            source_city_Delhi = 0
            source_city_Kolkata = 0
            source_city_Mumbai = 1
            source_city_Chennai = 0
            source_city_Bangalore = 0
            source_city_Hyderabad = 0

        elif (source_city == 'Chennai'):
            source_city_Delhi = 0
            source_city_Kolkata = 0
            source_city_Mumbai = 0
            source_city_Chennai = 1
            source_city_Bangalore = 0
            source_city_Hyderabad = 0

        elif (source_city == 'Bangalore'):
            source_city_Delhi = 0
            source_city_Kolkata = 0
            source_city_Mumbai = 0
            source_city_Chennai = 0
            source_city_Bangalore = 1
            source_city_Hyderabad = 0

        elif (source_city == 'Hyderabad'):
            source_city_Delhi = 0
            source_city_Kolkata = 0
            source_city_Mumbai = 0
            source_city_Chennai = 0
            source_city_Bangalore = 0
            source_city_Hyderabad = 1

        else:
            source_city_Delhi = 0
            source_city_Kolkata = 0
            source_city_Mumbai = 0
            source_city_Chennai = 0
            source_city_Bangalore = 0
            source_city_Hyderabad = 0


        destination = request.form["destination_city"]
        if (destination_city == 'Delhi'):
            destination_city_Delhi = 1
            destination_city_Kolkata = 0
            destination_city_Mumbai = 0
            destination_city_Chennai = 0
            destination_city_Bangalore = 0
            destination_city_Hyderabad = 0
        
        elif (destination_city == 'Kolkata'):
            destination_city_Delhi = 0
            destination_city_Kolkata = 1
            destination_city_Mumbai = 0
            destination_city_Chennai = 0
            destination_city_Bangalore = 0
            destination_city_Hyderabad = 0

        elif (destination_city == 'Mumbai'):
            destination_city_Delhi = 0
            destination_city_Kolkata = 0
            destination_city_Mumbai = 1
            destination_city_Chennai = 0
            destination_city_Bangalore = 0
            destination_city_Hyderabad = 0

        elif (destination_city == 'Chennai'):
            destination_city_Delhi = 0
            destination_city_Kolkata = 0
            destination_city_Mumbai = 0
            destination_city_Chennai = 1
            destination_city_Bangalore = 0
            destination_city_Hyderabad = 0

        elif (destination_city == 'Hyderabad'):
            destination_city_Delhi = 0
            destination_city_Kolkata = 0
            destination_city_Mumbai = 0
            destination_city_Chennai = 0
            destination_city_Bangalore = 0
            destination_city_Hyderabad = 1

        else:#Banglore
            destination_city_Delhi = 0
            destination_city_Kolkata = 0
            destination_city_Mumbai = 0
            destination_city_Chennai = 0
            destination_city_Bangalore = 0
            destination_city_Hyderabad = 0

        output = model.predict([[days_left, 
                                 price,
                                 duration_days', 
                                 duration_hours',
                                 duration_mins,
                                 no_of_stops, 
                                 airline_AirAsia, 
                                 airline_Air_India,
                                 airline_GO_FIRST, 
                                 airline_Indigo, 
                                 airline_SpiceJet,
                                 airline_Vistara, 
                                 source_city_Bangalore,
                                 source_city_Chennai,
                                 source_city_Delhi,
                                 source_city_Hyderabad,
                                 source_city_Kolkata,
                                 source_city_Mumbai,
                                 destination_city_Chennai,
                                 destination_city_Delhi, 
                                 destination_city_Hyderabad,
                                 destination_city_Kolkata, 
                                 destination_city_Mumbai,
                                 arrival_time_Early_Morning,
                                 arrival_time_Evening,
                                 arrival_time_Late_Night,
                                 arrival_time_Morning,
                                 arrival_time_Night,
                                 departure_time_Early_Morning, 
                                 departure_time_Evening,
                                 departure_time_Late_Night,
                                 departure_time_Morning,
                                 departure_time_Night,
                                 class_Economy]])

        output = round(output[0],2)
        return render_template('home.html',predictions='You will have to Pay approx Rs. {}'.format(output))


if __name__ == '__main__':
	app.run(debug=True)