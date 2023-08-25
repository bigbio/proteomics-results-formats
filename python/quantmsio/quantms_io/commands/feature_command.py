import click

from quantms_io.core.feature import FeatureHandler


@click.command("convert-feature-file", short_help="Convert msstats/mztab to parquet file")
@click.option("--sdrf_file", help="the SDRF file needed to extract some of the metadata", required=True)
@click.option("--msstats_file", help="the MSstats input file, this will be considered the main format to convert", required=True)
@click.option("--mztab_file", help="the mzTab file, this will be used to extract the protein information", required=True)
@click.option("--output_folder", help="Folder where the Json file will be generated", required=True)
@click.option("--output_file", help="Prefix of parquet file", required=False)
@click.option("--delete_existing", help="Delete existing files in the output folder", is_flag=True)
def convert_feature_file(sdrf_file: str, msstats_file: str, mztab_file: str, output_folder: str,
                         output_file: str, delete_existing: bool):
    """
    Convert a msstats/mztab file to a parquet file. The parquet file will contain the features and the metadata.
    :param sdrf_file: the SDRF file needed to extract some of the metadata
    :param msstats_file: the MSstats input file, this will be considered the main format to convert
    :param mztab_file: the mzTab file, this will be used to extract the protein information
    :param output_folder: Folder where the Json file will be generated
    :param output_file: Prefix of the Json file needed to generate the file name
    :param delete_existing: Delete existing files in the output folder
    :return: none
    """

    if sdrf_file is None or msstats_file is None or mztab_file is None or output_folder is None:
        raise click.UsageError("Please provide all the required parameters")

    feature_manager = FeatureHandler()
    feature_manager.parquet_path = output_folder + "/" + output_file + ".parquet"
    feature_manager.convert_mztab_msstats_to_feature(
        mztab_file=mztab_file,
        msstats_file=msstats_file,
        sdrf_file=sdrf_file, use_cache=True
    )



