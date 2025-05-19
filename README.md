# it\_berloga\_imageGetCoordinates

A Python script for extracting geographic coordinates (GPS) from an image's metadata (EXIF).

## Repository Contents

* `main.py` – The main script that handles image reading and metadata extraction.
* `image_metadata.txt` – Example metadata output or format documentation.
* `20221129_115957.jpg` – Sample image with embedded metadata.

## Requirements

* Python 3.7+
* Libraries:

  * `Pillow` (for reading image files and EXIF data)
  * `piexif` (for reading/writing EXIF) or `exifread`

```bash
pip install Pillow piexif
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/InvarGervi123/it_berloga_imageGetCoordinates-main.git
   cd it_berloga_imageGetCoordinates-main
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   *(If there is no `requirements.txt`, just run the command above manually.)*

## Usage

```bash
python main.py path/to/your/image.jpg
```

The script will read the image metadata, look for GPS fields (Latitude, Longitude), and print them in the format:

```
Latitude: xx.xxxxxx
Longitude: yy.yyyyyy
```

If no GPS data is found, you’ll see:

```
No GPS info found in image.
```

### Example

```bash
python main.py 20221129_115957.jpg
# Output:
# Latitude: 31.7767
# Longitude: 35.2345
```

## Code Structure (Assumed)

In `main.py`, the script likely:

1. Loads the image using `Pillow.Image`.
2. Extracts EXIF data using `piexif.load()` or `exifread`.
3. Retrieves GPS fields (GPSLatitude, GPSLongitude, GPSLatitudeRef, GPSLongitudeRef).
4. Converts degrees/minutes/seconds to decimal format.
5. Prints the result.

## Possible Future Improvements

* JSON or CSV output support.
* Batch processing for entire folders.
* Extract additional metadata (timestamp, camera model).
* Advanced CLI interface using `argparse` or `click`.

## Contributing

1. Open an issue for bugs or feature requests.
2. Submit a pull request with improvements.
