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
def dms_to_decimal(degrees, minutes, seconds, direction):
    decimal = degrees + minutes / 60 + seconds / 3600
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
        def gps_info_to_string(gps_info):
            lat_degrees, lat_minutes, lat_seconds = gps_info[2]
            lat_direction = gps_info[1]

            lon_degrees, lon_minutes, lon_seconds = gps_info[4]
            lon_direction = gps_info[3]

            # המרת הקואורדינטות לפורמט עשרוני
            latitude_decimal = dms_to_decimal(lat_degrees, lat_minutes, lat_seconds, lat_direction)
            longitude_decimal = dms_to_decimal(lon_degrees, lon_minutes, lon_seconds, lon_direction)

            # שרשור התוצאה לשימוש ישיר ב-Google Maps
            return f"{latitude_decimal}, {longitude_decimal}"

        gps_decimal = gps_info_to_string(exif["GPSInfo"])
        file.write("\nGPS Coordinates (for Google Maps):\n")
        file.write(gps_decimal + "\n")
    else:
        file.write("No GPS information found\n")

print("Metadata saved to image_metadata.txt")
