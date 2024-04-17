from abc import ABC, abstractmethod

class WeatherData():
    def __init__(self, temperature = None, humidity = None, pressure = None, measurementchanged = None) -> None:
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = pressure
        self.__measurementsChanged = measurementchanged

    @property
    def temperature(self):
        return self.__temperature
    
    @temperature.setter
    def temperature(self, value):
        self.__temperature = value
        self.__measurementsChanged()

    @property
    def humidity(self):
        return self.__humidity
    
    @humidity.setter
    def humidity(self, value):
        self.__humidity = value
        self.__measurementsChanged()

    @property
    def pressure(self):
        return self.__pressure
    
    @pressure.setter
    def pressure(self, value):
        self.__pressure = value
        self.__measurementsChanged()

    @property
    def measurementsChanged(self):
        return self.__measurementsChanged
    
    @measurementsChanged.setter
    def measurementsChanged(self, value):
        self.__measurementsChanged = value

class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass

class CurrentConditionsDisplay(DisplayElement):
    def __init__(self, weatherData, temperature = None, humidity = None, pressure = None ) -> None:
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = pressure
        self.__weatherData = weatherData
        self.__weatherData.measurementsChanged = self.update

    def update(self):
        self.__temperature = self.__weatherData.temperature
        self.__humidity = self.__weatherData.humidity
        self.__pressure = self.__weatherData.pressure
    
    def display(self):
        print(f"Current conditions: {self.__temperature}C° degrees and {self.__humidity}% humidity and {self.__pressure} pascal")

if __name__ == '__main__':
    weatherData = WeatherData()
    currentDisplay = CurrentConditionsDisplay(weatherData)
    currentDisplay.display()
    weatherData.temperature = 80
    weatherData.humidity = 65
    weatherData.pressure = 30.4
    currentDisplay.display()


