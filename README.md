# CS 467 Final Project

## Itinerary Visualization

Often, when planning an itinerary a lot of factors such as weather, wait time, and visit duration go unnoticed or not considered by the planner. Even more specifically, the order of visits for locations is almost ignored. Currently Google offers analysis of wait times in the form of a bar graph, however this visualization seems insufficient to plan an itinerary effectively such that they don't have to spend most of their day waiting in lines. Similarly, weather data can be viewed individually (i.e. by a quick google search) but not along with the wait time of a location. For example-  people does not prefer to stand in long queue lines when it’s really hot.

**Goals for this project:**

* Combine Google wait times with the weather forecast to create a tool that allows tourists to develop an almost time-efficient, weather permitting itineraries.

* To visualize waiting time like the length of a queue. For a person using our visualization, even if the queue at the location looks long/or is known to be long in real, it might show as a shorter queue on the visualization if the wait time is short.


## Data Collection

For the purposes of this project, we created our own datasets of place data and weather data for hand-selected cities using the following tools.

* [populartimes](https://github.com/m-wrzr/populartimes) github repo for popular times, wait times, and time spent
* Google Maps APIs for other general place data: [Place Details](https://developers.google.com/maps/documentation/places/web-service/details), [Place Photos](https://developers.google.com/maps/documentation/places/web-service/photos), and [Distance Matrix](https://developers.google.com/maps/documentation/distance-matrix/overview)
* [OpenWeather API](https://openweathermap.org/api) for weather forecasts
* [USA-cities-and-states](https://github.com/grammakov/USA-cities-and-states) github repo for map list options

**See example files in the [`data/` directory](https://github.com/richameher/FinalDesign467/tree/master/data).**

### Replicate Place Data Collection

1. Get a [Google API Key](https://developers.google.com/maps/documentation/places/web-service/get-api-key) and enable Places API. Place it into a `data/.secrets/credentials.json` file in the data/ directory as shown below:
    ```json
    { "api_key": "YOUR_API_KEY" }
    ```

2. Download [populartimes](https://github.com/m-wrzr/populartimes) library

3. Run the collection scripts. Currently, parameters such as filenames are hard-coded.
    ```sh
    $ python3 poptimes_collection.py  # optional: change lat/long coords and out filename
    $ python3 photos_collection.py    # change json_file to match above output
    ```

### Replicate Weather Data Collection

TODO

### Replicate Cities and States Collection

TODO
