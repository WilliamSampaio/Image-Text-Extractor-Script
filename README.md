# Image Text Extractor Script

## Dependencies

Requires the libraries `tesseract >= 5.4.1`, `imagemagick >= 7.1.1-36` and `bc >= 1.07.1`.

Example installation command (Manjaro):

```bash
pamac install tesseract imagemagick bc
```

## Usage

The accepted extensions are `jpg`, `jpeg` and `png`.

Run to extract text:

```bash
./scanner.py /path/to/images
```

In the same directory of the images that was informed when executing the command, a `txt` will be generated with the extracted information. An image with the suffix `_converted` will also be generated, this is the image processed for better reading.

To clear the path (remove `txt` and images with `_converted`):

```bash
./scanner.py /path/to/images --clear
```
