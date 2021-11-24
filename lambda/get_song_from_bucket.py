import json
import urllib
import boto3

S3URI = {
    " ": "+",
    "&": "%26"
}


def lambda_handler(event, context):
    # TODO implement
    region = 'eu-west-3'
    bucket_name_source = 'test-jeiffer-projet'
    s3 = boto3.client('s3')
    list_songs = []
    resp = s3.list_objects_v2(Bucket=bucket_name_source)
    for obj in resp['Contents']:
        artist, title = obj['Key'].split("-")
        artist = artist.strip()
        title = title.replace('.wav', '').strip()
        url_suffix = obj['Key']
        for spec_charac in S3URI.keys():
            url_suffix = url_suffix.replace(spec_charac, S3URI[spec_charac])
        url_obj = 'https://' + bucket_name_source + '.s3.' + region + '.amazonaws.com/' + url_suffix
        elt = {"name": title, "file": url_obj, "artist": artist}
        list_songs.append(elt)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type,Authorization,X-Amz-Date,X-Api-Key,X-Amz-Security-Token',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET'
        },
        'body': json.dumps(list_songs)
    }
