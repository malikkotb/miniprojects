let weather = {
    apikey: '93fc912fa2536df9e826971a36e1bab1',

    fetchWeather: function(city) {
        fetch(
            'https://api.openweathermap.org/data/2.5/weather?q=' 
            + city + '&units=metric&appid=' + this.apikey,
        ).then((response) => {
            if (!response.ok) {
              alert("No weather found.");
              throw new Error("No weather found.");
            }
            return response.json();
          })
          .then((data) => this.displayWeather(data));

    },

    displayWeather: function(data) {
        // destructuring assignment: const {}
        const { name } = data;
        const { icon, description } = data.weather[0];
        const { temp, humidity } = data.main;
        const { speed } = data.wind; 
        // gleiche wie: speed = data["wind"]["speed"]

        console.log(name, icon, description, temp, humidity, speed)
        document.querySelector(".city").innerText = "Weather in " + name;
        document.querySelector(".icon").src = "https://openweathermap.org/img/wn/" + icon + ".png";
        document.querySelector(".description").innerText = description;
        document.querySelector(".temp").innerText = temp + "°C";
        document.querySelector(".humidity").innerText = "Humidity: " + humidity + "%";
        document.querySelector(".wind").innerText = "Wind spped: " + speed + "km/h";
        document.body.style.backgroundImage = "url('https://source.unsplash.com/1600x900/?" + name + "')"
    },

    search: function () {
        this.fetchWeather(document.querySelector(".search-bar").value);
      }, 
};

document.querySelector(".search button").addEventListener("click", function () {
    weather.search();
  });

document
  .querySelector(".search-bar")
  .addEventListener("keyup", function (event) {
    if (event.key == "Enter") {
      weather.search();
    }
  });


weather.fetchWeather("Munich");
