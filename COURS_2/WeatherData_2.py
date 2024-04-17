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


class DsplayTemperature(DisplayElement):
    def __init__(self, weatherData, temperature = None) -> None:
        self.__temperature = temperature
        self.__weatherData = weatherData
        self.__weatherData.measurementsChanged = self.update

    def update(self):
        self.__temperature = self.__weatherData.temperature
    
    def display(self):
        print(f"Current temperature: {self.__temperature}C° degrees")

class DisplayHumidity(DisplayElement):
    def __init__(self, weatherData, humidity = None) -> None:
        self.__humidity = humidity
        self.__weatherData = weatherData
        self.__weatherData.measurementsChanged = self.update

    def update(self):
        self.__humidity = self.__weatherData.humidity
    
    def display(self):
        print(f"Current humidity: {self.__humidity}%")

class DisplayPressure(DisplayElement):
    def __init__(self, weatherData, pressure = None) -> None:
        self.__pressure = pressure
        self.__weatherData = weatherData
        self.__weatherData.measurementsChanged = self.update

    def update(self):
        self.__pressure = self.__weatherData.pressure
    
    def display(self):
        print(f"Current pressure: {self.__pressure} pascal")

if __name__ == '__main__':
    weatherData = WeatherData()
    currentTemperature = DsplayTemperature(weatherData)
    currentHumidity = DisplayHumidity(weatherData)
    currentPressure = DisplayPressure(weatherData)
    weatherData.temperature = 25
    weatherData.humidity = 65
    weatherData.pressure = 1013
    currentTemperature.display()
    currentHumidity.display()
    currentPressure.display()


