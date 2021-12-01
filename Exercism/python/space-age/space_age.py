class SpaceAge:
    def __init__(self, seconds):
        self.earth_years = seconds / 31557600

    def on_earth(self):
        return round(self.earth_years, 2)

    def on_mercury(self):
        years = self.earth_years / 0.2408467
        return round(years, 2)

    def on_venus(self):
        years = self.earth_years / 0.6151972
        return round(years, 2)

    def on_mars(self):
        years = self.earth_years / 1.8808158
        return round(years, 2)

    def on_jupiter(self):
        years = self.earth_years / 11.862615
        return round(years, 2)

    def on_saturn(self):
        years = self.earth_years / 29.447498
        return round(years, 2)

    def on_uranus(self):
        years = self.earth_years / 84.016846
        return round(years, 2)

    def on_neptune(self):
        years = self.earth_years / 164.79132
        return round(years, 2)
