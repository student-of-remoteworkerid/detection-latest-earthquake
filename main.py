"""
Application Detection Latest Earthquake
"""
import gempaterkini

if __name__ == '__main__':
    print('My application')
    result = gempaterkini.extraction_data()
    gempaterkini.display_data(result)
