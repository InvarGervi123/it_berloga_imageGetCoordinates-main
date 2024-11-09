from PIL import Image, ExifTags

# פתיחת תמונה
img = Image.open("20221129_115957.jpg")
exif_data = img._getexif()

# בדיקה אם קיימים נתוני Exif
if exif_data:
    exif = {ExifTags.TAGS.get(k): v for k, v in exif_data.items() if k in ExifTags.TAGS}
else:
    exif = {}

# פונקציה להמרת קואורדינטות לפורמט עשרוני
def dms_to_decimal(dms_tuple, direction):
    degrees, minutes, seconds = dms_tuple
    decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
    if direction in ['S', 'W']:
        decimal = -decimal
    return decimal

# כתיבת נתוני Exif לקובץ טקסט
with open("image_metadata.txt", "w") as file:
    file.write("Metadata Information:\n")
    
    if exif:
        for tag, value in exif.items():
            file.write(f"{tag}: {value}\n")
    else:
        file.write("No Exif data found\n")
    
    # בדיקה אם קיימים נתוני GPS
    if "GPSInfo" in exif:
        gps_info = exif["GPSInfo"]
        print("Raw GPS Data:", gps_info)  # הדפסת נתוני GPS גולמיים
        
        try:
            # קבלת נתוני קואורדינטות
            lat_dms = gps_info.get(2)
            lat_direction = gps_info.get(1)

            lon_dms = gps_info.get(4)
            lon_direction = gps_info.get(3)

            # בדיקה אם קיימים כל נתוני הקואורדינטות
            if lat_dms and lat_direction and lon_dms and lon_direction:
                # המרת הקואורדינטות לפורמט עשרוני
                latitude_decimal = dms_to_decimal(lat_dms, lat_direction)
                longitude_decimal = dms_to_decimal(lon_dms, lon_direction)

                # שרשור הקואורדינטות לפורמט המתאים ל-Google Maps
                gps_decimal = f"{latitude_decimal}, {longitude_decimal}"
                print("Decimal GPS Coordinates:", gps_decimal)  # הדפסת הקואורדינטות בפורמט עשרוני
                
                # כתיבת קואורדינטות בפורמט לשימוש ב-Google Maps
                file.write("\nGPS Coordinates (for Google Maps):\n")
                file.write(gps_decimal + "\n")
            else:
                file.write("Incomplete GPS information found\n")
        except Exception as e:
            file.write("\nError processing GPS information\n")
            print("Error processing GPS information:", e)
    else:
        file.write("No GPS information found\n")

print("Metadata saved to image_metadata.txt")
