# Exificator

Exificator is a Python command line application that allows you to modify EXIF metadata in JPEG images.

## Installation

To install Exificator, you can use pip:

```sh
$ pip install exificator
``````


## Usage

Exificator can be used to modify the EXIF metadata in JPEG images. Here's an example of how to use it:

```sh
$ exificator input.jpg -o output.jpg --payload '<script>alert(1337)</script>'
```


This will modify the title and description fields in the EXIF metadata of the input image and save the modified image to the output file.

Here are the available options:

```
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output filename. By default, filename-output.ext
  -f, --force           Overwrite output file if exists without confirmation
  -p PAYLOAD, --payload PAYLOAD
                        String to set in EXIF attributes. {} is replaced with the exif tag. Default: "<script>alert('{}')</script>
  --tags TAGS           List of tags to set, comma separated. Default: all tags
  --list-tags           List all available tags
```


## License

Exificator is licensed under the MIT License. See LICENSE for more information.