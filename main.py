"""
Application Detection Latest Earthquake
Modularization with function
Modularization with Package
"""
import earthquakelatest

if __name__ == '__main__':
    earthquake_in_indonesian = earthquakelatest.LatestEarthquake('https://bmkg.go.id')
    print(f'My application using package have description {earthquake_in_indonesian.description}')
    earthquake_in_indonesian.display_description()
    earthquake_in_indonesian.run()
