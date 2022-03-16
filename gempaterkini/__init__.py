def extraction_data():
    """
    Date: 16 Maret 2022,
    Time: 11:06:43 WIB
    Magnitudo: 4.2
    Depth: 16 km
    Location: LS=7.90 - BT=107.04
    Epicenter: Pusat gempa berada di laut 109 km Tenggara Kota Sukabumi
    perceived: Dirasakan (Skala MMI): II Singajaya, II Cidaun, II Agrabinta, II Cidora
    :return:
    """
    result = dict()
    result["date"] = "16 Maret 2022"
    result["time"] = "11:06:43 WIB"
    result["magnitude"] = "4.2"
    result["depth"] = "16 km"
    result["location"] = {"ls": 7.90, "bt": 1074.04}
    result["epicenter"] = "Pusat gempa berada di laut 109 km Tenggara Kota Sukabumi"
    result["perceived"] = "Dirasakan (Skala MMI): II Singajaya, II Cidaun, II Agrabinta, II Cidora"

    return result


def display_data(result):
    print("Last Earthquake base on BMKG")
    print(f"Date: {result['date']}")
    print(f"Time: {result['time']}")
    print(f"Magnitude: {result['magnitude']}")
    print(f"depth: {result['depth']}")
    print(f"Location: LS ={result['location']['ls']}, BT={result['location']['bt']}")
    print(f"Epicenter: {result['epicenter']}")
    print(f"Perceived: {result['perceived']}")

"""
if __name__ == '__main__' :
    print("Ini adalah package gempaterkini")
"""