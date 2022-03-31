"""
Application Detection Latest Earthquake
Modularization with function
Modularization with Package
"""
import earthquakelatest

if __name__ == '__main__':
    print(f'My application using package have description {earthquakelatest.description}')
    result = earthquakelatest.extraction_data()
    earthquakelatest.display_data(result)
