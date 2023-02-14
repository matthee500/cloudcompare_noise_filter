import os
import subprocess


def cloud_compare_ss(direct, cc):
    # create a 'processed' directory within the specified directory
    sor_processed_directory = os.path.join(direct, 'processed')
    os.makedirs(sor_processed_directory, exist_ok=True)

    # iterate through all files in the specified directory
    for i, filename in enumerate(os.listdir(direct), start=1):
        # check if the current file is a regular file with a '.e57' extension
        if os.path.isfile(os.path.join(direct, filename)) and filename.endswith('.e57'):
            # generate the input and output file paths
            input_file = os.path.join(direct, filename)
            output_file = os.path.join(sor_processed_directory, f'nf{i}.e57')
            
            # call CloudCompare using subprocess to process the input file and save the output file
            subprocess.check_call([
                cc, '-SILENT', '-NO_TIMESTAMP', '-AUTO_SAVE', 'OFF', '-C_EXPORT_FMT', 'E57',
                '-NOISE', '-O', '-GLOBAL_SHIFT', 'AUTO', input_file,
                '-DROP_GLOBAL_SHIFT', '-SAVE_CLOUDS', 'FILE', output_file
            ], shell=True)


if __name__ == '__main__':
    # prompt the user to input the directory containing the e57 files
    directory = input('Input directory containing e57s: ')

    # Prompt the user to input a value for the type of noise removal to use: KNN or RADIUS
    noise_value_1_input = input('Input 1 for KNN (number of neighbors) or 2 for RADIUS (spherical neighborhood)')

    # Use a dictionary to map input values to noise removal types
    noise_types = {'1': 'KNN', '2': 'RADIUS'}

    # Look up the noise removal type based on the input value
    noise_value_1 = noise_types.get(noise_value_1_input)

    # If the input value is not valid, print an error message
    if noise_value_1 is None:
        print('Input incorrect')

    # set the path to the CloudCompare executable
    cloud_compare = r'C:\Program Files\CloudCompare\CloudCompare.exe'
    
    # call the cloud_compare_ss function with the specified directory and CloudCompare executable
    cloud_compare_ss(directory, cloud_compare)
