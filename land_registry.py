import pandas as pd
import urllib.parse
import fetch

column_names = [
        'uid',
        'price',
        'transfer_date',
        'postcode',

        # D = Detached, S = Semi-Detached, T = Terraced, F = Flats/Maisonettes, O = Other
        'type',

        # Y means new build
        'new_build',

        # F = Freehold, L= Leasehold etc.
        'duration',

        # primary house number or name
        'paon',

        # secondary house number (ex flat # in a building @ paon)
        'saon',

        'street',
        'locality',
        'town',
        'district',
        'county',

        # Indicates the type of Price Paid transaction.
        # A = Standard Price Paid entry, includes single residential property sold for full market value.
        # B = Additional Price Paid entry including transfers under a power of sale/repossessions, buy-to-lets (where they can be identified by a Mortgage) and transfers to non-private individuals.
        #
        # Note that category B does not separately identify the transaction types stated.
        # HM Land Registry has been collecting information on Category A transactions from January 1995. Category B transactions were identified from October 2013.
        'ppd',

        # Monthly file Indicates additions, changes and deletions to the records.(see guide below).
        # A = Addition
        # C = Change
        # D = Delete
        'record_status'

    ]

base_url = 'http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/'

monthly_file = urllib.parse.urljoin(base_url, 'pp-monthly-update-new-version.csv')

full_file = urllib.parse.urljoin(base_url, 'pp-complete.csv')


def to_df(file_path):
    """ Convert full file to a DataFrame """
    return pd.read_csv(file_path, parse_dates=True, header=None, index_col='transfer_date', names=column_names)


def fetch_monthly(to_file='./tmp/pp-monthly.csv'):
    fetch.download_file(monthly_file, to_file)


if __name__ == '__main__':
    fetch_monthly()