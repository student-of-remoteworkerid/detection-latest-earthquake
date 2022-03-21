"""
Application Detection Latest Earthquake
"""
import earthquakelatest

if __name__ == '__main__':
    print('My application')
    result = earthquakelatest.extraction_data()
    earthquakelatest.display_data(result)
